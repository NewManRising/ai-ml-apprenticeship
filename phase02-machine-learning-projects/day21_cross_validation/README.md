Today's script applies cross validation to all three models I previously used for my bank loan dataset. I computed accuracy scores for logistic regression, decision tree, and random forest.

Additionally, I calculated the average mean, the standard deviation, F1 score, and average F1 score.

Here are the results:

```
LogReg Accuracy Scores: [0.745 0.695 0.775 0.74  0.725]
Decision Tree Accuracy Scores: [0.65 0.66 0.64 0.69 0.66]
Random Forest Accuracy Scores: [0.725 0.73  0.725 0.75  0.735]

LogReg F1 Scores: [0.4742268  0.35789474 0.50549451 0.45833333 0.44444444]
Decision Tree F1 Scores: [0.46969697 0.47692308 0.37931034 0.44642857 0.4516129 ]
Random Forest F1 Scores: [0.45544554 0.44897959 0.38202247 0.50980392 0.45360825]

** Cross Validation Results **

      Model  CV Accuracy Mean  CV Accuracy Std  CV F1 Mean
0   LogReg             0.736         0.026153    0.448079
1    DTree             0.660         0.016733    0.444794
2  RForest             0.733         0.009274    0.449972
```

I am still using a dataset with a class imbalance of 700/300. No hyperparameters, no fine-tuning, no class weights, no SMOTE, has been applied yet. These are just baseline values for comparison.

Based on the results, the model with the highest average CV accuracy was Logistic Regression but just barely (0.736 compared to 0.733 Random Forest). However, Random Forest had the lowest standard deviation of 0.009, suggesting it is more stable and generalizes well.

The best average F1 score was achieved by Random Forest with 0.449. At this moment I probably trust the Random Forest classifier the most. 
Although all the scores are very close, overall Random Forest has solid performance compared to the others.

In the coming days I will see if I can improve performance including hyperparameters, GridSearchCV, handling class imbalance, and other tuning. None of the models are handling the class imbalance well according to their average F1 scores. 