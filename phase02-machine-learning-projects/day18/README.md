1) **What model was used?**

Logistic Regression was used as a baseline classification model.

2) **Why logistic regression?**

It is simple, interpretable, and provides a strong baseline before using more complex models.

3) **What does the model predict?**

The model predicts the risk level (good vs bad credit).

4) **What metrics were used?**

Precision, recall, F1-score, and confusion matrix.

5) **Key observations:**

The model did not predict well for the "bad" class. The data was imbalanced (700 good, 300 bad). The model missed 39 bad loan predictions and predicted them as good. This is just a baseline and I will be attempting to improve these predictions.