from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
import pandas as pd
import re

#load the Dataset
data = pd.read_csv("Ling.csv")

#Combine subject and body
data["text"] = data["subject"].fillna('') + " " + data["body"].fillna('')
data = data.dropna(subset=["label"])

#print(data[["text" , "label"]].head())

# Clean the text
def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]' , '', text)  #remove special characters/numbers
    text = text.lower()                       #lowercase everything
    text = text.strip()                       #remove leading/trailing whitespace
    return text

data["clean_text"] = data["text"].apply(clean_text)

# Preview the cleaned version
#print(data[["clean_text", "label"]].head())

# Convert text to TF-IDF vectors
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X = vectorizer.fit_transform(data["clean_text"])

# Convert labels to a list (target values)
y = data["label"].astype(int)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42)

# Train a Naive Bayes model
model = MultinomialNB()
model.fit(X_train,y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy: ", accuracy_score(y_test,y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Train a Naive Bayes model
log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train,y_train)

# Predict on test data
log_pred = log_model.predict(X_test)

# Evaluate
print("Logistic Regression Accuracy: ", accuracy_score(y_test, log_pred))
print("Classification Report:\n", classification_report(y_test, log_pred))
