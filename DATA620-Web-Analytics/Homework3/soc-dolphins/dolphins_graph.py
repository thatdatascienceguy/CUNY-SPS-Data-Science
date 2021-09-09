# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 19:36:36 2018

@author: jonboy1987
"""

import networkx as nx
import pandas as pd

# Load a csv file containing information on dolphins and frequent association
# between them living in a community living off Doubtful Sound, New Zealand
# dolphins were labled with id's and a undirected edge between two dolphins 
# means they were frequently associated
dolphins = pd.read_csv("soc-dolphins.csv")

# make the undirected graph from a pandas dataframe
G = nx.from_pandas_edgelist(dolphins, source = 'node from', target = 'node to')

# positions of the nodes
pos = nx.spring_layout(G)

# draw graph with nodes, edges and labels positioned on the nodes
nx.draw(G, pos = nx.spring_layout(G), with_labels = True)

# write to a .gexf file to be read in using a graphing tool such as Gephi
nx.write_gexf(G, "dolphins_graph.gexf")

# print out some statistics
print "Number of nodes: ", nx.number_of_nodes(G)
print "Number of edges: ", nx.number_of_edges(G)

# diameter of a graph that is the greatest distance between any pair of nodes
print "Diameter of graph: ", nx.diameter(G)

# Examine the density of a graph that is the number of edges is close to the 
# maximum edges on a graph. Low density is a sparse graph and high density is a 
# dense graph
print "Graph Density: ", nx.density(G)

# degree histogram
print "Degree histogram: ", nx.degree_histogram(G)