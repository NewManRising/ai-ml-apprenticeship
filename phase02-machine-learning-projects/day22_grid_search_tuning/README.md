GridSearchCV was used to tune Random Forest hyperparameters using 5-fold cross-validation. The goal was to check to see if tuning with hyperparameters would have a meaningful effect on the model results. F1 score was used because of class imbalance. 

Here are the results:
```
** Grid Search Results **

Best Parameters: {'bootstrap': True, 'criterion': 'entropy', 'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 100}
Best F1 Score: 0.46682229516093354
Best Estimator: RandomForestClassifier(criterion='entropy', min_samples_leaf=2, random_state=42)
```

The F1 score improved slightly. Before GridSearchCV it was 0.449, with GridsearchCV it's 0.467.

The best parameters for Random Forest are: ``` RandomForestClassifier(criterion='entropy', min_samples_leaf=2, random_state=42)```

It seems the model benefits from deeper trees with minor regularization. The F1 score remains low but this is due to dataset imbalance (700/300). The dataset is the limiting factor and that will be handled next.