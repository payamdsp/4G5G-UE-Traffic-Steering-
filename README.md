# Intelligent Traffic Steering (5G NR/4G LTE ENDC) Platform

A closed-loop, scalable, ML-driven platform for 5G/4G traffic steering using Docker Compose, AWS, and OpenRAN principles.

## Features

- Real-time RAN data collection (RSRP, RSRQ, SINR, PRB, HetNet, 5QI/QCI, sNSSAI, slice params, A3/A5, PCI/ECGI/NR Cell ID, RSI, MCC/MNC dummy).
- Distributed feature engineering (Spark, EMR).
- S3 Feature Store (can be emulated locally).
- Ensemble ML (Isolation Forest + Random Forest).
- Closed-loop controller for autonomous steering.
- Security: Encryption, IAM, least-privilege, audit logs.

## Quickstart

1. Copy `.env.example` to `.env` and set your AWS keys.
2. Build and run:
   ```bash
   docker compose up --build
   ```
3. MLflow UI: http://localhost:5000

## Security

See [infrastructure/security_hardening.md](infrastructure/security_hardening.md) for mandatory practices.