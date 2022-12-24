import streamlit as st
import pandas as pd
import graphviz


# Create a graphlib graph object
graph = graphviz.Graph()

for index, row in st.session_state['df_result'].iterrows(): 
    graph.edge(row['name'], row['ref'])
    graph.edge(row['url'], row['name'])
    graph.edge(row['algo'], row['url'])



# graph.edge('run', 'intr')
# graph.edge('intr', 'runbl')
# graph.edge('runbl', 'run')
# graph.edge('run', 'kernel')
# graph.edge('kernel', 'zombie')
# graph.edge('kernel', 'sleep')
# graph.edge('kernel', 'runmem')
# graph.edge('sleep', 'swap')
# graph.edge('swap', 'runswap')
# graph.edge('runswap', 'new')
# graph.edge('runswap', 'runmem')
# graph.edge('new', 'runmem')
# graph.edge('sleep', 'runmem')

st.graphviz_chart(graph,use_container_width=True)

try:
    st.table(st.session_state['df_result'])
except:
    st.write("No Data, Generate some information in Fetch Information page to add data")