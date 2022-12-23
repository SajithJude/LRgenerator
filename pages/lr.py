import streamlit as st


import openai
import os
import pandas as pd

data = {'url': [''], 'algo':['']}
df = pd.DataFrame(data)
# st.text("#adjust the slider  to fine tune the number of questions you want in the output")

url1= st.text_input("enter the url of the research paper")



if st.button("Analyze"):


    openai.api_key =  os.getenv("APIKEY")


    response = openai.Completion.create(
    model="text-davinci-002",
    prompt="what are the algorithms used in this publication :" + url1  +" .",
    temperature=0.56,
    max_tokens=3600,
    top_p=1,
    frequency_penalty=0.35,
    presence_penalty=0,
    # stop=["\n"]
    )
    st.write(response.choices[0].text)
    # st.write(response)

    add = st.button("add result")
    if add:
        df['url'] = url1
        df['algo'] = str(response.choices[0].text)

    st.write(df)
