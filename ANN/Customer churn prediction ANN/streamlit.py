import streamlit as st
import pandas as pd
import tensorflow as tf
import joblib

# Load the saved model and preprocessing objects
model = tf.keras.models.load_model('best_model.pkl')
le = joblib.load('label_encoder.pkl')
ct = joblib.load('column_transformer.pkl')
sc = joblib.load('scaler.pkl')

# Streamlit app
st.title('Customer Churn Prediction')

# User inputs
credit_score = st.number_input('Credit Score', min_value=300, max_value=900, value=600)
geography = st.selectbox('Geography', ['France', 'Spain', 'Germany'])
gender = st.selectbox('Gender', ['Male', 'Female'])
age = st.number_input('Age', min_value=18, max_value=100, value=30)
tenure = st.number_input('Tenure', min_value=0, max_value=10, value=5)
balance = st.number_input('Balance', min_value=0.0, value=10000.0)
num_of_products = st.number_input('Number of Products', min_value=1, max_value=4, value=1)
has_cr_card = st.selectbox('Has Credit Card', [0, 1])
is_active_member = st.selectbox('Is Active Member', [0, 1])
estimated_salary = st.number_input('Estimated Salary', min_value=0.0, value=50000.0)

# Create input data dictionary
input_data = {
    'CreditScore': credit_score,
    'Geography': geography,
    'Gender': gender,
    'Age': age,
    'Tenure': tenure,
    'Balance': balance,
    'NumOfProducts': num_of_products,
    'HasCrCard': has_cr_card,
    'IsActiveMember': is_active_member,
    'EstimatedSalary': estimated_salary
}

# Function to preprocess input data
def preprocess_input(data):
    # Convert input data to DataFrame
    df = pd.DataFrame([data])
    
    # Apply one-hot encoding for categorical variables
    df = pd.get_dummies(df, columns=['Geography', 'Gender'])
    
    # Ensure the dataframe has the same columns as used in training
    expected_columns = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts',
                        'HasCrCard', 'IsActiveMember', 'EstimatedSalary', 'Geography_France',
                        'Geography_Germany', 'Geography_Spain', 'Gender_Female', 'Gender_Male']
    
    for col in expected_columns:
        if col not in df.columns:
            df[col] = 0
    
    # Reorder columns to match training data
    df = df[expected_columns]
    
    # Apply StandardScaler
    df_scaled = sc.transform(df)
    
    return df_scaled

# Button for prediction
if st.button('Predict'):
    # Preprocess the input data
    preprocessed_data = preprocess_input(input_data)
    
    # Make prediction
    predictions = model.predict(preprocessed_data)
    predictions_binary = (predictions > 0.5).astype(int)
    
    # Display prediction result
    if predictions_binary[0] == 1:
        st.write('The customer is likely to churn.')
    else:
        st.write('The customer is not likely to churn.')

# Run the Streamlit app
if __name__ == '__main__':
    st.run()


# # User inputs
# credit_score = st.number_input('Credit Score', min_value=300, max_value=900, value=600)
# geography = st.selectbox('Geography', ['France', 'Spain', 'Germany'])
# gender = st.selectbox('Gender', ['Male', 'Female'])
# age = st.number_input('Age', min_value=18, max_value=100, value=30)
# tenure = st.number_input('Tenure', min_value=0, max_value=10, value=5)
# balance = st.number_input('Balance', min_value=0.0, value=10000.0)
# num_of_products = st.number_input('Number of Products', min_value=1, max_value=4, value=1)
# has_cr_card = st.selectbox('Has Credit Card', [0, 1])
# is_active_member = st.selectbox('Is Active Member', [0, 1])
# estimated_salary = st.number_input('Estimated Salary', min_value=0.0, value=50000.0)