1) **What model was used today?**
The Random Forest Classifier.
2) **How is a random forest different from a single decision tree?**
Instead of a single tree making a prediction, the random forest is a panel of trees making a prediction. The random forest classifier solves overfitting and unstableness typically experienced with a single decision tree.
3) **Did the random forest seem more stable than the decision tree?**
Yes, but barely. Training accuracy was 1.0 and the test accuracy was 0.775. This is slightly more stable than the decision tree with a test accuracy of 0.75.
4) **How did it compare to logistic regression?**
It is much better than logistic regression. Test accuracy is higher, and it did better with predictions according to the metrics.
5) **Which model is strongest so far, and why?**
It would be a tie between decision tree and random forest. Random forest is a little more stable and has excellent recall for the majority (class 0). But the decision tree does a slightly better job at recall for the minority class (class 1). The random firest predicts more True Positives but a little more False Positives. 


The classification reports for all three models are below.



**Classification Report for Logistic Regression:**

              precision    recall  f1-score   support

           0        0.76      0.89      0.82       140
           1        0.58      0.35      0.44        60

    accuracy                            0.73       200
    macro avg       0.67      0.62      0.63       200
    weighted avg    0.71      0.73      0.71       200





**Classification Report for the Decision Tree:**

             precision    recall  f1-score   support

           0       0.81      0.84      0.83       140
           1       0.59      0.53      0.56        60

    accuracy                           0.75       200
    macro avg      0.70      0.69      0.69       200
    weighted avg   0.74      0.75      0.75       200


**Classification Report for Random Forest:**

               precision    recall  f1-score   support

           0       0.78      0.94      0.85       140
           1       0.73      0.40      0.52        60

    accuracy                           0.78       200
    macro avg      0.76      0.67      0.68       200
    weighted avg   0.77      0.78      0.75       200




**Analysis Of All 3 Models** 

Looking at all the confusion matrices and classifications reports
I would probably choose the decision tree. It has the least False Positives of the 3 models. Having fewer False Positives is much more meaningful with this type of classification problem.

False Positives for all three models were:



Logistic Regression = 39 

Decision Tree = 28

Random Forest = 36

Random Forest predicted the most True Positives with 131, compared to 118 for decision tree and 125 for logistic regression.