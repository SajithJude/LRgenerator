import os
import openai




import streamlit as st

# st.sidebar.success("Select a demo above.")

st.markdown("# Genr8NId8")
st.markdown("## Generate your research paper in less than 5 minutes")
st.markdown("### Input the publication URL and let A.I do the magic")
st.markdown("""
    
Click on the Fetch inform, 
technologies used, algorithm/methodology used and also generates literature reviews.
 It allows users to quickly evaluate the research presented
  and identify possible research gaps without the need to manually source and read through the content. 
  It uses advanced algorithms to quickly scan and analyze the given URL and generate clear and concise reports. 
  The reports are tailored to deliver easy-to-understand summaries of the research,
   allowing users to quickly gain insights. It is useful for researchers, academics, 
   and business professionals who require quick and reliable evaluation of research content.
""")

with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("https://aeiljuispo.cloudimg.io/v7/https://s3.amazonaws.com/moonup/production/uploads/1665676037566-noauth.jpeg?w=200&h=200&f=face")

    with text_col:
        st.subheader("Crafted with ❤️ from Jude Sajith")
        st.write("""Connect with me on LinkedIn for quick replies
            """)
        st.markdown("[LinkedIn profile...]https://www.linkedin.com/in/jude-sajith/)")

# with st.container():
#     image_col, text_col = st.columns((1,2))
#     with image_col:
#         st.image("https://cdn-images-1.medium.com/max/906/1*hjhCIWGgLzOznTFwDyeIeA.png")

#     with text_col:
#         st.subheader("Rational UI Design with Streamlit")
#         st.write("""
#             From one point of view Streamlit is a retrograde step in web development because 
#             it lets you mix up the logic of your app with the way it is presented. But from 
#             another it is very much simplifying web design.""")
#         st.markdown("[Read more...](https://towardsdatascience.com/rational-ui-design-with-streamlit-61619f7a6ea4)")