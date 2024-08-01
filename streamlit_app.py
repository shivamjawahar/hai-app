import streamlit as st
import pandas as pd

st.title('Machine Learning Project')

st.info('IRIS machine learning model!')

with st.expander('Data'):
  df = pd.read_csv('iris.csv')
  df
  
  
