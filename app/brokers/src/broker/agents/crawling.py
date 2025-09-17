from typing import Dict, Any, List
from .base import BaseAgent
import asyncio
import httpx
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse

class CrawlingAgent(BaseAgent):
    """Agent responsible for crawling broker websites to extract detailed information."""
    
    def __init__(self, agent_id: str):
        super().__init__(agent_id, "Crawling Agent")
        
    async def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Crawl broker websites to extract detailed information.
        
        Args:
            data: Contains brokers to crawl
            
        Returns:
            Dictionary with crawled broker information
        """
        self.update_activity()
        
        brokers = data.get("brokers", [])
        crawled_brokers = []
        success_count = 0
        failed_count = 0
        
        # Process each broker asynchronously
        for broker in brokers:
            try:
                crawled_broker = await self._crawl_broker(broker)
                crawled_broker["last_crawled"] = self.last_active.isoformat()
                crawled_broker["crawled_status"] = "success"
                crawled_brokers.append(crawled_broker)
                success_count += 1
            except Exception as e:
                # If crawling fails, return the original broker with error info
                failed_broker = broker.copy()
                failed_broker["last_crawled"] = self.last_active.isoformat()
                failed_broker["crawled_status"] = "error"
                failed_broker["crawled_error"] = str(e)
                crawled_brokers.append(failed_broker)
                failed_count += 1
                
        return {
            "crawled_brokers": crawled_brokers,
            "total_crawled": len(crawled_brokers),
            "success_count": success_count,
            "failed_count": failed_count
        }
        
    async def _crawl_broker(self, broker: Dict[str, Any]) -> Dict[str, Any]:
        """Crawl a single broker's website."""
        url = broker["url"]
        crawled_broker = broker.copy()
        
        # Use httpx for async HTTP requests
        async with httpx.AsyncClient(timeout=10.0) as client:
            try:
                response = await client.get(url)
                response.raise_for_status()
                
                # Parse HTML content
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Extract title
                title = soup.find('title')
                if title:
                    crawled_broker["extracted_title"] = title.get_text().strip()
                
                # Extract meta description
                meta_desc = soup.find('meta', attrs={'name': 'description'})
                if meta_desc:
                    crawled_broker["extracted_description"] = meta_desc.get('content', '')
                    
                # Try to find privacy policy link
                privacy_links = soup.find_all('a', href=re.compile(r'(privacy|policy)', re.I))
                if privacy_links:
                    privacy_url = urljoin(url, privacy_links[0]['href'])
                    crawled_broker["privacy_policy_url"] = privacy_url
                    
                # Try to find opt-out or do not sell links
                optout_patterns = [
                    r'(opt[-]?out|do not sell|delete my data|remove my data|unsubscribe)',
                    r'(opt[-]out|donotsell|deletemydata|removemydata|unsubscribe)'
                ]
                
                optout_links = []
                for pattern in optout_patterns:
                    links = soup.find_all('a', href=re.compile(pattern, re.I))
                    for link in links:
                        optout_url = urljoin(url, link['href'])
                        optout_links.append({
                            "url": optout_url,
                            "text": link.get_text().strip()
                        })
                        
                if optout_links:
                    crawled_broker["opt_out_urls"] = optout_links
                    # Set the first one as the primary opt-out URL
                    crawled_broker["opt_out_url"] = optout_links[0]["url"]
                    
                # Extract contact information
                contact_links = soup.find_all('a', href=re.compile(r'(contact|support|help)', re.I))
                if contact_links:
                    contact_url = urljoin(url, contact_links[0]['href'])
                    crawled_broker["contact_url"] = contact_url
                    
            except Exception as e:
                crawled_broker["crawling_error"] = str(e)
                
        return crawled_broker