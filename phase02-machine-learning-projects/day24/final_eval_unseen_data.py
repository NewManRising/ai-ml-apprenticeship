# Imports
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
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
# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)


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
GS = GridSearchCV(estimator=forest, param_grid=params, scoring="f1", cv=5)

# Running GridSearch CV on Training Data Only
GS.fit(X_train, y_train)

#--------------------------------------------------------------------------------------------------------------------
# Results
print("\n** Grid Search Results **\n")
print('Best Parameters:', GS.best_params_)
print('Best F1 Score:', GS.best_score_)
print('Best Estimator:', GS.best_estimator_)

#--------------------------------------------------------------------------------------------------------------------
# Prediction and Evaluation
y_pred = GS.best_estimator_.predict(X_test)

cr = classification_report(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)
print("** Final Results **\n")
print('Accuracy:', acc)
print('Classification Report:', cr)
print('Confusion Matrix:', cm)
