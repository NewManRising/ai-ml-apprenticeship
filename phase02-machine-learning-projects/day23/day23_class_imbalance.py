# Imports
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
#--------------------------------------------------------------------------------------------------------------------
# Loading Data
X = pd.read_csv("X_encoded.csv")
y = pd.read_csv("y.csv").squeeze()

y = y.map({"good": 0, "bad": 1})

print("Shape of Feature Matrix: ", X.shape)
print("Shape of Labels: ", y.shape)
print("Target Distribution:\n", y.value_counts())
#--------------------------------------------------------------------------------------------------------------------
# Defining Model
forest = RandomForestClassifier(random_state=42, class_weight="balanced")

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
GS = GridSearchCV(estimator=forest, param_grid=params, scoring=["f1", "accuracy"], cv=5, refit='f1')
GS.fit(X, y)

#--------------------------------------------------------------------------------------------------------------------
# Results
print("\n** Grid Search Results **\n")
print('Best Parameters:', GS.best_params_)
print('Best F1 Score:', GS.best_score_)
print('Best Estimator:', GS.best_estimator_)
