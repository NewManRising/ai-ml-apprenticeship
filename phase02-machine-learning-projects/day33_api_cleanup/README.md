## Day 33 — API Input Validation

Added Pydantic schema to enforce structured input.

### Benefits
- clearer API documentation
- automatic validation
- consistent input format

### Example Input

```json
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