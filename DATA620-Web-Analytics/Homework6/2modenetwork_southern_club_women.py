# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 11:49:13 2018

@author: jonboy1987

DATA 620 Week 6 Assignment

2-mode networks regarding southern club women attending social events
"""

import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

davis = open('davis.dat.txt','ro')
lines = davis.readlines()

# grab row labels and strip out escape characters
row_labels = lines[4:22]
row_labels = [x.rstrip() for x in row_labels]

# grab column labels and strip out escape characters
column_labels = lines[23:37]
column_labels = [x.rstrip() for x in column_labels]

# grab matrix
data = lines[38:57]

# convert data to a 18 x 14 matrix for analysis
matrix = np.loadtxt(data, dtype=int)

#take the transpose of this matrix to make a adjacency matrix
matrix_t = matrix.transpose()
adj_matrix = np.matmul(matrix, matrix_t)
print "Original Dataset 2-mode network as a matrix:"
print matrix

# make a dataset out of it and add row and column labels
dataset = pd.DataFrame(data=adj_matrix, index=row_labels, columns=row_labels)
print dataset
print
# let's try to compute the sum of rows in the dataset; this will show us
# how many events have they been to amongst other people
print "Number of times each person attended a event with at least someone else:"
print dataset.sum()

# now make a graph out of this dataset
G = nx.from_pandas_adjacency(dataset)
print nx.info(G)
pos = nx.spring_layout(G)
plt.close()
plt.subplot(1,3,1)
nx.draw(G, pos, with_labels=True)
# edge weights
nx.draw_networkx_edge_labels(G, pos, edge_labels = {(u,v): d['weight'] for u,v,d in G.edges(data=True)})

# we can see that Theresa attended the most events with everyone and is connected with everyone
# 2nd place is Evelyn who also attended events with everyone

# What's most interesting is that Olivia and Flora attended same events with another person
# the fewest times but if we look at the dataset, we can see that they both attended the same 
# number of events with the same exact people, making a subgraph of these nodes are
# exactly equal
# let's make a subgraph from these two people
plt.subplot(1,3,2)
olivia = G.subgraph(G['OLIVIA'])
nx.draw(olivia, pos=pos, node_color = 'green', edge_color = 'blue', with_labels=True)
nx.draw_networkx_edge_labels(olivia, pos, 
                             edge_labels = {(u,v): d['weight'] for u,v,d in olivia.edges(data=True)})
plt.subplot(1,3,3)
flora = G.subgraph(G['FLORA'])
nx.draw(flora, pos=pos, node_color = 'purple', edge_color = 'orange', with_labels=True)
nx.draw_networkx_edge_labels(flora, pos, 
                             edge_labels = {(u,v): d['weight'] for u,v,d in flora.edges(data=True)})
                             
plt.show()