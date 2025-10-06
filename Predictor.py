import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained Random Forest Regressor model
model = joblib.load(open('C:\\Om Jethva\\DJSCE\\SEM 6\\ML\\carfueleffiency\\mlp_rf.sav', 'rb')) 

# Take user input for car details
displacement = st.text_input("Enter car engine displacement (cubic inches - ci): ")
horsepower = st.text_input("Enter car horsepower (hp): ")
weight = st.text_input("Enter car weight (pounds - lbs): ")

# Add a submit button
if st.button("Submit"):
    # Convert user input to float
    displacement = float(displacement) if displacement else None
    horsepower = float(horsepower) if horsepower else None
    weight = float(weight) if weight else None

    # Create a DataFrame with user input
    user_data = pd.DataFrame([[None, displacement, horsepower, weight, None, None]], 
                             columns=['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year'])

    # Use the model to predict the mpg
    predicted_mpg = model.predict(user_data)[0]

    # Display the predicted mpg
    st.write(f"Predicted miles per gallon (mpg): {predicted_mpg}")
