# Credit Risk - README

## Project Overview
This project builds a machine learning model to classify loan borrowers as good or bad credit risks using a dataset of loan information. The process includes data cleaning, feature engineering, handling class imbalance with SMOTE-Tomek, and training an XGBoost model with cost-sensitive learning. A Streamlit app is also created to allow users to upload borrower data for predictions.

## Steps Implemented
1. **Data Exploration and Cleaning**
   - Dropped columns with high missing values.
   - Handled missing data in numerical and categorical columns.
   - Encoded categorical variables using label encoding and one-hot encoding.

2. **Feature Engineering**
   - Scaled numerical features using `StandardScaler`.
   - Handled outliers by capping at the 99th percentile.

3. **Class Imbalance Handling**
   - Used SMOTE-Tomek to balance the dataset.
   - Applied cost-sensitive learning by adjusting class weights.

4. **Model Training and Evaluation**
   - Evaluated Logistic Regression, Random Forest, XGBoost, LightGBM, and CatBoost.
   - Performed hyperparameter tuning using GridSearchCV.
   - Selected XGBoost as the final model based on performance metrics.

5. **Feature Selection**
   - Selected top 15 features based on importance from the XGBoost model.

6. **Streamlit App Development**
   - Built an app to upload an Excel file and predict borrower risk.
   - Provided a downloadable Excel template for input data.

## Final Selected Features
- term, sub_grade, emp_length, initial_list_status, application_type, loan_amnt, int_rate, installment, annual_inc, dti, delinq_2yrs, inq_last_6mths, mths_since_last_delinq, open_acc, pub_rec

## How to Run the Project
- **Jupyter Notebook:** Open `DataModeling.ipynb` to review the full data analysis and modeling process.
- **Streamlit App:** Run the app with `streamlit run app.py` to predict borrower risk.

## Results and Next Steps
- The XGBoost model achieved high accuracy but still needs improvements in predicting the minority class.
- Future work could involve acquiring more data, further hyperparameter tuning, or using ensemble methods.
