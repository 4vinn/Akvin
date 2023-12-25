from flask import Flask, render_template, request
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from textblob import TextBlob
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired 
from flask_wtf.csrf import CSRFProtect

# Initializing Flask app
app = Flask(__name__)

# Secret key for CSRF protection
app.config['SECRET_KEY'] = 'iitd'
csrf = CSRFProtect(app)

# Loading dataset
df = pd.read_excel('data.xlsx')

# Extracting features (sentiment) and target variables (CAGR, QOLI, IV) and reshaping them
X = df['sentiment_score'].to_numpy().reshape(-1, 1)
Y_cagr = df['CAGR'].to_numpy().reshape(-1, 1)
Y_ql = df['Quality of Life Index'].to_numpy().reshape(-1, 1)
Y_iv = df['Investment Value'].to_numpy().reshape(-1, 1)

# Standardize Data (Z-score normalization) for each KPI
#------sentiment-----
X_mean = np.mean(X)
X_std = np.std(X)
X = (X - X_mean) / X_std #new X
#------CAGR-----------
Y_mean_cagr = np.mean(Y_cagr)
Y_std_cagr = np.std(Y_cagr)
Y_cagr = (Y_cagr - Y_mean_cagr) / Y_std_cagr #new Y_cagr
#------ql-----------
Y_mean_ql = np.mean(Y_ql)
Y_std_ql = np.std(Y_ql)
Y_ql = (Y_ql - Y_mean_ql) / Y_std_ql #new Y_ql
#------iv-----------
Y_mean_iv = np.mean(Y_iv)
Y_std_iv = np.std(Y_iv)
Y_iv = (Y_iv - Y_mean_iv) / Y_std_iv #new Y_iv

# Linear Regression Model Training
model_cagr_pred = LinearRegression().fit(X, Y_cagr)
model_qual_life_pred = LinearRegression().fit(X, Y_ql)
model_inv_val_pred = LinearRegression().fit(X, Y_iv)

def predictCAGR_QOLI_IV(sentiment):
    
    # Predict CAGR, QOLI, and IV values based on sentiment
    if sentiment is None:
        return None, None, None
    
    cagr = model_cagr_pred.predict([[sentiment]])
    qoli = model_qual_life_pred.predict([[sentiment]])
    iv = model_inv_val_pred.predict([[sentiment]])

    # Reverse the normalization to get original scale
    return cagr[0][0] * Y_std_cagr + Y_mean_cagr, qoli[0][0] * Y_std_ql + Y_mean_ql, iv[0][0] * Y_std_iv + Y_mean_iv

# For handling user input
class PredictionForm(FlaskForm):
    news_headline = StringField('News Headline', validators=[DataRequired()])

# Route for the home page
@app.route('/')
def index():
    form = PredictionForm()
    return render_template('index.html', form=form)

# Route for handling predictions
@app.route('/predict', methods=['POST'])
def predict():
    form = PredictionForm(request.form)

    if form.validate_on_submit():

        # Extract sentiment from the news headline
        news_headline = form.news_headline.data
        # ---no need right now--- print("News Headline:", news_headline)
        sentiment = TextBlob(news_headline).polarity
        # ---no need right now--- print("Extracted Sentiment:", sentiment)

        # Predict values for CAGR, QOLI, and IV
        cagr, qoli, iv = predictCAGR_QOLI_IV(sentiment)

        # Round the values to four decimal places
        cagr = round(cagr, 4) if cagr is not None else None
        qoli = round(qoli, 4) if qoli is not None else None
        iv = round(iv, 4) if iv is not None else None

        # Render the results on the web page
        return render_template('index.html', cagr=cagr, qoli=qoli, iv=iv, form=form)

    return render_template('index.html', form=form)

# Running the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)