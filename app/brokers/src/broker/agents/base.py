from abc import ABC, abstractmethod
from typing import Dict, Any, List
from pathlib import Path
import json
from datetime import datetime

class BaseAgent(ABC):
    """Base class for all agents in the self-organizing network."""
    
    def __init__(self, agent_id: str, name: str):
        self.agent_id = agent_id
        self.name = name
        self.created_at = datetime.now()
        self.last_active = datetime.now()
        
    @abstractmethod
    async def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Process data and return results.
        
        Args:
            data: Input data for processing
            
        Returns:
            Processed results
        """
        pass
        
    def update_activity(self):
        """Update the last active timestamp."""
        self.last_active = datetime.now()
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert agent to dictionary representation."""
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "type": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),
            "last_active": self.last_active.isoformat()
        }
        
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'BaseAgent':
        """Create agent from dictionary representation."""
        agent = cls(data["agent_id"], data["name"])
        agent.created_at = datetime.fromisoformat(data["created_at"])
        agent.last_active = datetime.fromisoformat(data["last_active"])
        return agent