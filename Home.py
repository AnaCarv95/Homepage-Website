import streamlit as st
import pandas

st.set_page_config(layout="wide")

empty_col1, col1, col2, empty_col2 = st.columns([1,1.5,1.5,1])

with col1:
    st.image("images/photo.jpeg",width=400)

with col2:
    st.title("Ana Carvajal Peraza")
    content = """
    Biochemist with research experience since 2017, holding a Master’s degree from CIAD, A.C. Mazatlán and currently 
    pursuing a PhD. I’ve contributed to diverse projects in genomics, conservation, and sustainable agriculture, 
    including collaborations with ICMyL-UNAM, Pronatura Noroeste, and Conselva. Skilled in remote work and teaching, 
    I’m now seeking flexible opportunities where I can apply my adaptability, commitment to excellence, and continuous 
    learning mindset.
    """
    st.info(content)

content2 = """ Greetings! these are some of the apps I have developed in Python. And  in the next page you have a form to contact me 
"""
st.subheader(content2)

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])
df = pandas.read_csv("data.csv")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
