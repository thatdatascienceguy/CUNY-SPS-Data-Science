# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 21:19:35 2018

@author: jonboy1987
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from collections import Counter # counting groups in the islands

# read the matrix/dataset
world_cities_global_firms = pd.read_csv("da6.csv", header=0, skiprows=1,
                                        index_col = 0)
world_cities_global_firms = world_cities_global_firms.drop('Unnamed: 47',1) # remove total offices as we'll be converting the matrix to a 1-mode matrix
firms = list(world_cities_global_firms.columns) # extract firm and map it to it's full name (make a dictionary)
# firm mapping to the type of industry
print world_cities_global_firms

# create firm mapping

data = open('da6+.net', 'ro')
lines = data.readlines()
firm_industry = {}

for i in lines[59:64]:
    firm_industry[i[5:7]] = "Accountancy"

for i in lines[65:76]:
    firm_industry[i[5:7]] = "Advertising"
    
for i in lines[77:91]:
    firm_industry[i[5:7]] = "Banking and Finance"

for i in lines[92:108]:
    firm_industry[i[5:7]] = "Law"

world_cities_adjmatrix = np.matmul(np.transpose(world_cities_global_firms),world_cities_global_firms)

"""This adjancency matrix represents the global firms and number of cities that reside in them
Nodes are global firms and an undirected edge between them means that those firms exist
in at least one world city. The edge weights represents how many cities those two nodes
are in.
"""

# take the matrix (now 1-mode) and make a dataset out of it and create a graph from it
world_cities = pd.DataFrame(data=world_cities_adjmatrix, index=firms, columns=firms)
G = nx.from_pandas_adjacency(world_cities)
print nx.info(G)

# set node attribute for each firm; attribute is the industry per firm_mapping dict
nx.set_node_attributes(G,firm_industry, 'industry')
pos = nx.spring_layout(G)
plt.close()
nx.draw(G, pos, with_labels=True)

nx.draw_networkx_edge_labels(G, pos, edge_labels = {(u,v): d['weight'] for u,v,d in G.edges(data=True)})

# island method (Per Social Network Analysis for Startups 2nd edition)
# first trim edges
def trim_edges(g, weight=1):
    g2=nx.Graph()
    for from_node, to_node, edata in g.edges(data=True):
        if edata['weight'] > weight:
            g2.add_edge(from_node,to_node,weight=edata['weight'])
    return g2


def island_method(g, iterations=5):
    weights= [edata['weight'] for f,to,edata in g.edges(data=True)]
    mn=int(min(weights))
    mx=int(max(weights))
    #compute the size of the step, so we get a reasonable step in iterations
    step=int((mx-mn)/iterations)
    return [[threshold, trim_edges(g, threshold)] for threshold in range(mn,mx,step)]

islands= island_method(G)
for i in islands:
# print the threshold level, size of the graph and number of types of firms for each one
    subgraph= G.subgraph(i[1])
    print i[0], len(i[1]), dict(Counter(nx.get_node_attributes(subgraph,'industry').values()))
    nx.draw(subgraph, pos=nx.spring_layout(subgraph), with_labels=True)
    nx.draw_networkx_edge_labels(subgraph, pos=nx.spring_layout(subgraph), edge_labels = {(u,v): d['weight'] for u,v,d in subgraph.edges(data=True)})

""" There is only one connected component and thus a strongly connected graph
Looking at the thresholds for say a weight of 127 (number of cities) we can examine
the firms that are stationed at the most cities.

We see that for any threshold of sum of weights/edges that the Law industry is always
there and popular in most world cities. For each threshold the Law nodes decrease but
have the most weight in the graph.

Accounting is also popular but for the threshold levels is the smallest component followed
by Advertising and then Banking and Finance.
"""