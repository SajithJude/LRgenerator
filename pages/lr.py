import streamlit as st


import openai
import os

st.title("Input title of the reasearch papers")
# st.text("#adjust the slider  to fine tune the number of questions you want in the output")

url= st.text_input("enter the url of the research paper")
num =   st.slider("how many questions do you want to generate ?",min_value=6,max_value=30)

if st.button("Analyze"):


    openai.api_key =  os.getenv("OPENAI_API_KEY")


    response = openai.Completion.create(
    model="text-davinci-002",
    prompt="what are the algorithms used in this publication :" + url  +" .",
    temperature=0.56,
    max_tokens=3600,
    top_p=1,
    frequency_penalty=0.35,
    presence_penalty=0,
    # stop=["\n"]
    )
    st.write(response.choices[0].text)
    st.write(response)