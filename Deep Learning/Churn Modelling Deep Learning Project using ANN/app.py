import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import StandardScaler,LabelEncoder, OneHotEncoder
import pickle
from tensorflow.keras.models import load_model

# Loading the trained model, scaler, one hot and label encoder
model = load_model('model.h5', compile=False)

with open("label_encoder_gender.pkl",'rb') as file:
    label_encoder_gender=pickle.load(file)

with open("onehot_encoder_geo.pkl",'rb') as file:
    onehot_encoder_geo=pickle.load(file)

with open("scaler.pkl",'rb') as file:
    scaler=pickle.load(file)


## Streamlit App
st.title("Customer Churn Prediction")

geography=st.selectbox('Geography',onehot_encoder_geo.categories_[0])
gender=st.selectbox('Gender',label_encoder_gender.classes_)
age=st.slider('Age',18,92)
balance=st.number_input('Balance')
credit_score=st.number_input('Credit Score')
estimated_salary=st.number_input('Estimated Salary')
tenure=st.slider('Tenure',0,10)
num_of_products=st.slider('Number of Products',1,4)
has_cr_card=st.selectbox('Has Credit Card',[0,1])
is_active_member=st.selectbox('Is Active Member',[0,1])

input_data=pd.DataFrame({
    "CreditScore":[credit_score],
    "Gender":[gender],
    "Age":[age],
    "Tenure":[tenure],
    "Balance":[balance],
    "NumOfProducts":[num_of_products],
    "HasCrCard":[has_cr_card],
    "IsActiveMember":[is_active_member],
    "EstimatedSalary":[estimated_salary]
})

input_data['Gender']=label_encoder_gender.transform(input_data['Gender'])

encoded_geo=onehot_encoder_geo.transform([[geography]]).toarray()
geography_df=pd.DataFrame(encoded_geo,columns=onehot_encoder_geo.get_feature_names_out())
input_df=pd.concat([input_data,geography_df],axis=1)

# Scaling the input data
input_scaled=scaler.transform(input_df)

# Prediction
prediction_probability=model.predict(input_scaled)
st.write(f"The Prediction is: {prediction_probability}")

if(prediction_probability>0.5):
    st.write("The customer is likely to churn")
else:
    st.write("The customer is not likely to churn")