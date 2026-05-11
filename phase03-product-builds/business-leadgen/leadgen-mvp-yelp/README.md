## Current Status
The leadgen MVP is done. It is deployed.

I made a tiny edit to the frontend streamlit code. I swapped out the request from the local backend URL and put in the Render backend URL so the frontend can communicate when deployed.

So it basically went from "http://127.0.0.1:8000/leads" to " https://yelp-lead-gen.onrender.com/leads"

Frontend Url: https://leadgen-mvp-yelp.onrender.com

Backend Url:  https://yelp-lead-gen.onrender.com/docs

Getting both services on Render required 



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