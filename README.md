# Paarvai MCP Server

[![PyPI version](https://badge.fury.io/py/paarvai-mcp-server.svg)](https://badge.fury.io/py/paarvai-mcp-server)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

AWS infrastructure knowledge graph for Claude and other MCP clients. Query your cloud infrastructure using natural language, discover hidden relationships, and get security insights.

## ✨ Features

- 🔍 **Natural Language Queries** - Ask questions about your AWS infrastructure in plain English
- 🕸️ **Relationship Discovery** - Automatically infer connections between resources
- 🔒 **Security Analysis** - Identify overly permissive IAM roles and security group rules
- 📊 **Infrastructure Insights** - Find unused resources, cost optimization opportunities
- ⚡ **Fast Graph Queries** - Powered by Neo4j knowledge graph for complex multi-hop queries
- 🎯 **Multi-Account Support** - Query across multiple AWS accounts (Pro/Enterprise)

## 🚀 Quick Start

### Installation

Using `uvx` (recommended):
```bash
uvx paarvai-mcp-server
```

Using `pip`:
```bash
pip install paarvai-mcp-server
```

### Configuration

Add to your Claude Desktop config file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "paarvai": {
      "command": "uvx",
      "args": ["paarvai-mcp-server"],
      "env": {
        "PAARVAI_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

### Get Your API Key

1. Sign up at [paarvai.com](https://paarvai.com)
2. Connect your AWS account
3. Copy your API key from the dashboard
4. Add it to your Claude config

## 💡 Example Queries

Once configured, you can ask Claude questions like:

### Resource Discovery (Tier 1)
```
"List all EC2 instances in us-west-1"
"Show me all resources tagged with Environment=production"
"Search for resources with 'database' in the name"
"What types of resources do I have?"
```

### Resource Details (Tier 2)
```
"Get details for arn:aws:ec2:us-west-1:123456789012:instance/i-1234567890abcdef0"
"Show me the tags for this RDS instance"
"What's the configuration of this security group?"
```

### Relationships (Tier 3)
```
"What resources depend on this EC2 instance?"
"Show me the path from this Lambda to that RDS database"
"What security groups is this EC2 instance using?"
"Find all resources connected to this VPC"
```

### Analysis (Tier 4)
```
"What would be impacted if I delete this security group?"
"Analyze the security posture of this EC2 instance"
"Show me the blast radius of this RDS database"
```

### Summary & Ownership (Tier 5-6)
```
"Give me an overview of all my AWS resources"
"Who owns this EC2 instance?"
"Show me resource counts by type and region"
```

## 🛠️ Available Tools (13 Tools in 6 Tiers)

### Tier 1: Resource Discovery
- `list_resources` - Find resources by type, region, or tags
- `search_resources` - Fuzzy search across names, tags, and ARNs
- `get_resource_types` - See what resource types exist with counts

### Tier 2: Resource Details
- `get_resource` - Get complete details for a specific resource
- `get_resource_tags` - Get tags for a resource

### Tier 3: Relationships
- `get_dependencies` - Find connected resources (upstream/downstream)
- `get_relationship_path` - Find connection path between two resources
- `get_connected_by_type` - Find connected resources of a specific type

### Tier 4: Analysis
- `analyze_blast_radius` - Analyze impact of changes/deletions
- `analyze_security` - Security posture analysis

### Tier 5: Aggregation & Summary
- `get_account_summary` - High-level overview of all resources

### Tier 6: Ownership
- `get_resource_owner` - Get ownership information from tags

## 📖 Documentation

- [Full Documentation](https://docs.paarvai.com)
- [API Reference](https://docs.paarvai.com/api)
- [Example Queries](https://docs.paarvai.com/examples)
- [Troubleshooting](https://docs.paarvai.com/troubleshooting)

## 🔧 Advanced Configuration

### Custom API Endpoint

```json
{
  "mcpServers": {
    "paarvai": {
      "command": "uvx",
      "args": ["paarvai-mcp-server"],
      "env": {
        "PAARVAI_API_KEY": "your-api-key",
        "PAARVAI_API_URL": "https://api.paarvai.com",
        "PAARVAI_TIMEOUT": "30"
      }
    }
  }
}
```

### Environment Variables

- `PAARVAI_API_KEY` (required) - Your Paarvai API key
- `PAARVAI_API_URL` (optional) - API endpoint (default: https://api.paarvai.com)
- `PAARVAI_TIMEOUT` (optional) - Request timeout in seconds (default: 30)
- `PAARVAI_LOG_LEVEL` (optional) - Logging level: DEBUG, INFO, WARNING, ERROR (default: INFO)

## 🏗️ Architecture

```
┌─────────────┐         ┌──────────────────┐         ┌─────────────────┐
│   Claude    │ ◄─MCP──►│  Paarvai MCP     │ ◄─API──►│  Paarvai Cloud  │
│   Desktop   │         │  Server (Local)  │         │  (Knowledge     │
└─────────────┘         └──────────────────┘         │   Graph)        │
                                                      └─────────────────┘
```

The MCP server runs locally on your machine and communicates with Paarvai's cloud infrastructure where your AWS data is stored in a knowledge graph.

## 🔐 Security & Privacy

- **Read-Only Access**: Paarvai only requires read-only AWS permissions
- **Secure Storage**: Your AWS credentials are never stored by Paarvai
- **Encrypted Transit**: All API communication uses HTTPS/TLS
- **API Key Authentication**: Secure API key-based authentication
- **No Data Sharing**: Your infrastructure data is private and never shared

## 📊 Pricing

- **Free Tier**: 1,000 queries/month, 1 AWS account
- **Pro**: $49/month - 10,000 queries/month, 5 AWS accounts
- **Enterprise**: Custom pricing - Unlimited queries, unlimited accounts, on-premise option

See [paarvai.com/pricing](https://paarvai.com/pricing) for details.

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Issues & Support

- **Bug Reports**: [GitHub Issues](https://github.com/paarvai/mcp-server/issues)
- **Feature Requests**: [GitHub Discussions](https://github.com/paarvai/mcp-server/discussions)
- **Email Support**: support@paarvai.com
- **Documentation**: [docs.paarvai.com](https://docs.paarvai.com)

## 🌟 Acknowledgments

Built with:
- [Model Context Protocol](https://modelcontextprotocol.io/) by Anthropic
- [Claude](https://claude.ai/) by Anthropic
- [Neo4j](https://neo4j.com/) for graph database

---

Made with ❤️ by the Paarvai team
