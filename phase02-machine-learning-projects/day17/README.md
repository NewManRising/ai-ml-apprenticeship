1) **Which columns were one-hot encoded?** All the categorical columns (['sex', 'housing', 'saving_accounts', 'checking_account', 'purpose']) were encoded except "risk."

2) **How many feature columns existed before encoding?** After the risk column was excluded, there were 9 feature columns. 

3) **How many feature columns exist after encoding?** After encoding there were 21 columns.
4) **What does one-hot encoding do?** It transforms categorical values into binary feature columns that a machine learning model can read and use.
5) **Why was one-hot encoding used instead of label encoding?** One-hot encoding was used because label encoding assumes an order or ranking. The data in this dataset has no order and therefore one-hot encoding is the choice to use. 
6) **What did drop_first=True do?** It removed one category per encoded column set to reduce redundancy and make one category the baseline. It also prevents multicollinearity.
7) **What is the Target Variable?** The target variable is risk.
8) **What are X and y?** X contains the model features and y contains the label/target variable.