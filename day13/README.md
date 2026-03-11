1) **What is cross validation?**

Cross validation is a model evaluation technique to help with limitations experienced in a single train-test split. With a single score, a result could be unreliable and misleading due to one lucky or unlucky split, especially for small datasets. 

Cross validation gives you multiple accuracy scores based on k-folds, each time using k-1 folds for training and 1-fold for testing. It essentially evaluates the model multiple times on different subsets of the data.

2) **Why is it better than one train/test split?**

It retains more training data and gives better accuracy. It uses multiple folds, where k-1 is used to train the model and the held out portion is used as the "test set." It produces a list of accuracy scores vs a single score. The scores are then averaged, which produces a more reliable estimate of a model's ability to generalize on unseen data.


3) **What was your average model score?**

The logistical regression model, using a single train-test split, gave me an accuracy score of 0.67. The cross validation score for 5-folds was: [0.33333333, 1.0, 0.66666667, 1.0, 0.66666667]. The average accuracy from 5-fold cross validation was 0.73 with a std of 0.24. With small datasets like the one I used (15 samples), a standard deviation this big is expected. Errors produce bigger swings in metrics.