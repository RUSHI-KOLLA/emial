from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# 1. Initialize the API
app = FastAPI()

# 2. Global variables
model = None
vec = None

# 3. Train the model when the server starts
print("Training model...")
try:
    # Make sure 'noisy_emails.csv' is in the same folder!
    df = pd.read_csv('noisy_emails.csv')
    x = df['subject'] + " " + df['body']
    y = df['category']

    vec = TfidfVectorizer()
    x_train = vec.fit_transform(x)

    model = LogisticRegression()
    model.fit(x_train, y)
    print("✅ Model trained successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")

# 4. Define the data format
class EmailRequest(BaseModel):
    subject: str
    body: str

# 5. The Prediction Endpoint
@app.post("/predict")
def predict(email: EmailRequest):
    if not model or not vec:
        return {"category": "Error: Model not trained"}
        
    full_text = email.subject + " " + email.body
    text_vec = vec.transform([full_text])
    prediction = model.predict(text_vec)[0]
    return {"category": prediction}