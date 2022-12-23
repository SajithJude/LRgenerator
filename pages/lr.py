import streamlit as st


import openai
import os

@st.cache
def get_input_list():
  return []


st.title("Input title of the reasearch papers")
num =   st.slider("how many questions do you want to generate ?",min_value=5,max_value=30)

for i in len(num):
    user_input = st.text_input("enter the url of the research paper")
    input_list = get_input_list()
    input_list.append(user_input)
    
st.write('The list is now :', input_list)
# st.text("#adjust the slider  to fine tune the number of questions you want in the output")

url= st.text_input("enter the url of the research paper")

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