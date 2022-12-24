import streamlit as st


import openai
import os
import pandas as pd

openai.api_key =  os.getenv("APIKEY")

try:
    
    if st.button("generate Research Gap/Questions"):
        link = st.session_state['df_result']['url']
        links = ', '.join(link.tolist())
        st.write(links)
    # st.session_state['max_tries']  = st.session_state['max_tries']  -1
    # if st.session_state['max_tries'] >0:
        gap = openai.Completion.create(
        model="text-davinci-002",
        prompt="Generate comprehensive information on the research gap by analysing the following publications :" + links,
        temperature=0.86,
        max_tokens=3600,
        top_p=1,
        frequency_penalty=0.35,
        presence_penalty=0,
        # stop=["\n"]
        )
        
        # st.subheader("Research Gap")
        with st.expander("View Research Gap"):
            st.write(gap.choices[0].text)
        # x = str(gap.choices[0].text)
        # if st.button("generate research questions"):
            # link = st.session_state['df_result']['url']
            # links = ', '.join(link.tolist())
            # st.write(ink)
        ink = gap.choices[0].text
    # st.session_state['max_tries']  = st.session_state['max_tries']  -1
    # if st.session_state['max_tries'] >0:
        qus = openai.Completion.create(
        model="text-davinci-002",
        prompt="Generate 10 research questions for the following research gap :" + ink,
        temperature=0.86,
        max_tokens=3600,
        top_p=1,
        frequency_penalty=0.35,
        presence_penalty=0,
        # stop=["\n"]
        )
        # st.subheader("Research Questions")
        with st.expander("View Research Questions"):
            st.write(qus.choices[0].text)

        st.header("That was good start, now click on SRS Generator to spice things up a bit ")

    # for link in ink:
except:
    st.write("No Data, Generate some information in Fetch Information page to add data")


