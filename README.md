### A dashboard to predict the effect of news headlines on GDP

For now, its specifically focused on Infrastructure sector. We took 3 KPIs of infrastructure sector<br>
- CAGR 
- Quality of Life Index (QOLI)
- Investment Value (IV)

#### Deployed on pythonanywhere

Live Demo **[here](http://4vinn.pythonanywhere.com/) !**

---

#### Project Structure

```
.
├── static/
│   ├── iitd.jpg
│   ├── iitlogo.png
│   ├── index.css
│   └── style.css
├── templates/
|   └── index.html
|    
├── app.py
├── data.xlsx
├── Instruction.txt
└── README.md

```
> app.py ------ Main Flask application file (Model) <br>
> data.xlsx ---- Excel file containing historical information on sentiment scores and KPIs <br>
> static -------- Folder containing static assets (images, CSS files, etc.) <br>
> templates/ -- Folder containing HTML template <br>

<details> 
<summary> Additional Notes </summary>

**Model Training and Prediction Process**

- **Data Preparation:**
Loaded data from `data.xlsx` containing historical information on sentiment scores, CAGR, Quality of Life Index (QOLI), and Investment Value (IV).
`Extracted and reshaped the data` for input features (X: sentiment scores) and target variables (Y_cagr, Y_ql, Y_iv).

- **Data Standardization:**
Applied `Z-score normalization` to standardize data for both input sentiment scores and each KPI (CAGR, QOLI, IV).
Ensured consistency in scale across features to improve model training.

- **Linear Regression Model Training:**
Utilized `LinearRegression` from scikit-learn to `train three separate models for predicting each KPIs`: CAGR, QOLI, and IV.
Each model was fitted using the standardized sentiment scores (X) as input and the corresponding standardized KPI values as target (Y_cagr, Y_ql, Y_iv).

- **Prediction Function:**
Created a function `predictCAGR_QOLI_IV` to predict the KPI values given a sentiment score as input.
The `function takes a sentiment score`, predicts the standardized values using the trained models, and then transforms them back to the original scale.

- **Web Interface:**
Developed a web-based dashboard using `Flask`, where users can input news headlines via a user-friendly interface.
Incorporated a sentiment analysis library (`TextBlob`) to extract sentiment polarity from the provided news headline.

- **Prediction Process:**
Upon submitting a news headline, the application `extracts the sentiment` and uses the trained models to predict the impact on CAGR, QOLI, and IV.
Predicted values are then rounded to four decimal places for clarity and presented on the web page.

</details>
