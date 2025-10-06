import streamlit as st

st.header('Car Fuel Efficiency Predictor')

txt = '''
The automotive industry is continuously evolving, with a growing focus on fuel efficiency and environmental sustainability. In this context, the ability to predict a car's fuel efficiency based on its specifications is invaluable for manufacturers, consumers, and policymakers alike. Our project aims to leverage machine learning techniques to predict the miles per gallon (mpg) of cars, a key indicator of fuel efficiency.

In our quest to predict the fuel efficiency of cars, we conducted an extensive literature survey to explore various machine learning models. The models considered included Linear Regression, Random Forest, and Support Vector Machines (SVM). Our objective was to identify the most suitable model that could accurately predict the miles per gallon (mpg) of cars based on their specifications. Linear Regression is a simple and interpretable model that assumes a linear relationship between the input features and the target variable. However, it may not capture complex patterns in the data. On the other hand, Random Forest is an ensemble learning method that builds multiple decision trees and combines their predictions to improve accuracy. It is known for its robustness and ability to handle non-linear relationships in the data. SVM is another powerful model that can capture complex relationships in the data by mapping the input features into a higher-dimensional space. However, SVM is computationally heavy, especially with large datasets.

After analyzing the performance of these models on our dataset, we found that Random Forest outperformed Linear Regression in terms of accuracy. Random Forest's ability to handle non-linear relationships in the data made it more suitable for our prediction task. Additionally, SVM showed comparable accuracy to Random Forest but was computationally heavier, making it less practical for our application. Based on our literature survey and model comparison, we concluded that Random Forest is the optimal choice for predicting the fuel efficiency of cars in our project. Its high accuracy and ability to handle non-linear relationships in the data make it well-suited for this task. By selecting Random Forest as our model, we aim to build a robust and accurate prediction system for fuel efficiency, which can benefit the automotive industry and environmental sustainability efforts.
'''

st.write(txt)
