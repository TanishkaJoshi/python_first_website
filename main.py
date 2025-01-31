import streamlit as st
import pandas as pd
st.title("Welcome to the Website")
st.header("Python")
st.subheader("Java")
st.markdown("I love python")
st.code("""for i in range(1,5,1):
                print(i)
        """)
dataset=pd.read_csv("file.csv")

st.dataframe(dataset)
name=st.text_input("Enter your Name: ")
fname=st.text_input("Enter your father name :")
adr=st.text_area("Enter your Text :")
classdata=st.selectbox("Enter Your Class :",(1,2,3,4,5,6))
button=st.button("Done")
if button :
    st.markdown(f""" 
    Name : {name}
    Father : {fname}
    address : {adr}
    class : {classdata}""")