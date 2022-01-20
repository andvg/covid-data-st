import streamlit as st
import pandas as pd
import requests as r

url = 'https://covid-api.mmediagroup.fr/v1/cases?country=Italy'

data = r.get(url)

st.json(data)