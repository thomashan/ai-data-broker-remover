#!/usr/bin/env python3
"""
Demo script showing how the self-organizing agent network works with real internet data.
"""

import asyncio
import sys
from pathlib import Path

# Add the src directory to the path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from broker.agents import (
    DiscoveryAgent,
    DeduplicationAgent,
    CrawlingAgent,
    MonitoringAgent,
    ClassificationAgent,
    CoordinationAgent
)

async def main():
    print("=== Self-Organizing Data Broker Discovery Agent Network Demo ===\n")
    
    # Create a coordination agent to manage the workflow
    coordinator = CoordinationAgent("demo_coordinator")
    
    # Define a simple workflow
    workflow_data = {
        "workflow": [
            {
                "name": "discovery",
                "data": {
                    "keywords": ["data broker", "people search", "background check"],
                    "max_results": 3
                }
            }
        ]
    }
    
    print("1. Running discovery workflow...")
    result = await coordinator.process(workflow_data)
    print(f"   Discovered {result['workflow_results']['discovery']['total_found']} brokers")
    
    # Show discovered brokers
    discovered_brokers = result['workflow_results']['discovery']['discovered_brokers']
    print("   Discovered brokers:")
    for broker in discovered_brokers:
        print(f"   - {broker['name']} ({broker['url']})")
    print()
    
    # Run classification on discovered brokers
    print("2. Classifying discovered brokers...")
    classifier = ClassificationAgent("demo_classifier")
    classification_result = await classifier.process({"brokers": discovered_brokers})
    print(f"   Classified {classification_result['total_classified']} brokers")
    print(f"   Categories used: {', '.join(classification_result['categories_used'])}\n")
    
    # Run crawling on classified brokers (this will take a moment)
    print("3. Crawling broker websites (this may take a moment)...")
    crawler = CrawlingAgent("demo_crawler")
    crawling_result = await crawler.process({"brokers": classification_result['classified_brokers']})
    print(f"   Crawled {crawling_result['total_crawled']} brokers")
    print(f"   Success: {crawling_result['success_count']}, Failed: {crawling_result['failed_count']}\n")
    
    # Run monitoring on crawled brokers
    print("4. Monitoring broker status...")
    monitor = MonitoringAgent("demo_monitor")
    monitoring_result = await monitor.process({"brokers": crawling_result['crawled_brokers']})
    print(f"   Monitored {monitoring_result['total_monitored']} brokers")
    print(f"   Accessible: {monitoring_result['unchanged_count']}, Issues: {monitoring_result['changed_count'] + monitoring_result['error_count']}\n")
    
    # Show final results
    print("=== Final Results ===")
    for broker in monitoring_result['monitored_brokers']:
        print(f"- {broker['name']}")
        print(f"  URL: {broker['url']}")
        print(f"  Category: {broker.get('category', 'N/A')}")
        print(f"  Regulations: {', '.join(broker.get('regulations', []))}")
        print(f"  Status: {broker.get('monitoring_status', 'N/A')} ({broker.get('status_code', 'N/A')})")
        
        # Show opt-out information if available
        if 'opt_out_url' in broker:
            print(f"  Opt-out URL: {broker['opt_out_url']}")
        elif 'opt_out_urls' in broker:
            print(f"  Opt-out URLs: {len(broker['opt_out_urls'])} found")
            
        # Show any errors
        if broker.get('crawling_error'):
            print(f"  Crawling Error: {broker['crawling_error']}")
        if broker.get('monitoring_error'):
            print(f"  Monitoring Error: {broker['monitoring_error']}")
        print()

if __name__ == "__main__":
    asyncio.run(main())