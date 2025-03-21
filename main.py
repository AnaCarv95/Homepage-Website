import streamlit as st

# st.set_page_config(layout="wide")

col1, col2 = st.columns (2)

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

content2 = """ Below you can find some of the apps I have built in Python. Feel free to contact me
"""
st.write(content2)