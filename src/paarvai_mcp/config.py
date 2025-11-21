"""Configuration management for Paarvai MCP Server."""

import os
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_prefix="PAARVAI_",
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # Required settings
    api_key: str = Field(
        ...,
        description="Paarvai API key for authentication",
    )

    # Optional settings
    api_url: str = Field(
        default="https://api.paarvai.com",
        description="Paarvai API base URL",
    )

    timeout: int = Field(
        default=30,
        description="Request timeout in seconds",
        ge=1,
        le=300,
    )

    log_level: str = Field(
        default="INFO",
        description="Logging level (DEBUG, INFO, WARNING, ERROR)",
    )

    max_retries: int = Field(
        default=3,
        description="Maximum number of retry attempts for failed requests",
        ge=0,
        le=10,
    )

    @property
    def api_base_url(self) -> str:
        """Get the full API base URL."""
        return self.api_url.rstrip("/")


def get_settings() -> Settings:
    """Get application settings from environment."""
    return Settings()
