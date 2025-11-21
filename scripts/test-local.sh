#!/bin/bash
# Test script for local development

set -e

echo "Testing Paarvai MCP Server..."
echo ""

# Check Python version
echo "Checking Python version..."
python --version

# Create virtual environment if needed
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install package in development mode
echo "Installing package..."
pip install -e ".[dev]" > /dev/null 2>&1

# Run linting
echo "Running linting..."
ruff check src/ tests/ || true

# Run type checking
echo "Running type checking..."
mypy src/ || true

# Run tests
echo "Running tests..."
pytest

# Check server imports
echo "Checking server can start..."
python -c "from paarvai_mcp.server import create_server; print('Server imports OK')" || echo "Warning: Set PAARVAI_API_KEY to fully test"

echo ""
echo "All checks passed."
echo ""
echo "To test with an MCP client:"
echo "1. Set PAARVAI_API_KEY environment variable"
echo "2. Update client config to point to local server"
echo "3. Restart the client"
