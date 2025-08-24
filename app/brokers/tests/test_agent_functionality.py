import pytest
import asyncio
from pathlib import Path
import sys

# Add the src directory to the path so we can import the agents
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

# Test that the agent modules can be imported and instantiated
def test_agent_imports():
    """Test that all agent classes can be imported."""
    from broker.agents import (
        BaseAgent,
        DiscoveryAgent,
        DeduplicationAgent,
        CrawlingAgent,
        MonitoringAgent,
        ClassificationAgent,
        CoordinationAgent
    )
    
    # Verify that classes exist
    assert BaseAgent is not None
    assert DiscoveryAgent is not None
    assert DeduplicationAgent is not None
    assert CrawlingAgent is not None
    assert MonitoringAgent is not None
    assert ClassificationAgent is not None
    assert CoordinationAgent is not None

# Test that agents can be instantiated
def test_agent_instantiation():
    """Test that all agent classes can be instantiated."""
    from broker.agents import (
        DiscoveryAgent,
        DeduplicationAgent,
        CrawlingAgent,
        MonitoringAgent,
        ClassificationAgent,
        CoordinationAgent
    )
    
    discovery = DiscoveryAgent("test_discovery")
    dedup = DeduplicationAgent("test_dedup")
    crawling = CrawlingAgent("test_crawling")
    monitoring = MonitoringAgent("test_monitoring")
    classification = ClassificationAgent("test_classification")
    coordination = CoordinationAgent("test_coordination")
    
    # Verify that instances are created
    assert discovery is not None
    assert dedup is not None
    assert crawling is not None
    assert monitoring is not None
    assert classification is not None
    assert coordination is not None

# Test agent processing (async)
@pytest.mark.asyncio
async def test_discovery_agent_processing():
    """Test that discovery agent can process data."""
    from broker.agents import DiscoveryAgent
    
    agent = DiscoveryAgent("test_discovery")
    data = {
        "keywords": ["data broker", "people search"],
        "max_results": 5
    }
    
    result = await agent.process(data)
    
    # Verify result structure
    assert "discovered_brokers" in result
    assert "total_found" in result
    assert "sources_queried" in result
    
    # Verify content
    assert result["total_found"] >= 0
    assert isinstance(result["discovered_brokers"], list)

@pytest.mark.asyncio
async def test_deduplication_agent_processing():
    """Test that deduplication agent can process data."""
    from broker.agents import DeduplicationAgent
    
    agent = DeduplicationAgent("test_dedup")
    
    # Test data with duplicates
    data = {
        "brokers": [
            {"name": "Broker A", "url": "https://broker-a.com"},
            {"name": "Broker B", "url": "https://broker-b.com"}
        ],
        "existing_brokers": [
            {"name": "Broker A", "url": "https://broker-a.com"},
            {"name": "Broker C", "url": "https://broker-c.com"}
        ]
    }
    
    result = await agent.process(data)
    
    # Verify result structure
    assert "unique_brokers" in result
    assert "new_brokers" in result
    assert "duplicate_brokers" in result
    assert "total_unique" in result
    
    # Verify deduplication worked
    assert result["total_unique"] == 3  # A, B, C
    assert len(result["new_brokers"]) == 1  # Only B is new
    assert len(result["duplicate_brokers"]) == 1  # A is duplicate

@pytest.mark.asyncio
async def test_crawling_agent_processing():
    """Test that crawling agent can process data."""
    from broker.agents import CrawlingAgent
    
    agent = CrawlingAgent("test_crawling")
    
    data = {
        "brokers": [
            {"name": "Test Broker", "url": "https://httpbin.org/get"}
        ]
    }
    
    result = await agent.process(data)
    
    # Verify result structure
    assert "crawled_brokers" in result
    assert "total_crawled" in result
    assert "success_count" in result
    assert "failed_count" in result
    
    # Verify crawling worked
    assert result["total_crawled"] == 1
    assert result["success_count"] >= 0  # Could be 0 or 1 depending on network
    assert result["failed_count"] >= 0  # Could be 0 or 1 depending on network
    
    # Verify crawled data was added
    crawled_broker = result["crawled_brokers"][0]
    assert "last_crawled" in crawled_broker
    assert "crawled_status" in crawled_broker

@pytest.mark.asyncio
async def test_monitoring_agent_processing():
    """Test that monitoring agent can process data."""
    from broker.agents import MonitoringAgent
    
    agent = MonitoringAgent("test_monitoring")
    
    data = {
        "brokers": [
            {"name": "Test Broker", "url": "https://test-broker.com"}
        ]
    }
    
    result = await agent.process(data)
    
    # Verify result structure
    assert "monitored_brokers" in result
    assert "total_monitored" in result
    assert "unchanged_count" in result
    assert "changed_count" in result
    assert "error_count" in result
    
    # Verify monitoring worked
    assert result["total_monitored"] == 1
    assert result["unchanged_count"] == 1
    assert result["changed_count"] == 0
    assert result["error_count"] == 0
    
    # Verify monitoring data was added
    monitored_broker = result["monitored_brokers"][0]
    assert "last_monitored" in monitored_broker
    assert "monitoring_status" in monitored_broker
    assert "monitoring_message" in monitored_broker

@pytest.mark.asyncio
async def test_classification_agent_processing():
    """Test that classification agent can process data."""
    from broker.agents import ClassificationAgent
    
    agent = ClassificationAgent("test_classification")
    
    data = {
        "brokers": [
            {"name": "People Search Broker", "url": "https://people-search.com", "description": "Searching for people"},
            {"name": "Marketing Data Broker", "url": "https://marketing-data.com", "description": "Marketing services"}
        ]
    }
    
    result = await agent.process(data)
    
    # Verify result structure
    assert "classified_brokers" in result
    assert "total_classified" in result
    assert "categories_used" in result
    
    # Verify classification worked
    assert result["total_classified"] == 2
    
    # Verify categories were assigned
    categories = [broker["category"] for broker in result["classified_brokers"]]
    assert "People search websites" in categories
    assert "Marketing data brokers" in categories
    
    # Verify at least one broker has regulations
    regulations_found = any(broker.get("regulations") for broker in result["classified_brokers"])
    assert regulations_found is True

@pytest.mark.asyncio
async def test_coordination_agent_processing():
    """Test that coordination agent can process data."""
    from broker.agents import CoordinationAgent
    
    agent = CoordinationAgent("test_coordination")
    
    # Simple workflow test
    data = {
        "workflow": [
            {
                "name": "discovery",
                "data": {
                    "keywords": ["test"],
                    "max_results": 2
                }
            }
        ]
    }
    
    result = await agent.process(data)
    
    # Verify result structure
    assert "workflow_results" in result
    assert "completed_steps" in result
    assert "total_steps" in result
    assert "coordination_timestamp" in result
    
    # Verify coordination worked
    assert "discovery" in result["workflow_results"]
    assert "discovery" in result["completed_steps"]
    assert result["total_steps"] == 1