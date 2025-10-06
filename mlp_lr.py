import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# Load the car information data from CSV file
data = pd.read_csv('C:\\Om Jethva\\DJSCE\\SEM 6\\ML\\carfueleffiency\\Automobile.csv')

data.dropna(subset=['horsepower'], inplace=True)

# Extract features (X) and target variable (y)
X = data[['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year']]
y = data['mpg']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a Linear Regression model
model = LinearRegression()

# Train the model on the training set
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate Mean Absolute Error (MAE)
mae = mean_absolute_error(y_test, y_pred)

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)

# Calculate R-squared
r2 = r2_score(y_test, y_pred)

score = model.score(X_test, y_test)

print(f"Mean Absolute Error (MAE): {mae}")
print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared Value: {r2}")
print(f"Accuracy: {score}")

filename = 'mlp_lr.sav'
joblib.dump(model, open(filename, 'wb'))