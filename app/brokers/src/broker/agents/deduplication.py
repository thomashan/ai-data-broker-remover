from typing import Dict, Any, List
from .base import BaseAgent

class DeduplicationAgent(BaseAgent):
    """Agent responsible for identifying and merging duplicate broker entries."""
    
    def __init__(self, agent_id: str):
        super().__init__(agent_id, "Deduplication Agent")
        
    async def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Identify and merge duplicate broker entries.
        
        Args:
            data: Contains list of brokers to deduplicate
            
        Returns:
            Dictionary with deduplicated brokers
        """
        self.update_activity()
        
        brokers = data.get("brokers", [])
        existing_brokers = data.get("existing_brokers", [])
        
        # Simple deduplication logic (in reality, this would be more sophisticated)
        unique_brokers = []
        processed_urls = set()
        processed_names = set()
        
        # Check existing brokers first
        for broker in existing_brokers:
            url = broker.get("url", "").lower()
            name = broker.get("name", "").lower()
            processed_urls.add(url)
            processed_names.add(name)
            unique_brokers.append(broker)
            
        # Process new brokers
        new_brokers = []
        duplicate_brokers = []
        
        for broker in brokers:
            url = broker.get("url", "").lower()
            name = broker.get("name", "").lower()
            
            # Check if this is a duplicate
            if url in processed_urls or name in processed_names:
                duplicate_brokers.append(broker)
                # In a real implementation, we would merge the data
            else:
                processed_urls.add(url)
                processed_names.add(name)
                new_brokers.append(broker)
                unique_brokers.append(broker)
                
        return {
            "unique_brokers": unique_brokers,
            "new_brokers": new_brokers,
            "duplicate_brokers": duplicate_brokers,
            "total_unique": len(unique_brokers)
        }