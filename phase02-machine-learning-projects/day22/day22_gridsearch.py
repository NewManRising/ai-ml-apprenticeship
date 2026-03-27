# Imports
import pandas as pd

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
#---------------------------------------------------------------------------------------------------------------------
# Loading Data
X = pd.read_csv("X_encoded.csv")
y = pd.read_csv("y.csv").squeeze()

y = y.map({"good": 0, "bad": 1})

print("Shape of Feature Matrix: ", X.shape)
print("Shape of Labels: ", y.shape)
print("Target Distribution:\n", y.value_counts())
#---------------------------------------------------------------------------------------------------------------------
# Defining Model
forest = RandomForestClassifier(random_state=42)

# Parameter Grid
params = {
    'n_estimators': [100, 200, 300, 400],
    'criterion': ['gini', 'entropy'],
    'max_depth': [None, 2, 3, 5],
    'min_samples_split': [2, 3, 5],
    'min_samples_leaf': [2, 3, 5],
    'bootstrap': [True, False]
}

# Setting Up GridSearchCV
GS = GridSearchCV(forest, param_grid=params, scoring= 'f1', cv=5)

# Training GridSearchCV
GS.fit(X, y)

# Results
print("\n** Grid Search Results **\n")
print('Best Parameters:', GS.best_params_)
print('Best F1 Score:', GS.best_score_)
print('Best Estimator:', GS.best_estimator_)