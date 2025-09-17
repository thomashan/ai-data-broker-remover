import pytest
from pathlib import Path

def test_agent_modules_exist():
    """Test that agent modules exist."""
    agent_dir = Path("app/brokers/src/broker/agents")
    assert agent_dir.exists(), f"Agent directory not found at {agent_dir}"

def test_discovery_agent_exists():
    """Test that discovery agent module exists."""
    discovery_agent = Path("app/brokers/src/broker/agents/discovery.py")
    assert discovery_agent.exists(), f"Discovery agent module not found at {discovery_agent}"

def test_deduplication_agent_exists():
    """Test that deduplication agent module exists."""
    dedup_agent = Path("app/brokers/src/broker/agents/deduplication.py")
    assert dedup_agent.exists(), f"Deduplication agent module not found at {dedup_agent}"

def test_crawling_agent_exists():
    """Test that crawling agent module exists."""
    crawling_agent = Path("app/brokers/src/broker/agents/crawling.py")
    assert crawling_agent.exists(), f"Crawling agent module not found at {crawling_agent}"

def test_monitoring_agent_exists():
    """Test that monitoring agent module exists."""
    monitoring_agent = Path("app/brokers/src/broker/agents/monitoring.py")
    assert monitoring_agent.exists(), f"Monitoring agent module not found at {monitoring_agent}"

def test_classification_agent_exists():
    """Test that classification agent module exists."""
    classification_agent = Path("app/brokers/src/broker/agents/classification.py")
    assert classification_agent.exists(), f"Classification agent module not found at {classification_agent}"

def test_coordination_agent_exists():
    """Test that coordination agent module exists."""
    coordination_agent = Path("app/brokers/src/broker/agents/coordination.py")
    assert coordination_agent.exists(), f"Coordination agent module not found at {coordination_agent}"

def test_agent_base_class_exists():
    """Test that agent base class exists."""
    base_agent = Path("app/brokers/src/broker/agents/base.py")
    assert base_agent.exists(), f"Base agent module not found at {base_agent}"