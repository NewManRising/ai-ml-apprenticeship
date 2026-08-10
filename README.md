# AI / Machine Learning Apprenticeship

This repository documents a structured, hands-on build out of applied machine learning and AI systems.

The focus is simple: take raw data, turn it into usable features, build models, and ship working solutions. Everything here is organized into phases from data handling and modeling to deployment and iteration.

---

## What This Work Covers

This repository is not a collection of isolated notebooks. It is a continuous body of work centered around:

* Data preparation and transformation
* Feature engineering and encoding strategies
* Supervised and unsupervised modeling
* Model evaluation and iteration
* Applied NLP and generative AI workflows
* End-to-end project builds

Each phase builds on the previous one, with an emphasis on producing clean, reproducible, and usable outputs.

---

## Repository Structure

```text
ai-ml-apprenticeship/
│
├── phase01-python-data-foundations/
├── phase02-machine-learning-projects/
├── phase03-product-builds/
├── phase04-ai-systems-and-llms/
├── phase05-production-and-deployment/
│
├── projects/
│
└── README.md
```

## Phases Overview

- **Phase 01** — Core Python, data handling, data structures, and foundational workflows  

- **Phase 02** — Classical machine learning, model building, evaluation, and ML pipelines  

- **Phase 03** — Job-ready full-stack product builds (APIs, external integrations, data processing, UI, real-world tools)  

- **Phase 04** — AI systems and LLMs (prompting, embeddings, RAG, agents, applied AI pipelines with standalone learning + projects)  

- **Phase 05** — Production systems (deployment, databases, authentication, scaling, monitoring, and real-world application delivery)  

