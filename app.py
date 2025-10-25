from flask import Flask, redirect, request, url_for, render_template
from joblib import load
import string
import pandas as pd 
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

# Load the trained model and vectorizer
model = load('model_naive.joblib')
vectorizer = load('vectorizer.joblib')

@app.route('/')
def index():
    return 'hello'

@app.route('/spam',methods=['GET', 'POST'])
def preprocess(email):
    try:
        # Initialize Porter Stemmer and stopwords
        stemmer = PorterStemmer()
        stopwords_set = set(stopwords.words('english'))

        # Preprocess the email text to classify
        email_to_classify = email
        email_text = email_to_classify.lower().translate(str.maketrans('', '', string.punctuation)).split()
        email_text = [stemmer.stem(word) for word in email_text if word not in stopwords_set]
        email_text = ' '.join(email_text)
        email_corpus = [email_text]

        # Vectorize the email text using the same vectorizer as during training
        X_email = vectorizer.transform(email_corpus)

        # Make prediction
        result = model.predict(X_email)
        if result == 0:
            return "The mail is not spam"
        elif result == 1:
            return "The mail is spam"
        else: 
            return "Cant classify or Error occured"

    except Exception as e:
        return str(e)


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        email = request.form['email']
        result = preprocess(email)  # Call the preprocess function with the email
        return render_template('result.html', result=result)
    else:
        return render_template('form.html')

    
if __name__ == '__main__':
    app.run(debug=True)
