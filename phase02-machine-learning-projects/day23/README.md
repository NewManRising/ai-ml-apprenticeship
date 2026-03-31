The prior models ran on previous days did so with an imbalanced dataset (700/300).

Day 22 moved onto GridSearchCV and the F1 score improved a tiny bit. This was expected because the class distribution. 

The models have been performing poorly and that is because the models are not getting enough signal for the minority class (class 1).

For day 23, I ran the exact same set up as day 22 but I added class weights (class_weight="balanced") for the Random Forest classifier. 

I used the same parameter search grid as before. 

Here are the results:

```
** Grid Search Results **

Best Parameters: {'bootstrap': True, 'criterion': 'gini', 'max_depth': None, 'min_samples_leaf': 5, 'min_samples_split': 2, 'n_estimators': 300}
Best F1 Score: 0.5848489134582818
Best Estimator: RandomForestClassifier(class_weight='balanced', min_samples_leaf=5,
                       n_estimators=300, random_state=42)

```

Here are the results from before without class_weight:

```
** Grid Search Results **

Best Parameters: {'bootstrap': True, 'criterion': 'entropy', 'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 100}
Best F1 Score: 0.46682229516093354
Best Estimator: RandomForestClassifier(criterion='entropy', min_samples_leaf=2, random_state=42)
```