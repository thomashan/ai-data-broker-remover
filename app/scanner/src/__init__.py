"""AI Data Broker Remover - A tool to help remove personal data from data brokers."""

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from .core.manager import DataBrokerManager
from .core.base import DataBroker, PersonalInfo, RemovalRequest, RemovalStatus

__all__ = ["DataBrokerManager", "DataBroker", "PersonalInfo", "RemovalRequest", "RemovalStatus"]
