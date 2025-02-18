# Streamlit App for Borrower Prediction
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('xgb_cost_sensitive_model.pkl')

# Corrected list of required features based on model
required_features = ['term', 'sub_grade', 'emp_length', 'initial_list_status',
                     'application_type', 'loan_amnt', 'int_rate', 'installment',
                     'annual_inc', 'dti', 'delinq_2yrs', 'inq_last_6mths',
                     'mths_since_last_delinq', 'open_acc', 'pub_rec']

st.title("Borrower Credit Risk Prediction App")
st.write("Upload an Excel file with borrower data to predict if they are good or bad borrowers.")

uploaded_file = st.file_uploader("Upload Excel file", type=["xls", "xlsx"])

if uploaded_file is not None:
    data = pd.read_excel(uploaded_file)
    st.write("Data Preview:")
    st.dataframe(data.head())

    if all(feature in data.columns for feature in required_features):
        input_data = data[required_features]

        # Convert categorical features to category dtype
        categorical_features = ['sub_grade', 'initial_list_status', 'application_type']
        for col in categorical_features:
            input_data[col] = input_data[col].astype('category')

        # Make predictions
        predictions = model.predict(input_data)
        prediction_labels = ['Good Borrower' if pred == 1 else 'Bad Borrower' for pred in predictions]

        st.write("## Predictions:")
        results = data.copy()
        results['Prediction'] = prediction_labels
        st.dataframe(results)

        output = results.to_excel("predictions_output.xlsx", index=False)        
    else:
        st.error("Uploaded file does not contain all required features. Please include the following features: {}".format(', '.join(required_features)))
