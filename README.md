# gesture-ai

AI-Powered CCTV Safety Analytics System for Schools — scaffold and MVP

This repository contains a production-oriented scaffold for an AI CCTV safety monitoring system focused on privacy, explainability, and human-in-the-loop review.

Folders created by the scaffold:
- `backend/` — FastAPI backend, Kafka/Redis hooks, Celery tasks, MinIO integration
- `ai/` — Model adaptor stubs (YOLOv8, DeepSORT, MediaPipe) and event recognition pipeline
- `frontend/` — React + Tailwind dashboard skeleton (live feeds, timeline, review queue)
- `db/` — TimescaleDB migration SQL
- `k8s/` — Kubernetes deployment manifests
- `helm/` — Helm chart skeleton
- `.github/` — CI/CD pipelines

This scaffold implements the core contracts and provides modular, documented stubs to be extended for your environment (Jetson/RTX/servers).

Quick start (developer/dev machine, minimal):

1) Services required for local dev: Kafka, Zookeeper, MinIO, TimescaleDB/Postgres. You can use Docker images. A `docker-compose.yml` is included as a starting point.
2) Build backend image and run in dev mode (inside the workspace): see `backend/README.md` for details.
3) Build frontend and run dev server: see `frontend/README.md`.

See the files under `/backend`, `/ai`, `/frontend` for API contracts, event schema, and sample implementations.

Next steps: customize model weights, point RTSP feeds at the `ai/` runner, and configure credentials for Kafka/MinIO/TimescaleDB.