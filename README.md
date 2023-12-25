###Project Structure

1) app.py:         Main Flask application file (Model).
2) data.xlsx:     Excel file containing data set.
3) static/	         Folder containing static assets (images, CSS files, etc.).
4) templates/:  Folder containing HTML template.


###Additional Notes

**Model Training and Prediction Process**

1) Data Preparation:
Loaded data from 'data.xlsx' containing historical information on sentiment scores, CAGR, Quality of Life Index (QOLI), and Investment Value (IV).
Extracted and reshaped the data for input features (X: sentiment scores) and target variables (Y_cagr, Y_ql, Y_iv).

2) Data Standardization:
Applied Z-score normalization to standardize data for both input sentiment scores and each KPI (CAGR, QOLI, IV).
Ensured consistency in scale across features to improve model training.

3) Linear Regression Model Training:
Utilized LinearRegression from scikit-learn to train three separate models for predicting CAGR, QOLI, and IV.
Each model was fitted using the standardized sentiment scores (X) as input and the corresponding standardized KPI values as target (Y_cagr, Y_ql, Y_iv).

4) Prediction Function:
Created a function predictCAGR_QOLI_IV to predict the KPI values given a sentiment score as input.
The function takes a sentiment score, predicts the standardized values using the trained models, and then transforms them back to the original scale.

5) Web Interface:
Developed a web-based dashboard using Flask, where users can input news headlines via a user-friendly interface.
Incorporated a sentiment analysis library (TextBlob) to extract sentiment polarity from the provided news headline.

6) Prediction Process:
Upon submitting a news headline, the application extracts the sentiment and uses the trained models to predict the impact on CAGR, QOLI, and IV.
Predicted values are then rounded to four decimal places for clarity and presented on the web page.