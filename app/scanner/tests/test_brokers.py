"""Tests for data broker implementations."""

import pytest
from app.scanner.src import PersonalInfo, RemovalStatus
from app.scanner.src import WhitePages, Spokeo, PeopleFinder


@pytest.fixture
def personal_info():
    """Create test personal information."""
    return PersonalInfo(
        first_name="Test",
        last_name="User",
        email="test.user@example.com",
        phone="(555) 123-4567",
        address="123 Test St",
        city="Test City",
        state="TS",
        zip_code="12345"
    )


class TestWhitePages:
    """Test WhitePages broker implementation."""
    
    def test_initialization(self):
        """Test broker initialization."""
        broker = WhitePages()
        assert broker.name == "WhitePages"
        assert broker.url == "https://www.whitepages.com"
    
    def test_required_fields(self):
        """Test required fields."""
        broker = WhitePages()
        required = broker.get_required_fields()
        assert "first_name" in required
        assert "last_name" in required
        assert "email" in required
    
    def test_validate_personal_info(self, personal_info):
        """Test personal info validation."""
        broker = WhitePages()
        assert broker.validate_personal_info(personal_info) is True
        
        # Test with missing required field
        incomplete_info = PersonalInfo(
            first_name="Test",
            last_name="User",
            email=""  # Missing required email
        )
        assert broker.validate_personal_info(incomplete_info) is False
    
    @pytest.mark.asyncio
    async def test_search_records(self, personal_info):
        """Test searching for records."""
        broker = WhitePages()
        records = await broker.search_records(personal_info)
        assert isinstance(records, list)
        assert len(records) > 0
    
    @pytest.mark.asyncio
    async def test_submit_removal_request(self, personal_info):
        """Test submitting removal request."""
        broker = WhitePages()
        request = await broker.submit_removal_request(personal_info)
        
        assert request.broker_name == "WhitePages"
        assert request.personal_info == personal_info
        assert request.status == RemovalStatus.IN_PROGRESS
        assert request.request_id is not None


class TestSpokeo:
    """Test Spokeo broker implementation."""
    
    def test_initialization(self):
        """Test broker initialization."""
        broker = Spokeo()
        assert broker.name == "Spokeo"
        assert broker.url == "https://www.spokeo.com"
    
    @pytest.mark.asyncio
    async def test_submit_removal_request(self, personal_info):
        """Test submitting removal request."""
        broker = Spokeo()
        request = await broker.submit_removal_request(personal_info)
        
        assert request.broker_name == "Spokeo"
        assert request.status == RemovalStatus.PENDING  # Spokeo starts as pending


class TestPeopleFinder:
    """Test PeopleFinder broker implementation."""
    
    def test_initialization(self):
        """Test broker initialization."""
        broker = PeopleFinder()
        assert broker.name == "PeopleFinder"
        assert broker.url == "https://www.peoplefinder.com"
    
    def test_required_fields(self):
        """Test required fields."""
        broker = PeopleFinder()
        required = broker.get_required_fields()
        assert "first_name" in required
        assert "last_name" in required
        assert "city" in required
        assert "state" in required
