## Day 32 — Model API

Built a FastAPI service to serve a trained credit risk model.

### Endpoints
- GET `/` → health check
- POST `/predict` → returns prediction + risk score

### Run
```bash
uvicorn app:app --reload