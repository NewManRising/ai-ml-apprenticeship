# Imports
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
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
GS = GridSearchCV(estimator=forest, param_grid=params, scoring="f1", cv=5, n_jobs=-1, verbose=1)

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
y_prob = GS.best_estimator_.predict_proba(X_test)[:, 1]
roc_auc = roc_auc_score(y_test, y_prob)
fpr, tpr, thresholds = roc_curve(y_test, y_prob)

print("** Final Results **\n")
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nROC AUC Score:", roc_auc)

# ROC_AUC Curve Plot
plt.figure()

plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
plt.plot([0, 1], [0, 1], linestyle='--')

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")

plt.savefig("roc_curve.png")
plt.legend()
plt.show()
#----------------------------------------------------------------------------------------------------------------------
# Threshold Tuning
thresholdss = [0.3, 0.4, 0.5, 0.6, 0.7]
results = []

for t in thresholdss:
    y_pred_tuning = (y_prob >= t).astype(int)
    report = classification_report(y_test, y_pred_tuning, output_dict=True)


    print(f"\n{'='*50}")
    print(f"Threshold: {t}")
    print(f"{'='*50}")

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred_tuning))

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred_tuning))

    # noinspection PyTypeChecker
    results.append({
        "threshold": t,
        "precision_class_1": report["1"]["precision"],
        "recall_class_1": report["1"]["recall"],
        "f1_class_1": report["1"]["f1-score"],
        "precision_class_0": report["0"]["precision"],
        "recall_class_0": report["0"]["recall"],
        "f1_class_0": report["0"]["f1-score"],
        "accuracy": report["accuracy"]
    })

results_df = pd.DataFrame(results)
results_df.to_csv("threshold_tuning.csv", index=False)
print("\nThreshold Comparison Table:")
print(results_df)