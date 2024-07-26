#import streamlit as st

#st.write('hai')

import pandas as pd
import pandas_profiling
import streamlit as st

from streamlit_pandas_profiling import st_profile_report

df = pd.read_csv("iris.csv")
pr = df.profile_report()

st_profile_report(pr)