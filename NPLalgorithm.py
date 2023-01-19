"""
Code used here is a amalgamation of tutorials from DataCamp and Analytics Vidya
Dataset used is a modified version of https://www.kaggle.com/datasets/kazanova/sentiment140

Code has been modified via Github Copilot
"""
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer



# Reading the file
sheet = pd.read_csv('tweets20.csv')
y = sheet.iloc[:, 0]
X = sheet

vectorizer = TfidfVectorizer()

tweets = [row[1] for index, row in sheet.iterrows()]

# Transforming the data
X = vectorizer.fit(tweets)
X = vectorizer.transform(tweets)
X = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())


# Training and splitting data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Generating the model
model = LogisticRegression(penalty='l2', C=1.2, max_iter=1000).fit(X_train, y_train)

# Testing accuracy
print('Accuracy on train set: ', model.score(X_train, y_train))
print('Accuracy on test set: ', model.score(X_test, y_test))

# # Saving the model to a file
# with open('api_model.pkl', 'wb') as file:
#     pickle.dump(model, file)

# No test set here
# log_reg = LogisticRegression(max_iter=1000).fit(X, y)
# print('Accuracy of logistic regression: ', log_reg.score(X, y))
# print(log_reg.predict(X))
