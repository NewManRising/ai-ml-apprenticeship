# Day 34 — API Hardening

## Objective
Improve the FastAPI service by adding input validation, response schemas, and safe error handling.

## What Was Built
A machine learning API that:
- Accepts structured input via FastAPI
- Validates input using Pydantic schemas
- Returns prediction and risk score
- Rejects invalid input with proper errors (422)

## Endpoints

### GET /
Health check
Returns:
```JSON
{"message": "Credit Risk Model API is running"}
```

### POST /predict

Accepts credit data and returns prediction.

Example Input:
```JSON
{
  "age": 35,
  "sex": "male",
  "job": 2,
  "housing": "own",
  "saving_accounts": "little",
  "checking_account": "moderate",
  "credit_amount": 3000,
  "duration": 12,
  "purpose": "car"
}
```
Example Output:
```JSON
{
  "prediction": "Good",
  "risk_score": 0.41
}
```