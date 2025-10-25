# 📧 Spam Email Classifier

A simple **Machine Learning-based Spam Email Classifier** built using **Python**, **Flask**, and **Scikit-learn**.  
It predicts whether an email or message is **Spam** or **Not Spam (Ham)** using natural language processing techniques.

---

## 🚀 Features
- 🧹 Text preprocessing and cleaning  
- 🔤 TF-IDF Vectorization for feature extraction  
- 🤖 Trained using **Naive Bayes** and **Logistic Regression** models  
- 🌐 Flask web app interface for predictions  
- 💾 Models saved using `joblib` for fast loading  

---

## 🧩 Tech Stack
- **Python 3.x**  
- **Flask**  
- **Scikit-learn**  
- **Pandas**, **NumPy**  
- **HTML**, **CSS**

---

## ⚙️ How to Run

```bash
# Clone this repository
git clone https://github.com/<your-username>/spam-email-classifier.git

# Navigate to the project folder
cd spam-email-classifier

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py

---
##📁 Project Structure
├── app.py                # Main Flask application
├── spam_email.ipynb      # Model training and evaluation
├── spam_ham_dataset.xls  # Dataset used for training
├── model.joblib          # Trained ML model
├── vectorizer.joblib     # TF-IDF vectorizer
├── templates/            # HTML templates
├── static/               # CSS and JS files
└── requirements.txt      # Dependencies

##📊 Model Training

Dataset: Spam-Ham Email Dataset (.xls)

Models: Naive Bayes, Logistic Regression

Metrics: Accuracy, Precision, Recall, F1-score

##📈 Future Enhancements

🌍 Multi-language support

☁️ Cloud deployment (Heroku / AWS)

##📬 Integration with live email services

🎨 Enhanced UI using Bootstrap or React