- **projects/** — Clean, polished portfolio versions of completed systems 
---

## Approach

The approach here is execution-focused:

* Build directly on real datasets
* Keep pipelines simple and inspectable
* Avoid unnecessary abstraction early
* Prioritize clarity over cleverness
* Iterate quickly and refine

The goal is not theory for its own sake, but systems that work and can be extended.

---

## Current Work

Active work is centered on:

* Structured tabular datasets (classification and prediction tasks)
* Feature preparation and encoding workflows
* Baseline modeling and evaluation
* Expanding into NLP and LLM-based applications

---

## Why This Exists

Most projects stop at “it runs.” This does not.

The intent here is to:

* Build systems that are understandable end-to-end
* Maintain clean, readable code and structure
* Create a body of work that can be extended into production tools
* Treat each phase as part of a larger system, not a one-off exercise

---

## Notes

* Code is organized by phase and day for traceability
* Outputs are reproducible and tied to specific datasets
* Work is iterative. Earlier phases may be revisited and improved

---

## Ongoing Direction

This repository will continue evolving toward:

* End-to-end AI applications
* API-driven tools and services
* RAG systems and domain-specific assistants
* Production-ready deployments

---
## Resources Used
### Python

1) Corey Schafer - Python Tutorial Playlist:
   https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

### Data Processing
1) Pandas Official Docs - 
   
   Get_dummies:
   https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html
    
   Value_counts:
    https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html
   
   Missing Data:
    https://pandas.pydata.org/docs/user_guide/missing_data.html?

2) Numpy Official Docs - https://numpy.org/doc/stable/

### Machine Learning

1) Scikit-Learn Official Docs - 
   
   Logistic Regression:
    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
   
   Class Weight:
    https://scikit-learn.org/stable/modules/generated/sklearn.utils.class_weight.compute_class_weight.html
  
   GridSearchCV:
    https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html
   
   Multimetric Scoring:
    https://scikit-learn.org/stable/modules/model_evaluation.html#multimetric-scoring
   
   Multimetric Cross_validation
    https://scikit-learn.org/stable/modules/cross_validation.html#multimetric-cross-validation
   
   Label Encoding
    https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html
   
   One-Hot Encoding
   https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html

   Decision Tree Classifier
   https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html

   Decision Trees
   https://scikit-learn.org/stable/modules/tree.html

   ROC AUC Score
   https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html

   Feature Importances With A Forest Of Trees
   https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html

   String Name Scorers
   https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-string-names

   Cross Validation
   https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation

   Cross Val Score
   https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html


### Visualization
1) Matplotlib Official Docs - 
   https://matplotlib.org/
2) Seaborn Official Docs - 
   https://seaborn.pydata.org/

### FastAPI
1) FastAPI Official Docs: https://fastapi.tiangolo.com/
2) OneUpTime (File Downloads): https://oneuptime.com/blog/post/2026-02-03-fastapi-file-downloads/view
3) Dev Community (Streaming Response): https://dev.to/ashraful/fastapi-streaming-response-39c5
4) Code with Josh - FastAPI Crash Course 2025: https://youtu.be/nWWPlEO0he8?si=HzG-J-gzhbsil_pR
5) pixegami - FastAPI for AI: https://youtu.be/uDUfZyNXFX0?si=x0o7e4lx6aU6h1vp


### Pydantic
1) Pydantic Official Docs - https://pydantic.dev/docs/

### Render
1) Render Official Docs - https://render.com/docs/web-services
### Streamlit
1) pixegami - Streamlit: The Fastest Way To Build Python Apps? https://www.youtube.com/watch?v=D0D4Pa22iG0&t=1s
2) Streamlit Official Docs - Getting Started:

    https://docs.streamlit.io/get-started/fundamentals/main-concepts

   API Reference: 
   https://docs.streamlit.io/develop/api-reference
3) Code with Josh - Streamlit Tutorial: Build Python Apps in less than a day: https://www.youtube.com/watch?v=8W8NQFFbDcU
4) freeCodeCamp.org - Build 12 Data Science Apps with Python and Streamlit - Full Course: https://www.youtube.com/watch?v=JwSS70SZdyM



### Google Places API
1) Overview - https://developers.google.com/maps/documentation/places/web-service/overview

   Place ID - https://developers.google.com/maps/documentation/places/web-service/place-id

   Text Search - https://developers.google.com/maps/documentation/places/web-service/text-search

   Place Details - https://developers.google.com/maps/documentation/places/web-service/place-details

   Place Data Fields - https://developers.google.com/maps/documentation/places/web-service/data-fields

   Field Mask - https://developers.google.com/maps/documentation/places/web-service/choose-fields

### Web Scraping
1. Beautiful Soup - 
   
   Quick start: https://beautiful-soup-4.readthedocs.io/en/latest/#quick-start
 
   decompose(): https://beautiful-soup-4.readthedocs.io/en/latest/#decompose

   get_text(): https://beautiful-soup-4.readthedocs.io/en/latest/#get-

   find(): https://beautiful-soup-4.readthedocs.io/en/latest/#find

   Response Content: https://requests.readthedocs.io/en/latest/user/quickstart/#response-content

   Errors and Exceptions: https://requests.readthedocs.io/en/latest/user/quickstart/#errors-and-exceptions

2. freeCodeCamp - Beautiful Soup Tutorial - Web Scraping in Python: https://www.youtube.com/watch?v=87Gx3U0BDlo


### OpenAI API
1. Quickstart: https://developers.openai.com/api/docs/quickstart
2. Models: https://developers.openai.com/api/docs/models/all
3. Responses Overview: https://developers.openai.com/api/reference/responses/overview


### Requests
1. Requests (Python Library): https://requests.readthedocs.io/en/latest/
  
   Response Status Codes: https://requests.readthedocs.io/en/latest/user/quickstart/#response-status-codes

3. Wikipedia - List of HTTP Status Codes: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

   List of HTTP Header Fields: https://en.wikipedia.org/wiki/List_of_HTTP_header_fields




---
If you're reviewing this repository, start with the latest phase for the most current work, then move backward for context.
