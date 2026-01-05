# Email Classifier 📧

An intelligent email classification system that automatically categorizes emails into different types (Primary, Social, Updates, Promotions) using Machine Learning. The project includes a standalone classifier, a RESTful API backend, and an interactive web interface.

## 🌟 Features

- **Machine Learning Classification**: Uses Logistic Regression with TF-IDF vectorization to classify emails
- **Multiple Interfaces**: Standalone script, REST API, and interactive web UI
- **Real-time Predictions**: Classify emails instantly through the web interface
- **High Accuracy**: Trained on a comprehensive dataset for reliable predictions
- **History Tracking**: View your recent classification history in the web UI
- **RESTful API**: Easy integration with other applications

## 📋 Categories

The classifier categorizes emails into four types:
- **👔 Primary**: Important work-related emails, project discussions, meetings
- **👥 Social**: Social interactions, personal messages, casual conversations
- **🔔 Updates**: System notifications, alerts, status updates
- **🏷️ Promotions**: Marketing emails, sales, promotional content

## 🛠️ Tech Stack

- **Python 3.x**
- **Machine Learning**: scikit-learn (Logistic Regression, TF-IDF Vectorizer)
- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Data Processing**: Pandas, NumPy
- **HTTP Client**: Requests

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/RUSHI-KOLLA/emial.git
cd emial
```

2. Install required dependencies:
```bash
pip install pandas numpy scikit-learn fastapi uvicorn streamlit requests
```

## 📊 Dataset

The project uses `noisy_emails.csv` which contains:
- **subject**: Email subject line
- **body**: Email body content
- **category**: Classification label (Primary, Social, Updates, Promotions)

## 🚀 Usage

### Option 1: Standalone Classifier (code.py)

Train and test the model directly:

```bash
python code.py
```

This script will:
- Load the dataset from `noisy_emails.csv`
- Train a Logistic Regression model
- Display accuracy metrics and classification report
- Test sample emails with predictions

**Important**: The code.py file has a hardcoded Windows path on line 9. Update it to match your system:
```python
# Current (Windows-specific):
df = pd.read_csv(r'C:\\dev\\ml\\Email_Classifier\\noisy_emails.csv')

# Recommended change (relative path):
df = pd.read_csv('noisy_emails.csv')
```

### Option 2: Full Application (Backend + Frontend)

#### Step 1: Start the Backend Server

```bash
uvicorn backend:app --reload
```

The FastAPI server will start at `http://127.0.0.1:8000`

#### Step 2: Launch the Frontend

In a new terminal:

```bash
streamlit run frontend.py
```

The Streamlit app will open in your browser (typically at `http://localhost:8501`)

#### Step 3: Use the Web Interface

1. Enter an email subject line
2. Enter the email body
3. Click "🔍 Classify Email"
4. View the predicted category
5. Check recent history in the sidebar

## 🔌 API Documentation

### Endpoint: `/predict`

**Method**: POST

**Request Body**:
```json
{
  "subject": "Meeting Tomorrow",
  "body": "Hi team, just a reminder about our project meeting tomorrow at 10 AM"
}
```

**Response**:
```json
{
  "category": "Primary"
}
```

**Example with cURL**:
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"subject": "Flash Sale!", "body": "Get 50% off today only!"}'
```

## 📝 Code Structure

### code.py
- Standalone training and testing script
- Loads dataset and trains the model
- Displays performance metrics (accuracy, recall, classification report)
- Includes prediction function for testing custom emails

### backend.py
- FastAPI server implementation
- Trains model on startup
- Provides `/predict` endpoint for real-time classification
- Returns JSON responses with predicted categories

### frontend.py
- Streamlit-based web interface
- User-friendly email input form
- Real-time classification via backend API
- History tracking with session state
- Styled UI with category emojis

## 📈 Model Performance

The model uses:
- **Algorithm**: Logistic Regression
- **Feature Extraction**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Train/Test Split**: 80/20
- **Text Features**: Combined subject and body text

Performance metrics are displayed when running `code.py`:
- Test Accuracy
- Recall Score
- Classification Report (Precision, Recall, F1-Score per category)

## 🔧 Troubleshooting

### Backend Connection Error
If the frontend shows "Could not connect to backend":
1. Ensure the backend server is running (`uvicorn backend:app --reload`)
2. Verify it's running on `http://127.0.0.1:8000`
3. Check there are no firewall issues

### CSV File Not Found
Make sure `noisy_emails.csv` is in the same directory as your Python scripts.

### Model Training Error
Ensure all dependencies are installed and the CSV file has the correct format (subject, body, category columns).

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**RUSHI-KOLLA**

---

**Note**: This project is designed for educational purposes and demonstrates email classification using machine learning techniques.