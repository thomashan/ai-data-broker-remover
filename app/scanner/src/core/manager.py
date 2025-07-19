"""Manager for coordinating data broker removal requests."""

import asyncio
from typing import List, Dict, Type, Optional
import logging

from .base import DataBroker, PersonalInfo, RemovalRequest, RemovalStatus


logger = logging.getLogger(__name__)


class DataBrokerManager:
    """Manages multiple data broker removal operations."""
    
    def __init__(self):
        self._brokers: Dict[str, DataBroker] = {}
        self._requests: List[RemovalRequest] = []
    
    def register_broker(self, broker: DataBroker) -> None:
        """Register a data broker implementation.
        
        Args:
            broker: DataBroker implementation to register
        """
        self._brokers[broker.name] = broker
        logger.info(f"Registered broker: {broker.name}")
    
    def get_broker(self, name: str) -> Optional[DataBroker]:
        """Get a registered broker by name.
        
        Args:
            name: Name of the broker to retrieve
            
        Returns:
            DataBroker instance or None if not found
        """
        return self._brokers.get(name)
    
    def list_brokers(self) -> List[str]:
        """Get list of registered broker names.
        
        Returns:
            List of broker names
        """
        return list(self._brokers.keys())
    
    async def submit_removal_to_broker(self, broker_name: str, personal_info: PersonalInfo) -> RemovalRequest:
        """Submit removal request to a specific broker.
        
        Args:
            broker_name: Name of the broker
            personal_info: Personal information for removal
            
        Returns:
            RemovalRequest object
            
        Raises:
            ValueError: If broker not found or personal info invalid
        """
        broker = self.get_broker(broker_name)
        if not broker:
            raise ValueError(f"Broker '{broker_name}' not registered")
        
        if not broker.validate_personal_info(personal_info):
            raise ValueError(f"Invalid personal info for broker '{broker_name}'")
        
        request = await broker.submit_removal_request(personal_info)
        self._requests.append(request)
        logger.info(f"Submitted removal request to {broker_name}")
        
        return request
    
    async def submit_removal_to_all(self, personal_info: PersonalInfo) -> List[RemovalRequest]:
        """Submit removal request to all registered brokers.
        
        Args:
            personal_info: Personal information for removal
            
        Returns:
            List of RemovalRequest objects
        """
        requests = []
        
        for broker_name in self.list_brokers():
            try:
                request = await self.submit_removal_to_broker(broker_name, personal_info)
                requests.append(request)
            except Exception as e:
                logger.error(f"Failed to submit to {broker_name}: {e}")
                # Create a failed request record
                failed_request = RemovalRequest(
                    broker_name=broker_name,
                    personal_info=personal_info,
                    status=RemovalStatus.FAILED,
                    notes=str(e)
                )
                requests.append(failed_request)
                self._requests.append(failed_request)
        
        return requests
    
    async def check_all_statuses(self) -> List[RemovalRequest]:
        """Check status of all pending removal requests.
        
        Returns:
            List of updated RemovalRequest objects
        """
        updated_requests = []
        
        for request in self._requests:
            if request.status in [RemovalStatus.PENDING, RemovalStatus.IN_PROGRESS]:
                broker = self.get_broker(request.broker_name)
                if broker:
                    try:
                        new_status = await broker.check_removal_status(request)
                        request.status = new_status
                        logger.info(f"Updated {request.broker_name} status to {new_status}")
                    except Exception as e:
                        logger.error(f"Failed to check status for {request.broker_name}: {e}")
                        request.status = RemovalStatus.FAILED
                        request.notes = str(e)
                
                updated_requests.append(request)
        
        return updated_requests
    
    def get_requests_by_status(self, status: RemovalStatus) -> List[RemovalRequest]:
        """Get all requests with a specific status.
        
        Args:
            status: Status to filter by
            
        Returns:
            List of matching RemovalRequest objects
        """
        return [req for req in self._requests if req.status == status]
    
    def get_completion_summary(self) -> Dict[str, int]:
        """Get summary of request completion status.
        
        Returns:
            Dictionary with counts by status
        """
        summary = {}
        for status in RemovalStatus:
            summary[status.value] = len(self.get_requests_by_status(status))
        
        return summary
