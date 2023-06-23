import streamlit as st
import pickle
import pandas as pd
import sklearn
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Visualization",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title('Lung_Cancer_Visualization')

st.header('1.How data looks like after converting it into dataframe:') 
img = Image.open('1.jpeg')
st.image(img)

st.header('2.Checking for null values in our DataFrame:')
img = Image.open('2.jpeg')
st.image(img)
st.header('3.Value counts of the target variable:')
img = Image.open('3.jpeg')
st.image(img)
img = Image.open('4.jpeg')
st.header('4.HeatMap For Correlation Between the varibles')
st.image(img)
img = Image.open('5.jpeg')
st.header('5.Correlation with target variable')
st.image(img)
img = Image.open('6.jpeg')
st.header('6.Check the threshold value and remove all other columns:')
st.image(img)
img = Image.open('7.jpeg')
st.header('7.Elbow Method for KNN Classifier')
st.image(img)
img = Image.open('8.jpeg')
st.header('8.Accuracy:')
st.image(img)
