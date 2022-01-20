import streamlit as st
import pandas as pd
import requests as r
import json

url = 'https://covid-api.mmediagroup.fr/v1/cases?country=Italy'

resp = r.get(url)

data = resp.json()
st.json(data)
list = []
for i in data:
    list.append(i)
    st.write(i)

df = DataFrame(columns=(list))

st.dataframe(df)