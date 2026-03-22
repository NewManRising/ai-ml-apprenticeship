1) **What model was used today?**

    A Decision Tree Classifier was trained on the encoded credit-risk dataset.

2) **How is a decision tree different from logistic regression?**

    Logistic regression uses one global linear decision boundary, while a decision tree makes a sequence of split decisions based on feature values.

3) **Why did you print both train and test accuracy?**

    To check whether the model is overfitting.
4) **Did the tree appear to overfit?**

    Yes, the tree overfit. I received an accuracy of 1.0 on training, but test accuracy was 0.75.

5) **How did it compare to the logistic regression baseline?**

    I computed the same metrics like classification report and confusion matrix for both models. 
    Upon viewing the results, the decision tree does a slightly better job than the logistic regression model.
    Test accuracy for logistic regression was 0.73, whereas it was 0.75 for the decision tree.



Classification Report for Logistic Regression:

              precision    recall  f1-score   support

           0        0.76      0.89      0.82       140
           1        0.58      0.35      0.44        60

    accuracy                            0.73       200
    macro avg       0.67      0.62      0.63       200
    weighted avg    0.71      0.73      0.71       200





Classification Report for the Decision Tree:

             precision    recall  f1-score   support

           0       0.81      0.84      0.83       140
           1       0.59      0.53      0.56        60

    accuracy                           0.75       200
    macro avg      0.70      0.69      0.69       200
    weighted avg   0.74      0.75      0.75       200


The Decision Tree seems to handle class imbalance a little better. But the classification reports overall are similar.

However, the confusion matrix from the Decision Tree predicted less False Positives with 28. Logistic Regression predicted 39 False Positives. 