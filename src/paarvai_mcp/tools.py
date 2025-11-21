"""MCP tool definitions for Paarvai - matches backend implementation."""

from mcp.types import Tool

# Tool definitions organized by tier (matching backend/app/api/v1/mcp.py)
TOOLS = [
    # ============================================================================
    # TIER 1: RESOURCE DISCOVERY
    # ============================================================================
    Tool(
        name="list_resources",
        description="Find resources by type, region, or tags. Use this to discover what resources exist.",
        inputSchema={
            "type": "object",
            "properties": {
                "resource_type": {
                    "type": "string",
                    "description": "Resource type to filter by (optional - omit to see all types)",
                    "enum": ["EC2", "RDS", "VPC", "Subnet", "SecurityGroup", "RouteTable", "IAMRole", "S3Bucket", "Lambda", "DynamoDBTable", "SNSTopic", "SQSQueue"]
                },
                "region": {"type": "string", "description": "AWS region"},
                "tags": {"type": "object", "description": "Tag filters"},
                "limit": {"type": "integer", "default": 100}
            }
        }
    ),
    Tool(
        name="search_resources",
        description="Fuzzy search across resource names, tags, and ARNs. Use when you don't know the exact resource.",
        inputSchema={
            "type": "object",
            "properties": {
                "query_string": {"type": "string", "description": "Search term"},
                "limit": {"type": "integer", "default": 50}
            },
            "required": ["query_string"]
        }
    ),
    Tool(
        name="get_resource_types",
        description="See what types of resources exist in the account with counts.",
        inputSchema={"type": "object", "properties": {}}
    ),
    
    # ============================================================================
    # TIER 2: RESOURCE DETAILS
    # ============================================================================
    Tool(
        name="get_resource",
        description="Get complete details for a specific resource including configuration and metadata.",
        inputSchema={
            "type": "object",
            "properties": {
                "arn": {"type": "string", "description": "AWS Resource ARN"}
            },
            "required": ["arn"]
        }
    ),
    Tool(
        name="get_resource_tags",
        description="Get tags for a specific resource.",
        inputSchema={
            "type": "object",
            "properties": {
                "arn": {"type": "string", "description": "AWS Resource ARN"}
            },
            "required": ["arn"]
        }
    ),
    
    # ============================================================================
    # TIER 3: RELATIONSHIPS
    # ============================================================================
    Tool(
        name="get_dependencies",
        description="Find resources connected to this resource. Shows what it depends on (upstream) and what depends on it (downstream).",
        inputSchema={
            "type": "object",
            "properties": {
                "arn": {"type": "string", "description": "AWS Resource ARN"},
                "direction": {
                    "type": "string",
                    "enum": ["upstream", "downstream", "both"],
                    "default": "both",
                    "description": "upstream=dependencies, downstream=dependents"
                },
                "depth": {"type": "integer", "default": 1, "description": "How many hops to traverse"}
            },
            "required": ["arn"]
        }
    ),
    Tool(
        name="get_relationship_path",
        description="Find the connection path between two resources. Useful for 'Can X reach Y?' questions.",
        inputSchema={
            "type": "object",
            "properties": {
                "source_arn": {"type": "string", "description": "Starting resource ARN"},
                "target_arn": {"type": "string", "description": "Target resource ARN"},
                "max_hops": {"type": "integer", "default": 5}
            },
            "required": ["source_arn", "target_arn"]
        }
    ),
    Tool(
        name="get_connected_by_type",
        description="Find connected resources of a specific type (e.g., 'What security groups does this EC2 use?').",
        inputSchema={
            "type": "object",
            "properties": {
                "arn": {"type": "string", "description": "AWS Resource ARN"},
                "resource_type": {"type": "string", "description": "Type of connected resources"}
            },
            "required": ["arn", "resource_type"]
        }
    ),
    
    # ============================================================================
    # TIER 4: ANALYSIS
    # ============================================================================
    Tool(
        name="analyze_blast_radius",
        description="Analyze what would be impacted if this resource is changed or deleted.",
        inputSchema={
            "type": "object",
            "properties": {
                "arn": {"type": "string", "description": "AWS Resource ARN"},
                "action": {"type": "string", "enum": ["delete", "modify", "stop"], "default": "delete"}
            },
            "required": ["arn"]
        }
    ),
    Tool(
        name="analyze_security",
        description="Analyze security posture of a resource including public exposure and security groups.",
        inputSchema={
            "type": "object",
            "properties": {
                "arn": {"type": "string", "description": "AWS Resource ARN"}
            },
            "required": ["arn"]
        }
    ),
    
    # ============================================================================
    # TIER 5: AGGREGATION & SUMMARY
    # ============================================================================
    Tool(
        name="get_account_summary",
        description="Get high-level overview of all resources (counts by type, region, etc.).",
        inputSchema={"type": "object", "properties": {}}
    ),
    
    # ============================================================================
    # TIER 6: OWNERSHIP
    # ============================================================================
    Tool(
        name="get_resource_owner",
        description="Get ownership information for a resource from tags.",
        inputSchema={
            "type": "object",
            "properties": {
                "arn": {"type": "string", "description": "AWS Resource ARN"}
            },
            "required": ["arn"]
        }
    )
]
