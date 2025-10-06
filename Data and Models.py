import streamlit as st
import pandas as pd

st.header('Dataset:')
df = pd.read_csv('C:\\Om Jethva\\DJSCE\\SEM 6\\ML\\carfueleffiency\\Automobile.csv')
st.dataframe(df)

st.header('Correlations:')
st.subheader('Heatmap:')
st.image('C:\\Om Jethva\\DJSCE\\SEM 6\\ML\\carfueleffiency\\Data Visuals\\correlation_matrix.png')

st.subheader('Strong Positive Correlations:')

st.write('Car Engine Displacement (cubic inch) vs Car Horsepower (hp):')
st.image('C:\\Om Jethva\\DJSCE\\SEM 6\\ML\\carfueleffiency\\Data Visuals\\relation_displacement_horsepower.png')

st.write('Car Engine Displacement (cubic inch vs Car Weight (lbs):')
st.image('C:\\Om Jethva\\DJSCE\\SEM 6\\ML\\carfueleffiency\\Data Visuals\\relation_displacement_weight.png')

st.write('Car Horsepower (hp) vs Car Weight (lbs):')
st.image('C:\\Om Jethva\\DJSCE\\SEM 6\\ML\\carfueleffiency\\Data Visuals\\relation_horsepower_weight.png')

st.subheader('Strong Negative Correlations:')

st.write(' Car Fuel Efficiency (miles per gallon) vs Car Engine Displacement (cubic inch):')
st.image('C:\\Om Jethva\\DJSCE\\SEM 6\\ML\\carfueleffiency\\Data Visuals\\relation_mpg_displacement.png')

st.write('Car Fuel Efficiency (miles per gallon) vs Car Horsepower (hp):')
st.image('C:\\Om Jethva\\DJSCE\\SEM 6\\ML\\carfueleffiency\\Data Visuals\\relation_mpg_horsepower.png')

st.write('Car Fuel Efficiency (miles per gallon) vs Car Weight (lbs):')
st.image('C:\\Om Jethva\\DJSCE\\SEM 6\\ML\\carfueleffiency\\Data Visuals\\relation_mpg_weight.png')

st.header('Models:')
st.subheader('1. Linear Regression:')
st.write('Performance:')
m1 = '''
Mean Absolute Error (MAE): 2.540287015270524\n
Mean Squared Error (MSE): 10.175162530636072\n
R-squared Value: 0.8076704419810162\n
Accuracy: 0.8076704419810162\n
'''
st.write(m1)

st.subheader('2. Random Forest Regressor:')
st.write('Performance:')
m2 = '''
Mean Absolute Error (MAE): 1.835788135593219\n
Mean Squared Error (MSE): 6.836110533898287\n
R-squared Value: 0.870784755172713\n
Accuracy: 0.870784755172713\n
'''
st.write(m2)