# Contributing to Paarvai MCP Server

Thank you for your interest in contributing to Paarvai MCP Server! This document provides guidelines for contributing to the project.

## Code of Conduct

Be respectful, inclusive, and professional in all interactions.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/paarvai/mcp-server/issues)
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version, etc.)
   - Relevant logs or error messages

### Suggesting Features

1. Check [Discussions](https://github.com/paarvai/mcp-server/discussions) for similar ideas
2. Create a new discussion with:
   - Clear use case
   - Proposed solution
   - Why it would be valuable

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linting
5. Commit with clear messages
6. Push to your fork
7. Open a Pull Request

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/mcp-server.git
cd mcp-server

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run linting
black src/ tests/
ruff check src/ tests/
mypy src/
```

## Code Style

- Follow PEP 8
- Use Black for formatting (line length: 100)
- Use type hints
- Write docstrings for public functions
- Keep functions focused and small

## Testing

- Write tests for new features
- Maintain test coverage above 80%
- Use pytest for testing
- Mock external API calls

## Commit Messages

Follow conventional commits:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `test:` Test changes
- `refactor:` Code refactoring
- `chore:` Maintenance tasks

Example: `feat: add support for ECS resource queries`

## Questions?

- Open a [Discussion](https://github.com/paarvai/mcp-server/discussions)
- Email: support@paarvai.com

Thank you for contributing! 🎉
