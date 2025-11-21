"""Tests for Paarvai API client."""

import pytest
from unittest.mock import AsyncMock, patch

from paarvai_mcp.client import PaarvaiClient, APIError
from paarvai_mcp.config import Settings


@pytest.fixture
def settings():
    """Create test settings."""
    return Settings(api_key="test_key", api_url="https://test.api.com")


@pytest.fixture
def client(settings):
    """Create test client."""
    return PaarvaiClient(settings)


@pytest.mark.asyncio
async def test_query_resources_success(client):
    """Test successful resource query."""
    with patch.object(client, "_request", new_callable=AsyncMock) as mock_request:
        mock_request.return_value = {"resources": []}
        
        result = await client.query_resources("test query")
        
        assert result == {"resources": []}
        mock_request.assert_called_once()


@pytest.mark.asyncio
async def test_query_resources_error(client):
    """Test resource query with API error."""
    with patch.object(client, "_request", new_callable=AsyncMock) as mock_request:
        mock_request.side_effect = APIError("API Error", status_code=500)
        
        with pytest.raises(APIError):
            await client.query_resources("test query")


@pytest.mark.asyncio
async def test_get_relationships_success(client):
    """Test successful relationship query."""
    with patch.object(client, "_request", new_callable=AsyncMock) as mock_request:
        mock_request.return_value = {"relationships": []}
        
        result = await client.get_relationships("arn:aws:ec2:us-west-1:123:instance/i-123")
        
        assert result == {"relationships": []}
        mock_request.assert_called_once()
