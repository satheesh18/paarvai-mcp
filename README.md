# Paarvai MCP Server

MCP server for querying AWS infrastructure through Paarvai.

## Setup

1. Get your API key from [paarvai.app](https://paarvai.app)

2. Set environment variable:
```bash
export PAARVAI_API_KEY="your-api-key-here"
```

3. Add to your MCP client configuration:
```json
{
  "mcpServers": {
    "paarvai": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/satheesh18/paarvai-mcp-server", "paarvai-mcp-server"],
      "env": {
        "PAARVAI_API_KEY": "${PAARVAI_API_KEY}",
        "PAARVAI_API_URL": "https://api.paarvai.app"
      }
    }
  }
}
```

Works with Claude Desktop, Cline, and any other MCP-compatible client.

## Usage

Ask your AI assistant questions about your AWS infrastructure:

- "Show me all EC2 instances in us-west-1"
- "What S3 buckets are publicly accessible?"
- "Find all resources tagged with environment=production"
- "What would be affected if I delete this Lambda function?"

## License

MIT
