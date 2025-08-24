"""Agent modules for the self-organizing data broker discovery system."""

from .base import BaseAgent
from .discovery import DiscoveryAgent
from .deduplication import DeduplicationAgent
from .crawling import CrawlingAgent
from .monitoring import MonitoringAgent
from .classification import ClassificationAgent
from .coordination import CoordinationAgent

__all__ = [
    "BaseAgent",
    "DiscoveryAgent",
    "DeduplicationAgent",
    "CrawlingAgent",
    "MonitoringAgent",
    "ClassificationAgent",
    "CoordinationAgent"
]