## Day 35 — Project Polish

Improved API structure and production readiness. Tested all end points and everything works fine. The model is now live and hosted on Render.

### Improvements
- Config management using environment variables
- Logging for tracking predictions and errors
- Health check endpoint
- Reproducible environment with requirements.txt

### Run

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```
### Endpoints
```
GET / > status message
GET /health > API health
POST /predict > prediction + risk score
```

## Live API
https://ai-ml-apprenticeship.onrender.com/docs