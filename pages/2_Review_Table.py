import streamlit as st
# import pandas

# df = pd.DataFrame(columns=['url', 'algo','contrib','LR','ref','tech'])
# st.text("#adjust the slider  to fine tune the number of questions you want in the output")
# if "df_result" not in st.session_state:
#         st.session_state['df_result'] = df
  
try:
    st.table(st.session_state['df_result'])
except:
    st.write("No Data, Generate some information in Fetch Information page to add data")