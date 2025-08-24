from typing import Dict, Any, List
from .base import BaseAgent
import asyncio
import httpx
from datetime import datetime

class MonitoringAgent(BaseAgent):
    """Agent responsible for monitoring existing brokers for changes."""
    
    def __init__(self, agent_id: str):
        super().__init__(agent_id, "Monitoring Agent")
        
    async def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Monitor existing brokers for changes.
        
        Args:
            data: Contains brokers to monitor
            
        Returns:
            Dictionary with monitoring results
        """
        self.update_activity()
        
        brokers = data.get("brokers", [])
        monitored_brokers = []
        unchanged_count = 0
        changed_count = 0
        error_count = 0
        
        # Process each broker asynchronously
        for broker in brokers:
            try:
                monitored_broker = await self._monitor_broker(broker)
                monitored_broker["last_monitored"] = self.last_active.isoformat()
                
                # Determine if there were changes (simplified logic)
                if monitored_broker.get("status_code") == 200:
                    monitored_broker["monitoring_status"] = "success"
                    monitored_broker["monitoring_message"] = "Website is accessible"
                    unchanged_count += 1
                else:
                    monitored_broker["monitoring_status"] = "warning"
                    monitored_broker["monitoring_message"] = f"Website returned status {monitored_broker.get('status_code')}"
                    changed_count += 1
                    
                monitored_brokers.append(monitored_broker)
                
            except Exception as e:
                # If monitoring fails, return the original broker with error info
                error_broker = broker.copy()
                error_broker["last_monitored"] = self.last_active.isoformat()
                error_broker["monitoring_status"] = "error"
                error_broker["monitoring_message"] = str(e)
                monitored_brokers.append(error_broker)
                error_count += 1
                
        return {
            "monitored_brokers": monitored_brokers,
            "total_monitored": len(monitored_brokers),
            "unchanged_count": unchanged_count,
            "changed_count": changed_count,
            "error_count": error_count
        }
        
    async def _monitor_broker(self, broker: Dict[str, Any]) -> Dict[str, Any]:
        """Monitor a single broker's website status."""
        url = broker["url"]
        monitored_broker = broker.copy()
        
        # Use httpx for async HTTP requests
        async with httpx.AsyncClient(timeout=10.0) as client:
            try:
                response = await client.head(url)  # Use HEAD to minimize data transfer
                monitored_broker["status_code"] = response.status_code
                monitored_broker["response_time"] = response.elapsed.total_seconds()
                
                # If HEAD fails, try GET
                if response.status_code >= 400:
                    response = await client.get(url)
                    monitored_broker["status_code"] = response.status_code
                    monitored_broker["response_time"] = response.elapsed.total_seconds()
                    
            except Exception as e:
                monitored_broker["monitoring_error"] = str(e)
                monitored_broker["status_code"] = 0
                
        return monitored_broker