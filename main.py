import streamlit as st
import pandas

st.set_page_config(layout="wide")

empty_col1, col1, col2, empty_col2 = st.columns([1.5,1,1.5,1])

with col1:
    st.image("images/photo.jpeg",width=300)

with col2:
    st.title("Ana Carvajal Peraza")
    content = """
    I hold a degree in Biochemistry from Instituto Tecnológico de Mazatlán (ITMAZ) and completed my social service, professional practices, 
    and graduate studies at CIAD, A.C. Mazatlán. Since 2017, I have participated in diverse research projects, including a collaboration with 
    the Genomics Laboratory at ICMyL-UNAM (2020–2021). Following my Master’s degree, I contributed to conservation efforts with Pronatura Noroeste 
    in Bahía Santa María La Reforma and am currently part of a Conselva-led project optimizing water and agrochemical usage in crop irrigation. 
    Additionally, I’ve gained experience as a remote teacher. In 2024, I began pursuing a PhD and am now seeking remote or flexible opportunities 
    where I can apply my dedication to excellence and ability to adapt and learn quickly.
    """
    st.info(content)

content2 = """ Greetings! these are some of the apps I have developed in Python. And  in the next page you have a form to contact me 
"""
st.write(content2)

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
