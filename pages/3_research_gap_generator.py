import streamlit as st


import openai
import os
import pandas as pd

openai.api_key =  os.getenv("APIKEY")

try:
    links = st.session_state['df_result']['url']
    st.write(links)
except:
    st.write("No Data, Generate some information in Fetch Information page to add data")

# if st.button("generate and add to table") and len(url1)>0:
#     st.session_state['max_tries']  = st.session_state['max_tries']  -1
#     if st.session_state['max_tries'] >0:
#         response = openai.Completion.create(
#         model="text-davinci-002",
#         prompt="what are the algorithms used in this publication :" + url1  +" .",
#         temperature=0.56,
#         max_tokens=3600,
#         top_p=1,
#         frequency_penalty=0.35,
#         presence_penalty=0,
#         # stop=["\n"]
#         )
#         st.subheader("Älgorithms")
#         st.write(response.choices[0].text)
#         x = str(response.choices[0].text)

#         contrib = openai.Completion.create(
#         model="text-davinci-002",
#         prompt="what is the novel contribution by the author in this publication :" + url1  +" .",
#         temperature=0.56,
#         max_tokens=3600,
#         top_p=1,
#         frequency_penalty=0.35,
#         presence_penalty=0,
#         # stop=["\n"]
#         )
#         st.subheader("Novel Contribution")

#         st.write(contrib.choices[0].text)
#         cx = str(contrib.choices[0].text)