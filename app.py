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

with open (data) as f:
    data1 = json.loads(f.read())
df = ps.json_normalize(data1)
st.dataframe(df)