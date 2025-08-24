from typing import Dict, Any, List
from .base import BaseAgent

class ClassificationAgent(BaseAgent):
    """Agent responsible for categorizing brokers and applying regulatory tags."""
    
    def __init__(self, agent_id: str):
        super().__init__(agent_id, "Classification Agent")
        self.categories = [
            "People search websites",
            "Marketing data brokers",
            "Risk mitigation data brokers",
            "Credit reporting agencies",
            "Background check websites",
            "Marketing research agencies",
            "Large data aggregators",
            "Recruitment data brokers",
            "Financial information brokers",
            "Health information data brokers",
            "Other Data Brokers",
            "Unexpected Data Brokers"
        ]
        
        self.regulations = [
            "GDPR",
            "CCPA",
            "COPPA",
            "GLBA",
            "FCRA"
        ]
        
    async def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Classify brokers and apply regulatory tags.
        
        Args:
            data: Contains brokers to classify
            
        Returns:
            Dictionary with classified brokers
        """
        self.update_activity()
        
        brokers = data.get("brokers", [])
        classified_brokers = []
        
        # Simple classification logic (in reality, this would use ML or rules)
        for broker in brokers:
            classified_broker = broker.copy()
            
            # Assign category based on name/url keywords (simplified)
            name = broker.get("name", "").lower()
            url = broker.get("url", "").lower()
            description = broker.get("description", "").lower()
            
            category = "Other Data Brokers"  # default
            regulations = ["GDPR"]  # Default regulation for all brokers
            
            # Simple keyword matching for category
            if "people" in name or "people" in description:
                category = "People search websites"
            elif "marketing" in name or "marketing" in description:
                category = "Marketing data brokers"
            elif "credit" in name or "credit" in description:
                category = "Credit reporting agencies"
                regulations.append("FCRA")
            elif "background" in name or "background" in description:
                category = "Background check websites"
                regulations.append("FCRA")
            elif "health" in name or "health" in description:
                category = "Health information data brokers"
                regulations.extend(["GDPR", "HIPAA"])
            elif "financial" in name or "financial" in description:
                category = "Financial information brokers"
                regulations.extend(["GLBA", "GDPR"])
                
            # Assign regulations based on category and location
            if "gdpr" in name or "eu" in url:
                regulations.append("GDPR")
            if "ccpa" in name or "california" in description:
                regulations.append("CCPA")
                
            # Remove duplicates
            regulations = list(set(regulations))
            
            classified_broker.update({
                "category": category,
                "regulations": regulations,
                "last_classified": self.last_active.isoformat()
            })
            
            classified_brokers.append(classified_broker)
            
        return {
            "classified_brokers": classified_brokers,
            "total_classified": len(classified_brokers),
            "categories_used": list(set(broker["category"] for broker in classified_brokers))
        }