import streamlit as st
import pandas as pd
import graphviz
import random

# r = list(range(8))
# random.shuffle(r)
# Create a graphlib graph object
graph = graphviz.Digraph(node_attr={'shape': 'plaintext'})

# for index, row in st.session_state['df_result'].iterrows(): 
#     graph.node('n', row['name'][index])
#     # graph.node('a', row['algo'])
#     # graph.node('r', row['ref'])
#     # graph.node('t', row['tech'])
row = st.session_state['df_result']['name']

def addnode(x,y):
    return graph.node(x,y)

list3=[]
def addedge(a,b):
    for i in range(len(a)):
        h= random.choice(a)
        o= random.choice(b)
        string=h+o
        list3.append(string)
    # output = [x+y for x in h for y in o]
    # print(output)
    return graph.edges(list3)

list1 = ['A','B','C','D']
list2 = ['q','w','e','r']


lst = ['A','B','C','D','q','w','e','r']
random.shuffle(lst)
for i in range(len(list1)):
    for j in range(len(list2)):
        addnode(str(list1[i]), row[j])




for i in range(4):
    addedge(list1,list2)



# graph.node('A', row[0])
# graph.node('B', row[1])
# graph.node('C', row[2])
# graph.node('D', row[3])


# tech = st.session_state['df_result']['tech']
# graph.node('q', tech[0])
# graph.node('w', tech[1])
# graph.node('e', tech[2])
# graph.node('r', tech[3])

# for index, dfe in st.session_state['df_result'].iterrows(): 
#     graph.node('a', dfe['algo'])


# graph.edges(['Aa','Ba','Ca','Da','qA','wA','eC','Da','AD','AR'])
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