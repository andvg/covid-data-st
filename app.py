import streamlit as st
import pandas as pd
import requests as r
import json

url = 'https://covid-api.mmediagroup.fr/v1/cases?country=Italy'

resp = r.get(url)

data = resp.json()
st.json(data)
for i in data:
    st.write(i)

df = pd.DataFrame(data.items())
df = df.drop([0])
#df = df.reset_index(drop=True)

st.dataframe(df)