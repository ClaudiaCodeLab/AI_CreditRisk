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

st.title("Aplicación de Predicción de Riesgo de Crédito")
#st.write("Aquí tienes un [ejemplo del fichero excel](https://docs.google.com/spreadsheets/d/1ls5y30XinLHIexTI2CMIVad9pmCzGhZr/edit?usp=drive_link&ouid=107476812262514809219&rtpof=true&sd=true)")
with open('example_data.xlsx', 'rb') as file:
    st.download_button(
        label="Aquí tiene un ejemplo del fichero excel",
        data=file,
        file_name='example_file.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )


st.write("Carga un archivo Excel con datos de prestatarios para predecir si son buenos o malos pagadores.")

uploaded_file = st.file_uploader("Carga un archivo Excel", type=["xls", "xlsx"])

if uploaded_file is not None:
    data = pd.read_excel(uploaded_file)
    st.write("Vista previa de los datos:")
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

        st.write("## Predicciones:")
        results = data.copy()
        results['Predicción'] = prediction_labels
        st.dataframe(results)

        output = results.to_excel("predictions_output.xlsx", index=False)        
    else:
        st.error("El archivo subido no contiene todas las columnas requeridas. Por favor, incluya las siguientes columnas: {}".format(', '.join(required_features)))
