import streamlit as st
import pandas

#st.set_page_config(layout="wide")

st.title("The Best Company")
st.text("Una compañía es una entidad legal que representa una asociación de personas, ya sean naturales, jurídicas o una combinación de ambas, con un objetivo específico y común.")
st.header("Our Team")

col1, col2, col3 = st.columns(3)

content = pandas.read_csv("Companywebsite/data.csv")

with col1:
    for index, row in content[:4].iterrows():
        st.header(f"{row["first name"].title()} {row["last name"].title()}")
        st.text(row["role"])
        st.image("Companywebsite/images/" + row["image"])

with col2:
    for index, row in content[4:8].iterrows():
        st.header(f"{row["first name"].title()} {row["last name"].title()}")
        st.text(row["role"])
        st.image("Companywebsite/images/" + row["image"])


with col3:
    for index, row in content[8:12].iterrows():
        st.header(f"{row["first name"].title()} {row["last name"].title()}")
        st.text(row["role"])
        st.image("Companywebsite/images/" + row["image"])