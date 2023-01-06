import pandas as pd
from nltk.tokenize import TweetTokenizer
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

sheet = pd.read_csv('tweets.csv')
y = sheet.iloc[:, 0]
X = sheet
# print(y)
# print(type(y))

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()

tweets = [row[1] for index, row in sheet.iterrows()]

X = vectorizer.fit_transform(tweets)
X = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
print(type(X))
log_reg = LogisticRegression(max_iter=1000).fit(X, y)
print('Accuracy of logistic regression: ', log_reg.score(X, y))


print(log_reg.predict(X))

