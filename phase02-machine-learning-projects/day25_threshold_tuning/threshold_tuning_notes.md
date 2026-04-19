The goal of this task was to determine the best decision threshold for predictions. The criteria for selecting the best threshold was based on highest recall.

However, precision goes down as the recall increases, indicating that there is a tradeoff for this. I want as much as the minority class predicted as possible while making sure False Positives are not too unreasonable or excessive.

Since this model is predicting customers that are a credit risk, having the higher recall of this class is most important.

My threshold comparison table I calculated is below:

```
Threshold Comparison Table:
   threshold  precision_class_1  recall_class_1  f1_class_1  precision_class_0  recall_class_0  f1_class_0  accuracy
0        0.3           0.345455        0.950000    0.506667           0.914286        0.228571    0.365714     0.445
1        0.4           0.428571        0.900000    0.580645           0.918919        0.485714    0.635514     0.610
2        0.5           0.500000        0.750000    0.600000           0.863636        0.678571    0.760000     0.700
3        0.6           0.600000        0.450000    0.514286           0.787097        0.871429    0.827119     0.745
4        0.7           0.800000        0.133333    0.228571           0.726316        0.985714    0.836364     0.730
```

The threshold of 0.4 seems to be optimal for this problem. Recall for class 1 (credit risk) is 0.90 with a precision of 0.43. I believe this is the best balance.

This is an imbalanced dataset that has class weights applied, has been fined tuned with GridSearchCV, and was tested on unseen data through a train-test split. 

I calculated the ROC_AUC score and that was 0.78. Not the best, but pretty good considering the nature of the dataset and problem.

Here was the confusion matrix at the 0.4 decision threshold:

```
Confusion Matrix:
[[68 72]
 [ 6 54]]
```

Only 6 cases of credit risk were missed which is about the most acceptable for me.