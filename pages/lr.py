import streamlit as st


import openai
import os
import pandas as pd

# data = {'url': [''], 'algo':['']}
df = pd.DataFrame(columns=['Column1', 'Column2'])
# st.text("#adjust the slider  to fine tune the number of questions you want in the output")
state = st.session_state.df

# If the state object is empty, add the starting dataframe
if state is None:
    state.df = df

# def add(url,x):
    




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
    df_addrow = pd.DataFrame([[url1, x]], columns=['url','algo'])
    state.df = state.df.append(df_addrow, ignore_index=True)



    # df['url'].append(url1)
    # df['algo'] = str(response.choices[0].text)

st.write(state.df)

