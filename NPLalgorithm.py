"""
Code used here is a amalgamation of tutorials from DataCamp and Analytics Vidya
Dataset used is a modified version of https://www.kaggle.com/datasets/kazanova/sentiment140
"""
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

sheet = pd.read_csv('tweets20.csv')
y = sheet.iloc[:, 0]
X = sheet

vectorizer = CountVectorizer()

tweets = [row[1] for index, row in sheet.iterrows()]


X = vectorizer.fit_transform(tweets)
X = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

log_reg = LogisticRegression(penalty='l2', C=1.2, max_iter=1000).fit(X_train, y_train)
print('Accuracy on train set: ', log_reg.score(X_train, y_train))
print('Accuracy on test set: ', log_reg.score(X_test, y_test))

# No test set here
# log_reg = LogisticRegression(max_iter=1000).fit(X, y)
# print('Accuracy of logistic regression: ', log_reg.score(X, y))
# print(log_reg.predict(X))
