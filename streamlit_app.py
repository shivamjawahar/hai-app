import streamlit as st
import pandas as pd

st.title('Machine Learning Project')

st.info('IRIS machine learning model!')

with st.expander('IRIS values'):
  df = pd.read_csv('iris.csv')
  df

  st.write('**X**')
  X_raw = df.drop('variety', axis=1)
  X_raw
  
  
