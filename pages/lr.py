import streamlit as st


import openai
import os
import pandas as pd

data = {'url': [''], 'algo':['']}
df = pd.DataFrame(data)
# st.text("#adjust the slider  to fine tune the number of questions you want in the output")
# state = st.State() 

# If the state object is empty, add the starting dataframe
if 'state' not in st.session_state:
    st.session_state.state = df

def add(url,x):
    df_addrow = pd.DataFrame([[url1, x]], columns=['url','algo'])
    st.session_state.state = st.session_state.append(df_addrow, ignore_index=True)
    return st.session_state.state



if st.button("Analyze"):

    url1= st.text_input("enter the url of the research paper")

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
    x = str(response.choices[0].text)
    # st.write(response)

    if st.button("add"):
        c = add(url1,x)



    # df['url'].append(url1)
    # df['algo'] = str(response.choices[0].text)

st.write(st.session_state.state)

