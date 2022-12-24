import os
import openai




import streamlit as st

# st.sidebar.success("Select a demo above.")

st.markdown("# Genr8NId8")
st.markdown("## Generate your research paper in less than 5 minutes")
st.markdown("### Input the publication URLs and let A.I do the magic")
st.markdown("""
    
Click on the Fetch info option on right from the menu, 
Input the URLS of the publications that revolve around your domain,
Start with the link that is the most relevant
Once you click on the generate button click on the titles of the generated content to expand
Repeat the process with atleast 4 URLS
Once youre Finished, click on the Review table to access all the generated content together

  Ideate uses advanced A.I algorithms to quickly scan and analyze the given URL and generate clear and concise reports. 
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







# import streamlit as st
# import pandas as pd
# import graphviz
# import random

# # r = list(range(8))
# # random.shuffle(r)
# # Create a graphlib graph object
# graph = graphviz.Digraph(node_attr={'shape': 'plaintext'})

# # for index, row in st.session_state['df_result'].iterrows(): 
# #     graph.node('n', row['name'][index])
# #     # graph.node('a', row['algo'])
# #     # graph.node('r', row['ref'])
# #     # graph.node('t', row['tech'])
# row = st.session_state['df_result']['name']

# def addnode(x,y):
#     return graph.node(x,y)

# list3=[]
# def addedge(a,b):
#     for i in range(len(a)):
#         h= random.choice(a)
#         o= random.choice(b)
#         string=h+o
#         list3.append(string)
#     # output = [x+y for x in h for y in o]
#     # print(output)
#     return graph.edges(list3)

# list1 = ['A','B','C','D']
# list2 = ['q','w','e','r']


# lst = ['A','B','C','D','q','w','e','r']
# random.shuffle(lst)
# for i in range(len(list1)):
#     addnode(str(lst[i]), row[i])
#     addnode(str(list2[i]), row['name'])

# # for index, row in st.session_state['df_result'].iterrows(): 
# #     addnode(str(list2[i]), row['name'])

# # for i in range(4):
# #     addedge(list1,list2)



# # graph.node('A', row[0])
# # graph.node('B', row[1])
# # graph.node('C', row[2])
# # graph.node('D', row[3])


# # tech = st.session_state['df_result']['tech']
# # graph.node('q', tech[0])
# # graph.node('w', tech[1])
# # graph.node('e', tech[2])
# # graph.node('r', tech[3])

# # for index, dfe in st.session_state['df_result'].iterrows(): 
# #     graph.node('a', dfe['algo'])


# # graph.edges(['Aa','Ba','Ca','Da','qA','wA','eC','Da','AD','AR'])
# # graph.node('a', row[4])
#     # graph.node('r', row['re'])


    
# # graph.edge(row['name'], row['tech'])
#     # graph.edges(['na','nt','at'])
# # graph.edges(row['tech'], row['algo'])



# # graph.edge('run', 'intr')
# # graph.edge('intr', 'runbl')
# # graph.edge('runbl', 'run')
# # graph.edge('run', 'kernel')
# # graph.edge('kernel', 'zombie')
# # graph.edge('kernel', 'sleep')
# # graph.edge('kernel', 'runmem')
# # graph.edge('sleep', 'swap')
# # graph.edge('swap', 'runswap')
# # graph.edge('runswap', 'new')
# # graph.edge('runswap', 'runmem')
# # graph.edge('new', 'runmem')
# # graph.edge('sleep', 'runmem')

# st.graphviz_chart(graph,use_container_width=True)

# try:
#     st.table(st.session_state['df_result'])
# except:
#     st.write("No Data, Generate some information in Fetch Information page to add data")