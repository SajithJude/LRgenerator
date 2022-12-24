import streamlit as st
import pandas as pd
import graphviz


# Create a graphlib graph object
graph = graphviz.Digraph(node_attr={'shape': 'plaintext'})

# for index, row in st.session_state['df_result'].iterrows(): 
#     graph.node('n', row['name'][index])
#     # graph.node('a', row['algo'])
#     # graph.node('r', row['ref'])
#     # graph.node('t', row['tech'])
row = st.session_state['df_result']['name']
graph.node('n0', row[0])
graph.node('n1', row[1])
graph.node('n2', row[2])
graph.node('n3', row[3])
# graph.node('a', row[4])
    # graph.node('r', row['re'])


    
# graph.edge(row['name'], row['tech'])
    # graph.edges(['na','nt','at'])
# graph.edges(row['tech'], row['algo'])



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