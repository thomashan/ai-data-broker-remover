"""Base classes for data broker removal implementations."""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enum import Enum


class RemovalStatus(Enum):
    """Status of removal request."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress" 
    COMPLETED = "completed"
    FAILED = "failed"
    NOT_FOUND = "not_found"


@dataclass
class PersonalInfo:
    """Personal information for removal requests."""
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    date_of_birth: Optional[str] = None


@dataclass
class RemovalRequest:
    """Represents a removal request to a data broker."""
    broker_name: str
    personal_info: PersonalInfo
    status: RemovalStatus = RemovalStatus.PENDING
    request_id: Optional[str] = None
    submission_date: Optional[str] = None
    completion_date: Optional[str] = None
    notes: Optional[str] = None


class DataBroker(ABC):
    """Abstract base class for data broker implementations."""
    
    def __init__(self, name: str, url: str, **kwargs):
        self.name = name
        self.url = url
        self.config = kwargs
    
    @abstractmethod
    async def search_records(self, personal_info: PersonalInfo) -> List[Dict[str, Any]]:
        """Search for records matching the personal information.
        
        Args:
            personal_info: Personal information to search for
            
        Returns:
            List of found records
        """
        pass
    
    @abstractmethod
    async def submit_removal_request(self, personal_info: PersonalInfo) -> RemovalRequest:
        """Submit a removal request to the data broker.
        
        Args:
            personal_info: Personal information for removal
            
        Returns:
            RemovalRequest object with initial status
        """
        pass
    
    @abstractmethod
    async def check_removal_status(self, request: RemovalRequest) -> RemovalStatus:
        """Check the status of a removal request.
        
        Args:
            request: The removal request to check
            
        Returns:
            Current status of the removal request
        """
        pass
    
    def get_required_fields(self) -> List[str]:
        """Get list of required personal info fields for this broker.
        
        Returns:
            List of required field names
        """
        return ["first_name", "last_name", "email"]
    
    def validate_personal_info(self, personal_info: PersonalInfo) -> bool:
        """Validate that personal info contains required fields.
        
        Args:
            personal_info: Personal information to validate
            
        Returns:
            True if valid, False otherwise
        """
        required_fields = self.get_required_fields()
        for field in required_fields:
            if not hasattr(personal_info, field) or not getattr(personal_info, field):
                return False
        return True
