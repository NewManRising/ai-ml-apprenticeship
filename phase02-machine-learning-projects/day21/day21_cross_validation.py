# Imports
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

#---------------------------------------------------------------------------------------------------------------------
# Loading Data
X = pd.read_csv("X_encoded.csv")
y = pd.read_csv("y.csv").squeeze()

y = y.map({"good": 0, "bad": 1})

print("\n** Quick Data Check **\n")
print("Shape of Feature Matrix:", X.shape)
print("Shape of Labels:", y.shape)

#---------------------------------------------------------------------------------------------------------------------
# Defining Models
log_reg = LogisticRegression(max_iter=5000, random_state=42)
tree = DecisionTreeClassifier(random_state=42)
forest = RandomForestClassifier(random_state=42)

# Cross Validation Accuracy Scores
log_score = cross_val_score(log_reg, X, y, cv=5, scoring="accuracy")
tree_score = cross_val_score(tree, X, y, cv=5, scoring="accuracy")
forest_score = cross_val_score(forest, X, y, cv=5, scoring="accuracy")

# Average Accuracy Score
log_avg = log_score.mean()
tree_avg = tree_score.mean()
forest_avg = forest_score.mean()

# Standard Deviations
log_std = log_score.std()
tree_std = tree_score.std()
forest_std = forest_score.std()


# F1 Scores
log_f1 = cross_val_score(log_reg, X, y, cv=5, scoring="f1")
tree_f1 = cross_val_score(tree, X, y, cv=5, scoring="f1")
forest_f1 = cross_val_score(forest, X, y, cv=5, scoring="f1")

# Avg F1 Scores
avg_log_f1 = log_f1.mean()
avg_tree_f1 = tree_f1.mean()
avg_forest_f1 = forest_f1.mean()

#---------------------------------------------------------------------------------------------------------------------
# Results

results = {
    "Model": ["LogReg", "DTree", "RForest"],
    "Avg_scores": [log_avg, tree_avg, forest_avg],
    "Std_scores": [log_std, tree_std, forest_std],
    "Avg_F1_scores": [avg_log_f1, avg_tree_f1, avg_forest_f1]
}

df = pd.DataFrame(results)
df.to_csv("cv_results.csv", index=False)
scores_report = df.to_string()
print("\n** Report Of All Model Scores **\n\n", scores_report)
