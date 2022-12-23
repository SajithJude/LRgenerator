import os
import openai
import streamlit as st





def main():

    st.title("LR generator")
    # num =   st.slider("how many questions do you want to generate ?",min_value=6,max_value=30)

    


if __name__ == "__main__":
    openai.api_key =  os.getenv("OPENAI_API_KEY")

    main()