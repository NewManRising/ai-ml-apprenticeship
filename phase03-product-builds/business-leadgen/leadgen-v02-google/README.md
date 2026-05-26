## Lead Gen App — v0.2 Google Places


The v0.2 Google Lead Gen app is complete. The deployment workflow was done just the same as the lead-gen-mvp-yelp app. 

Both front and backend were deployed on Render but the URLs are kept private for now.


This version upgrades the original Yelp MVP by using Google Places API (New) as the lead discovery source.

### Completed Features

- FastAPI backend
- Google Places Text Search integration
- Google API key loaded through environment variables
- Clean normalized lead output
- Filtering by rating, review count, and operational status
- 0–100 lead scoring system
- Streamlit frontend
- Excel download
- Local testing completed
- Render deployment completed (private)



## App Preview

#### Streamlit UI
![LeadGen Dashboard](images/v02%20leadgen%20frontpage.png)

#### Excel Download
![Excel Download](images/v02%20leadgen%20download.png)

#### Clean URLs to websites 
![Excel Download](images/v02%20leadgen%20url.png)

#### FastAPI Docs

![FastAPI Docs](images/v02%20leadgen%20FastAPI%20Docs.png)

![Excel Download](images/v02%20leadgen%20search%20leads.png)







### Current Architecture

```text
Streamlit Frontend
↓
FastAPI Backend
↓
Google Places API
↓
Clean / Filter / Score
↓
Display + Excel Export
```

### Next Steps
I am going to build upon the foundation of this app and add an AI layer. 

Planned AI features:

- Website text extraction
- Company summary generation
- Product/service offering extraction
- Sales notes
- Lead qualification
- Structured LLM outputs



## How to Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/NewManRising/ai-ml-apprenticeship.git
cd ai-ml-apprenticeship/phase03-product-builds/leadgen/leadgen-v02-google
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Create a .env file
```bash
GOOGLE_PLACES_API_KEY=your_google_places_api_key
API_BASE_URL=http://127.0.0.1:8000
```
### 4. Run the FastAPI backend
```bash
Open terminal:

uvicorn app:app --reload

Backend docs:

http://127.0.0.1:8000/docs
```
### 5. Run the Streamlit frontend
```bash
Open a second terminal:

streamlit run streamlit_app.py
```
### Render Deployment Notes

This project uses two Render web services:

FastAPI Backend

Streamlit Frontend

#### Backend Service
```bash
Build command:

pip install -r requirements.txt
```
```bash
Start command:

uvicorn app:app --host 0.0.0.0 --port $PORT
```
```bash
Backend environment variable:

GOOGLE_PLACES_API_KEY=your_google_places_api_key
```
#### Frontend Service
```bash
Build command:

pip install -r requirements.txt
```
```bash
Start command:

streamlit run streamlit_app.py --server.port $PORT --server.address 0.0.0.0
```
```bash
Frontend environment variable:

API_BASE_URL=https://your-backend-service.onrender.com
```

## Important Notes
- Do not commit .env files.
- API keys should only be stored locally in .env or in Render environment variables.
- Localhost URLs only work locally; deployed frontend services must use the deployed backend URL.