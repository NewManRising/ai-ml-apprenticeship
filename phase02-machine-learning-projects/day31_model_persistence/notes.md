# Day 31 — Model Persistence

## Objective
Save trained model and reuse it for predictions

## Steps
- Trained model using pipeline
- Saved with joblib
- Reloaded model
- Ran predictions on new data

## Key Insight
Saving the full pipeline ensures preprocessing and model remain consistent. The model is now reusable, portable, and deployable. 