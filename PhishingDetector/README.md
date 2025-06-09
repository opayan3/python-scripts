# 📧 Phishing Email Detector

This project uses machine learning to detect phishing emails based on their content, using both the email subject and body text.

## 🧠 Models Used
- Naive Bayes (Multinomial)
- Logistic Regression

## 🔍 How It Works
1. Loads a CSV file (`Ling.csv`) with three columns:
   - `subject`: Email subject line
   - `body`: Main email content
   - `label`: 0 (safe) or 1 (phishing)
2. Combines subject + body into a single text input.
3. Cleans the text: removes punctuation, lowers case, strips whitespace.
4. Converts text into TF-IDF features.
5. Splits data into training and testing sets.
6. Trains and evaluates both models using accuracy and classification report.

## 📊 Sample Output
Accuracy:  0.94
Classification Report:
precision    recall  f1-score   support
0       0.95      0.94      0.94       350
1       0.93      0.94      0.94       340
accuracy                           0.94       690

## 🗃️ Note on Dataset
The dataset used in this project was sourced from [Kaggle: Email Spam Detection Dataset](https://www.kaggle.com/datasets/suryadulal/email-spam-detection-dataset).  
Make sure to download the CSV file from Kaggle and name it `Ling.csv`, or update the code to reflect your filename.

📚 What I Learned
	•	How to clean and vectorize text data using TF-IDF
	•	Differences in performance between Naive Bayes and Logistic Regression
	•	Importance of proper data preparation in NLP tasks
