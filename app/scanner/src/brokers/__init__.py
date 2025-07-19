"""Data broker implementations."""

from .whitepages import WhitePages
from .spokeo import Spokeo
from .peoplefinder import PeopleFinder

# Registry of all available brokers
AVAILABLE_BROKERS = {
    "whitepages": WhitePages,
    "spokeo": Spokeo,
    "peoplefinder": PeopleFinder,
}

__all__ = ["WhitePages", "Spokeo", "PeopleFinder", "AVAILABLE_BROKERS"]
