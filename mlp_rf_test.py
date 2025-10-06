import pandas as pd
import joblib

# Load the pre-trained Random Forest Regressor model
model = joblib.load(open('mlp_rf.sav', 'rb')) 

# Take user input for car horsepower and weight
displacement = float(input("Enter car engine displacement: "))
horsepower = float(input("Enter car horsepower: "))
weight = float(input("Enter car weight: "))

# Create a DataFrame with user input
user_data = pd.DataFrame([[None, displacement, horsepower, weight, None, None]], columns=['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year'])

# Use the model to predict the mpg
predicted_mpg = model.predict(user_data)[0]

# Display the predicted mpg
print(f"Predicted miles per gallon (mpg): {predicted_mpg}")