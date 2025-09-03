FastAPI backend for gesture-ai

This folder contains a minimal FastAPI app, database models, event ingestion APIs, and integration points for Kafka, Redis, Celery, and MinIO.

Local dev quickstart
1. Create a virtualenv and install requirements from `requirements.txt`.
2. Configure environment variables (see `.env.example`).
3. Run `uvicorn app.main:app --reload --port 8000`.

This is a scaffold; replace Kafka/Timescale connection strings for production.
