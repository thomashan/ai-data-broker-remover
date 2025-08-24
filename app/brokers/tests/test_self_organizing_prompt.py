from pathlib import Path


def test_prompt_file_exists():
    """Test that the prompt.md file exists in the expected location."""
    prompt_path = Path("app/brokers/prompts/prompt.md")
    assert prompt_path.exists(), f"Prompt file not found at {prompt_path}"


def test_prompt_mentions_self_organizing_agents():
    """Test that the prompt mentions self-organizing agent network approach."""
    prompt_path = Path("app/brokers/prompts/prompt.md")
    content = prompt_path.read_text()

    # Check for self-organizing agent network concepts
    assert "self-organizing" in content.lower(), "Prompt should mention self-organizing approach"
    assert "network" in content.lower(), "Prompt should mention network approach"
    assert "dynamic" in content.lower(), "Prompt should mention dynamic collaboration"


def test_prompt_includes_agent_collaboration_mechanisms():
    """Test that the prompt includes mechanisms for agent collaboration."""
    prompt_path = Path("app/brokers/prompts/prompt.md")
    content = prompt_path.read_text()

    # Check for collaboration mechanisms
    assert "collaboration" in content.lower(), "Prompt should mention collaboration"
    assert "coordination" in content.lower(), "Prompt should mention coordination"
    assert "communication" in content.lower(), "Prompt should mention communication"


def test_prompt_specifies_adaptive_behavior():
    """Test that the prompt specifies adaptive behavior for agents."""
    prompt_path = Path("app/brokers/prompts/prompt.md")
    content = prompt_path.read_text()

    # Check for adaptive behavior specifications
    assert "adapt" in content.lower(), "Prompt should mention adaptive behavior"
    assert "emergent" in content.lower(), "Prompt should mention emergent behavior"
    assert "resource" in content.lower(), "Prompt should mention resource management"


def test_prompt_includes_resilience_features():
    """Test that the prompt includes resilience features."""
    prompt_path = Path("app/brokers/prompts/prompt.md")
    content = prompt_path.read_text()

    # Check for resilience features
    assert "resilience" in content.lower() or "resilient" in content.lower(), "Prompt should mention resilience"
    assert "fault" in content.lower(), "Prompt should mention fault tolerance"
    assert "failure" in content.lower(), "Prompt should mention failure handling"


def test_prompt_covers_complexity_management():
    """Test that the prompt covers complexity management."""
    prompt_path = Path("app/brokers/prompts/prompt.md")
    content = prompt_path.read_text()

    # Check for complexity management
    assert "complexity" in content.lower(), "Prompt should mention complexity management"
    assert "predictable" in content.lower() or "unpredictable" in content.lower(), "Prompt should address predictability"
    assert "testing" in content.lower() or "test" in content.lower(), "Prompt should mention testing considerations"
