import streamlit as st
import pandas


st.set_page_config(layout="wide")

col1, empty_col1, col2 = st.columns([1,0.1,1])
df = pandas.read_csv("extras.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"],width=300)
        st.write(f"[Source Code]({row['url']})")

with col2:
    for index, row in df[4:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"],width=300)
        st.write(f"[Source Code]({row['url']})")
