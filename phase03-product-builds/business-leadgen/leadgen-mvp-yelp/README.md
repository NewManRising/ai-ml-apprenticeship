## Current Status
The leadgen MVP is done. It is deployed.

I made a tiny edit to the frontend streamlit code. I swapped out the request from the local backend URL and put in the Render backend URL so the frontend can communicate when deployed.

So it basically went from "http://127.0.0.1:8000/leads" to " https://leadgen-mvp-yelp.onrender.com/leads"

Local Backend Url: http://127.0.0.1:8000

Local Frontend Url: streamlit run streamlit_app.py


Render Frontend Url: https://yelp-lead-gen.onrender.com

Render Backend Url:  https://leadgen-mvp-yelp.onrender.com/docs



## Render Deployment Setup

### Backend (FastAPI) — Render Web Service

#### Build Command

```bash
pip install -r requirements.txt
```
#### Start Command
```bash
uvicorn app:app --host 0.0.0.0 --port $PORT
```
#### Backend Environment Variables
```markdown
Render Dashboard → Backend Service → Environment

Ex: 
YELP_API_KEY=your_yelp_api_key
GOOGLE_PLACES_API_KEY=your_google_api_key
```
## Frontend (Streamlit) — Render Web Service
### Build Command
```bash
pip install -r requirements.txt
```
### Start Command
```bash
streamlit run streamlit_app.py --server.port $PORT --server.address 0.0.0.0
```
## Frontend Environment Variables
```markdown
Render Dashboard → Frontend Service → Environment

Ex:
API_BASE_URL=https://your-backend-name.onrender.com
```

LeadGen MVP v0.1 currently includes:

- FastAPI backend
- Yelp API integration
- Filtering and scoring
- Excel export
- Streamlit frontend
- Frontend ↔ backend communication

### Next Planned Features

This will continue in new versions in their own folder. The Google Places migration and other features will built at "leadgen-v02-google."

The following features is what is planned next:

- Google Places API migration
- AI enrichment layer
- Notion CRM integration
- React frontend
- Deployment