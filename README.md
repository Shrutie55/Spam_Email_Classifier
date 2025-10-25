📧 Spam Email Classifier

A simple Machine Learning-based Spam Email Classifier built using Python, Flask, and Scikit-learn.
It predicts whether a given email or message is Spam or Not Spam (Ham) using text classification techniques.

🚀 Features

Preprocesses and cleans input text

Uses TF-IDF Vectorization for feature extraction

Trained using Naive Bayes and Logistic Regression models

Flask web app interface for user input and prediction

Models saved using joblib for quick loading

🧩 Tech Stack

Python

Flask

Scikit-learn

Pandas & NumPy

HTML, CSS (Flask Templates)

⚙️ How to Run
# Clone this repository
git clone https://github.com/<your-username>/spam-email-classifier.git

# Navigate to the project folder
cd spam-email-classifier

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py


Now open http://127.0.0.1:5000/
 in your browser to use the app.

📁 Project Structure
app.py                # Flask application
spam_email.ipynb      # Model training notebook
spam_ham_dataset.xls  # Dataset
model.joblib          # Trained ML model
vectorizer.joblib     # TF-IDF vectorizer
templates/            # HTML files
static/               # CSS/JS files
