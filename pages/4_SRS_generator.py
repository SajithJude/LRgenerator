import streamlit as st


import openai
import os
import pandas as pd

openai.api_key =  os.getenv("APIKEY")

try:
    links = st.text_area("Describe how will your software will be used by an end user", placeholder="Eg: An app that enables the users to...")
    if st.button("generate SRS"):
        # link = st.session_state['df_result']['url']
        # links = ', '.join(link.tolist())
        # st.write(links)
    # st.session_state['max_tries']  = st.session_state['max_tries']  -1
    # if st.session_state['max_tries'] >0:
        fr = openai.Completion.create(
        model="text-davinci-002",
        prompt="Generate 10 Functional Requirements for the software that does the following :" + links,
        temperature=0.86,
        max_tokens=3600,
        top_p=1,
        frequency_penalty=0.35,
        presence_penalty=0,
        # stop=["\n"]
        )
        # st.subheader("/")
        with st.expander("View Functional Requirements"):
            st.write(fr.choices[0].text)

        nfr = openai.Completion.create(
        model="text-davinci-002",
        prompt="Generate 10 Non-Functional Requirements for the software that does the following :" + links,
        temperature=0.86,
        max_tokens=3600,
        top_p=1,
        frequency_penalty=0.35,
        presence_penalty=0,
        # stop=["\n"]
        )
        # st.subheader("Research nfr")
        with st.expander("View Non-Functional Requirements"):
            st.write(nfr.choices[0].text)

        sthl = openai.Completion.create(
        model="text-davinci-002",
        prompt="List down and Generate information about the stakeholders and their roles individually for a software that does the following :" + links,
        temperature=0.86,
        max_tokens=3600,
        top_p=1,
        frequency_penalty=0.35,
        presence_penalty=0,
        # stop=["\n"]
        )
        # st.subheader("Research sthl")
        # st.subheader("Stakeholders information")
        with st.expander("View Stakeholders Information"):

            st.write(sthl.choices[0].text)
        # x = str(gap.choices[0].text)
    # for link in links:

except:
    st.write("An Error occurred")


