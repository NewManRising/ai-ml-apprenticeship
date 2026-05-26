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