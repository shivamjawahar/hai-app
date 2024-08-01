import streamlit as st
import pandas as pd

st.title('Machine Learning Project')

st.info('IRIS machine learning model!')

with st.expander('IRIS values'):
  df = pd.read_csv('iris.csv')
  df

  st.write('**Input data**')
  X = df.drop('variety', axis = 1)
  X
  
  st.write('**Target data**')
  y_raw = df.variety
  y_raw

with st.expander('IRIS visualization'):
  st.scatter_chart(data=df, x='sepal.length', y='sepal.width', color='variety')

