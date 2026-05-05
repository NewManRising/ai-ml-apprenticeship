## Day 35 — Project Polish

Improved API structure and production readiness. Tested all end points and everything works fine.

The model is now live and hosted on Render.
Live link here: https://ai-ml-apprenticeship.onrender.com/docs

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


### What I Learned
I learned the workflows and best practices of machine learning. I then learned how to make a machine learning model configurable, portable, and deployable.

The FastAPI endpoints were significant as well. They are basically requests coming from a user or client where the API performs an action (or response). The FastAPI generators correspond to CRUD:

- Create = Post
- Read = Get
- Update = Put
- Delete = Delete


I hosted my local API on Render (Render.com) and after signing up and filling out the required info, the machine learning API was deployed. 

Below is the start command to give to Render when making the API go live. 
```
uvicorn app:app --host 0.0.0.0 --port $PORT
```
This command helps configure the server on Render. The API is running entirely on Render's infrastructure now where it can receive and respond to public HTTP requests.

This wraps of phase02 of the apprenticeship. Next I am moving onto product builds.