import streamlit as st

st.title('🤖 Machine Learning App')

st.info('This is app builds a machine learning model!')

with st.expander('Data'):
  st.write('**IRIS data**')
  df = pd.read_csv('iris.csv')
  df
  
  
