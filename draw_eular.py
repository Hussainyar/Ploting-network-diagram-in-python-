from networkx.algorithms.sparsifiers import _add_edge_to_spanner
import numpy as np 
import networkx as nx 
import matplotlib.pyplot as plt 
G=nx.DiGraph()
G.add_edges_from([(0,5),(5,6),(6,4),(4,5),(5,3),
(3,6),(6,2),(2,4),(4,3),(3,1),(1,4),(4,0),(0,3),(3,2),(2,0)]) 
pos=nx.spring_layout(G)

#nx.draw(G)
#plt.show()
#edges = [['A','B'],['B','C'],['B','D']]
#G = nx.Graph()
#G.add_edges_from(edges)
pos = nx.spring_layout(G)
plt.figure()    
nx.draw(G,pos,edge_color='black',width=1,linewidths=1,\
node_size=500,node_color='pink',alpha=0.9,\
labels={node:node for node in G.nodes()})
nx.draw_networkx_edge_labels(G,pos,edge_labels={(0,5):1,(5,6):2,(6,4):3,(4,5):4,(5,3):5,
(3,6):6,(6,2):7,(2,4):8,(4,3):9,(3,1):10,(1,4):11,(4,0):12,(0,3):13,(3,2):14,(2,0):15},font_color='green')
plt.axis('off')
plt.show()