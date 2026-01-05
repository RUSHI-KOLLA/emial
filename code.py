import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import recall_score,classification_report,accuracy_score

# Use the real-world dataset with more challenging classification
df = pd.read_csv(r'C:\\dev\\ml\\Email_Classifier\\noisy_emails.csv')
print(f"Dataset loaded: {len(df)} emails")
print(f"Categories: {df['category'].unique()}")

x = df['subject'] + " " + df['body']  # Combine subject and body
y = df['category']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state= 42)

vec = TfidfVectorizer() # convert text into numeric
x_train = vec.fit_transform(x_train)
x_test = vec.transform(x_test)
print(x_train)
print(df.info())
print(f"There is any infinity val:{np.isinf(x_train.data).any()}")

model = LogisticRegression()

model.fit(x_train,y_train)

pre = model.predict(x_test)
test_pred = model.predict(x_test)
test_accuracy = accuracy_score(y_test, test_pred)

print(f"Test Accuracy:     {test_accuracy * 100:.2f}%")
recall = recall_score(y_test,pre,average='macro')
accuracy = accuracy_score(y_test,pre)
clre = classification_report(y_test,pre)

print(f'recall_score:{recall}\n accuracy_score:{accuracy*100:.2f}% \n classification_report:{clre}\n')
# --- Add this at the bottom to test new emails ---

def predict_email(text):
    text_vec = vec.transform([text])
    prediction = model.predict(text_vec)
    return prediction[0]

# Test Examples
sample_1 = "Hey friend, are you coming to the party tonight?"
sample_2 = "Security Alert: Please verify your account login."
sample_3 = "Flash Sale! Get 50% off your next order."

print("-" * 30)
print(f"Email: '{sample_1}' -> Pred: {predict_email(sample_1)}")
print(f"Email: '{sample_2}' -> Pred: {predict_email(sample_2)}")
print(f"Email: '{sample_3}' -> Pred: {predict_email(sample_3)}")
print("-" * 30)