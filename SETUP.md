# Setup Guide for Paarvai MCP Server

## For Users

### Prerequisites
- Python 3.10 or higher
- Claude Desktop (or another MCP-compatible client)
- Paarvai account with API key

### Installation

1. **Install the package**:
   ```bash
   # Using uvx (recommended)
   uvx paarvai-mcp-server
   
   # Or using pip
   pip install paarvai-mcp-server
   ```

2. **Get your API key**:
   - Go to [paarvai.com](https://paarvai.com)
   - Sign up or log in
   - Navigate to Settings → API Keys
   - Create a new API key
   - Copy the key (starts with `sk_live_`)

3. **Configure Claude Desktop**:
   
   **macOS**: Edit `~/Library/Application Support/Claude/claude_desktop_config.json`
   
   **Windows**: Edit `%APPDATA%\Claude\claude_desktop_config.json`
   
   Add this configuration:
   ```json
   {
     "mcpServers": {
       "paarvai": {
         "command": "uvx",
         "args": ["paarvai-mcp-server"],
         "env": {
           "PAARVAI_API_KEY": "sk_live_your_api_key_here"
         }
       }
     }
   }
   ```

4. **Restart Claude Desktop**

5. **Test it**:
   Ask Claude: "Show me all my EC2 instances"

### Troubleshooting

**"API key not found" error**:
- Make sure you've set `PAARVAI_API_KEY` in the config
- Check that the key starts with `sk_live_`
- Verify the key is valid at paarvai.com

**"Connection refused" error**:
- Check your internet connection
- Verify the API endpoint is accessible
- Check if there's a firewall blocking the connection

**"Tool not found" error**:
- Restart Claude Desktop
- Check that the MCP server is properly configured
- Look at Claude's logs for more details

## For Developers

### Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/paarvai/mcp-server.git
   cd mcp-server
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   make dev-install
   # Or: pip install -e ".[dev]"
   ```

4. **Set up environment**:
   ```bash
   cp .env.example .env
   # Edit .env and add your API key
   ```

5. **Run tests**:
   ```bash
   make test
   ```

6. **Format code**:
   ```bash
   make format
   ```

7. **Run linting**:
   ```bash
   make lint
   ```

### Testing Locally

1. **Run the server directly**:
   ```bash
   python -m paarvai_mcp.server
   ```

2. **Test with Claude Desktop**:
   Update your config to use the local version:
   ```json
   {
     "mcpServers": {
       "paarvai": {
         "command": "python",
         "args": ["-m", "paarvai_mcp.server"],
         "cwd": "/path/to/mcp-server",
         "env": {
           "PAARVAI_API_KEY": "your_key",
           "PYTHONPATH": "/path/to/mcp-server/src"
         }
       }
     }
   }
   ```

### Building and Publishing

1. **Build the package**:
   ```bash
   make build
   ```

2. **Test on TestPyPI**:
   ```bash
   make publish-test
   ```

3. **Publish to PyPI**:
   ```bash
   make publish
   ```

### Project Structure

```
paarvai-mcp-server/
├── src/
│   └── paarvai_mcp/
│       ├── __init__.py      # Package initialization
│       ├── server.py        # Main MCP server
│       ├── client.py        # API client
│       ├── config.py        # Configuration
│       └── tools.py         # Tool definitions
├── tests/                   # Test files
├── examples/                # Example configs and queries
├── pyproject.toml          # Package configuration
├── README.md               # Main documentation
├── LICENSE                 # MIT License
├── CONTRIBUTING.md         # Contribution guidelines
├── CHANGELOG.md            # Version history
└── Makefile                # Development commands
```

### Making Changes

1. Create a feature branch
2. Make your changes
3. Add tests
4. Run `make format` and `make lint`
5. Run `make test`
6. Commit and push
7. Open a Pull Request

### Release Process

1. Update version in `src/paarvai_mcp/__init__.py`
2. Update `CHANGELOG.md`
3. Commit changes
4. Create a git tag: `git tag v0.1.0`
5. Push tag: `git push --tags`
6. Build and publish: `make publish`
7. Create GitHub release

## Support

- **Documentation**: [docs.paarvai.com](https://docs.paarvai.com)
- **Issues**: [GitHub Issues](https://github.com/paarvai/mcp-server/issues)
- **Discussions**: [GitHub Discussions](https://github.com/paarvai/mcp-server/discussions)
- **Email**: support@paarvai.com
