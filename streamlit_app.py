import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.title('🤖 Machine Learning App')

st.info('This is app builds a machine learning model!')

with st.expander('Data'):
  st.write('**IRIS data**')
  df = pd.read_csv('iris.csv')
  df
  
st.write('**X**')
  X_raw = df.drop('variety', axis=1)
  X_raw
