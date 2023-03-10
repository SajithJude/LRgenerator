import streamlit as st


import openai
import os
import pandas as pd
# st.write(st.experimental_user)
# ADMIN_USERS = {
#     'judesajith.aj@gmail.com',
#     'person2@email.com',
#     'person3@email.com'
# }
# if :
# data = {'url': [''], 'algo':['']}
df = pd.DataFrame(columns=['name','url', 'algo','contrib','LR','ref','tech'])
# st.text("#adjust the slider  to fine tune the number of questions you want in the output")
if "df_result" not in st.session_state:
    st.session_state['df_result'] = df

# def add(url,x):
    


# if st.experimental_user.email in ADMIN_USERS:
#     max = 10000
# else:
max = 5

if "max_tries" not in st.session_state:
    st.session_state['max_tries'] = max
if  st.session_state['max_tries'] >0:
    st.caption("You have "+str(st.session_state['max_tries']-1)+ " free clicks left")
else:
    st.caption("You have Finished your free Trial")


url1= st.text_input("enter the url of the research paper")

openai.api_key =  os.getenv("APIKEY")

if st.button("generate and add to table") and len(url1)>0:
    st.session_state['max_tries']  = st.session_state['max_tries']  -1
    if st.session_state['max_tries'] >0:
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
        # st.subheader("Älgorithms")
        with st.expander("View Algorithms used in publication"):

            st.write(response.choices[0].text)
        x = str(response.choices[0].text)

        nam = openai.Completion.create(
        model="text-davinci-002",
        prompt="Generate a short name with less than 4 words for this publication :" + url1  +" (include only the name in response).",
        temperature=0.56,
        max_tokens=3600,
        top_p=1,
        frequency_penalty=0.35,
        presence_penalty=0,
        # stop=["\n"]
        )
        # st.subheader("Älgorithms")
        # with st.expander("View Algorithms used in publication"):

        #     st.write(nam.choices[0].text)
        nx = str(nam.choices[0].text)

        contrib = openai.Completion.create(
        model="text-davinci-002",
        prompt="what is the novel contribution by the author in this publication :" + url1  +" .",
        temperature=0.56,
        max_tokens=3600,
        top_p=1,
        frequency_penalty=0.35,
        presence_penalty=0,
        # stop=["\n"]
        )
        # st.subheader("Novel Contribution")
        with st.expander("View Novel contribution proposed in the publication"):

            st.write(contrib.choices[0].text)
        cx = str(contrib.choices[0].text)


        lrd = openai.Completion.create(
        model="text-davinci-002",
        prompt="Generate information for literature review around the novel contribution from this publication :" + url1  +" .",
        temperature=0.56,
        max_tokens=3600,
        top_p=1,
        frequency_penalty=0.35,
        presence_penalty=0,
        # stop=["\n"]
        )
        # st.subheader("Literature Review on Novel Contribution")
        with st.expander("View Literature Review about Novel Contribution"):
        
            st.write(lrd.choices[0].text)
        lx = str(lrd.choices[0].text)
        # st.write(response)

        ref = openai.Completion.create(
        model="text-davinci-002",
        prompt="Generate reference in havard format for this publication :" + url1  +" .",
        temperature=0.56,
        max_tokens=3600,
        top_p=1,
        frequency_penalty=0.35,
        presence_penalty=0,
        # stop=["\n"]
        )
        # st.subheader("Havard Reference")
        with st.expander("View Citation (Havard Format)"):
            st.write(ref.choices[0].text)
        rx = str(ref.choices[0].text)

        tech = openai.Completion.create(
        model="text-davinci-002",
        prompt="What are the tools and technologies used this publication :" + url1  +"(include only short points in response) .",
        temperature=0.56,
        max_tokens=3600,
        top_p=1,
        frequency_penalty=0.35,
        presence_penalty=0,
        # stop=["\n"]
        )
        # st.subheader("Tools and Technologies")
        with st.expander("View Tools and Technologies Used"):

            st.write(tech.choices[0].text)
        tx = str(tech.choices[0].text)

        
        df_addrow = pd.DataFrame([[nx,url1,x,cx,lx,rx,tx]], columns=['name','url', 'algo','contrib','LR','ref','tech'])
        st.session_state['df_result'] = st.session_state['df_result'].append(df_addrow, ignore_index=True)
    else:
        st.header("You have finished your Free trial, Click on the Research Gap & Questions menu for the cool part.")


st.subheader("You can acccess the generated information in the table shown bellow ")
st.session_state['df_result']

    # df['url'].append(url1)
    # df['algo'] = str(response.choices[0].text)
# @st.cache
# st.table(st.session_state['df_result'])
