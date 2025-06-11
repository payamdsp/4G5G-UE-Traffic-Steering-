# Security Hardening

- All data encrypted in transit (TLS 1.2+) and at rest (S3 SSE, EBS)
- AWS IAM: least-privilege roles for EMR, S3, MLflow, Lambda
- Secrets in AWS Secrets Manager
- EMR, S3 use private subnets, security groups restrict traffic
- CloudTrail for API auditing
- Docker: minimal, non-root images, no sensitive data in image
- Input validation and sanitization on all data interfaces