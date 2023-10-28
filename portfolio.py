import streamlit as st
import toxic_comments
from toxic_comments import home

st.title("Natalia Heine")
st.header("PORTFOLIO")

projekte = {
  "Toxic Comments Classification":toxic_comments, 
  "AutoScout24 Car Price Prediction":None}
select = st.radio("", list(projekte(keys()), horizontal=True)

if select == "Toxic Comments Classification":
    home.start()
