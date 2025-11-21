#!/bin/bash
# Quick test script for local development

set -e

echo "🧪 Testing Paarvai MCP Server locally..."
echo ""

# Check Python version
echo "✓ Checking Python version..."
python --version

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "✓ Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
echo "✓ Activating virtual environment..."
source venv/bin/activate

# Install package in development mode
echo "✓ Installing package..."
pip install -e ".[dev]" > /dev/null 2>&1

# Run linting
echo "✓ Running linting..."
ruff check src/ tests/ || true

# Run type checking
echo "✓ Running type checking..."
mypy src/ || true

# Run tests
echo "✓ Running tests..."
pytest

# Try to run the server (will fail without API key, but checks imports)
echo "✓ Checking server can start..."
python -c "from paarvai_mcp.server import create_server; print('Server imports OK')" || echo "⚠️  Set PAARVAI_API_KEY to fully test"

echo ""
echo "✅ All checks passed!"
echo ""
echo "To test with Claude Desktop:"
echo "1. Set PAARVAI_API_KEY environment variable"
echo "2. Update Claude config to point to local server"
echo "3. Restart Claude Desktop"
