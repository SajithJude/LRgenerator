import streamlit as st


import openai
import os
import pandas as pd

openai.api_key =  os.getenv("APIKEY")

try:
    
    if st.button("generate Research Gap from Urls in table"):
        links = st.session_state['df_result']['url']
        st.write(links)
    # st.session_state['max_tries']  = st.session_state['max_tries']  -1
    # if st.session_state['max_tries'] >0:
        gap = openai.Completion.create(
        model="text-davinci-002",
        prompt="Find a research gap in the following publications :" + links,
        temperature=0.56,
        max_tokens=3600,
        top_p=1,
        frequency_penalty=0.35,
        presence_penalty=0,
        # stop=["\n"]
        )
        st.subheader("Research Gap")
        st.write(gap.choices[0].text)
        # x = str(gap.choices[0].text)
    # for link in links:

except:
    st.write("No Data, Generate some information in Fetch Information page to add data")


