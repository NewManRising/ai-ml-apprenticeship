# Day 26 — ML Pipeline

## Objective
Build a leak-free ML pipeline using ColumnTransformer and Pipeline.

## What Changed
- Removed manual encoding
- Added preprocessing inside pipeline
- Ensured no data leakage

## Key Learning
Pipelines ensure transformations are applied only to training data and reused safely on test data.

## Result
Model trained and evaluated using full pipeline.