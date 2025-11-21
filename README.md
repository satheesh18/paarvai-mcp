# Paarvai MCP Server

MCP server for querying AWS infrastructure through Paarvai.

## Setup

Get your API key from [paarvai.app](https://paarvai.app):

1. Sign up and connect your AWS account
2. Generate an API key from the dashboard

## Configuration

Add to your MCP client configuration:

```json
{
  "mcpServers": {
    "paarvai": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/yourusername/paarvai-mcp-server", "paarvai-mcp"],
      "env": {
        "PAARVAI_API_KEY": "your-api-key-here"
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
