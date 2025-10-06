import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the car information data from CSV file
data = pd.read_csv('Automobile.csv')

# Select columns for correlation matrix
cols = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year']

# Create a correlation matrix
corr_matrix = data[cols].corr()

# Plot the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.4f', square=True)
plt.title('Correlation Matrix of Car Information')
plt.show()
