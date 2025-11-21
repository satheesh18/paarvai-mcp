# Example Queries for Paarvai MCP Server

## Resource Discovery

### EC2 Instances
```
"Show me all EC2 instances"
"List EC2 instances in us-west-1"
"Find EC2 instances tagged with Environment=production"
"Show me stopped EC2 instances"
```

### RDS Databases
```
"List all RDS databases"
"Show me RDS instances larger than 100GB"
"Find RDS databases without encryption"
"Which RDS databases are publicly accessible?"
```

### Lambda Functions
```
"Show me all Lambda functions"
"Find Lambda functions that haven't been invoked in 30 days"
"List Lambda functions with more than 512MB memory"
"Which Lambda functions are in a VPC?"
```

### S3 Buckets
```
"List all S3 buckets"
"Find S3 buckets without versioning"
"Show me public S3 buckets"
"Which S3 buckets have encryption enabled?"
```

## Relationship Queries

### Network Relationships
```
"Which resources can access my RDS database db-prod-001?"
"Show me all resources in security group sg-12345"
"What subnets is this EC2 instance connected to?"
"Find all resources in VPC vpc-abc123"
```

### IAM Relationships
```
"Which resources use IAM role AppServerRole?"
"Show me all resources that this IAM role can access"
"What permissions does this Lambda function have?"
"Find all EC2 instances with admin IAM roles"
```

### Data Flow
```
"Trace the data flow from API Gateway to DynamoDB"
"Show me the complete path from this Lambda to S3"
"How does data flow from my application to the database?"
```

## Security Analysis

### Security Groups
```
"Find security groups with port 22 open to the internet"
"Show me overly permissive security groups"
"Which security groups allow all traffic?"
"Find unused security groups"
```

### IAM Security
```
"Which IAM roles have admin access?"
"Find IAM roles with overly broad permissions"
"Show me IAM roles that can access S3"
"Which roles haven't been used in 90 days?"
```

### Network Security
```
"Find resources with public IP addresses"
"Show me resources accessible from the internet"
"Which databases are publicly accessible?"
"Find resources without encryption"
```

## Cost Optimization

### Unused Resources
```
"Find unused security groups"
"Show me stopped EC2 instances"
"List unattached EBS volumes"
"Find idle load balancers"
"Which Lambda functions are never invoked?"
```

### Over-provisioned Resources
```
"Find EC2 instances with low CPU utilization"
"Show me oversized RDS instances"
"List Lambda functions with excessive memory"
```

## Compliance & Audit

### Encryption
```
"Find resources without encryption"
"Show me S3 buckets without encryption"
"Which RDS databases don't use encryption?"
"List unencrypted EBS volumes"
```

### Tagging
```
"Find resources without tags"
"Show me resources missing the Environment tag"
"Which resources don't have an Owner tag?"
```

### Best Practices
```
"Find RDS databases without backups"
"Show me S3 buckets without versioning"
"Which resources violate our tagging policy?"
"Find resources not following naming conventions"
```

## Complex Multi-hop Queries

```
"Show me all resources that can write to my production S3 bucket"
"Find the complete infrastructure stack for my web application"
"Which IAM roles can access both my database and S3 bucket?"
"Show me all resources in the data path from API to database"
"Find all resources that depend on this security group"
```

## Tips for Better Queries

1. **Be specific**: Include resource IDs, names, or tags when possible
2. **Use filters**: Specify regions, accounts, or environments
3. **Ask follow-ups**: Drill down into results with more specific questions
4. **Combine criteria**: "Find EC2 instances in production that are stopped"
5. **Use natural language**: The system understands conversational queries
