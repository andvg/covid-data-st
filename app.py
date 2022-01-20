import streamlit as st
import pandas as pd
import requests as r
import json

url = 'https://covid-api.mmediagroup.fr/v1/cases?country=Italy'

resp = r.get(url)

data = resp.json()
for i in data:
    st.write(i)

df = pd.dataframe(resp)
st.dataframe(df)