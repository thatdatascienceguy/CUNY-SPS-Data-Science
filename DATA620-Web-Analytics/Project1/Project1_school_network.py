# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 20:44:14 2018

@author: Jonathan Hernandez

This project is looking at a graph of primary school data.
It contains a network of contacts between children and teachers used in a 
publication of infectious Deseases. A node between people means there was
contact/interaction between them. The edge weight is the time duration the 
interaction was taking place. There are other attributes such as classname and gender.

I will look and compare the degree and eigenvector centrality between the nodes.
I will then group the nodes and their centralities by gender and plot the 
degree/eigenvector centralities histogram distribution. Finally I will perform a
2-sample t-test between genders and see if there is any difference in their means.

Data was extracted from:
http://www.sociopatterns.org/datasets/primary-school-temporal-network-data/

Citation:

Mitigation of infectious disease at school: targeted class closure vs school closure,
BMC Infectious Diseases 14:695 (2014)

High-Resolution Measurements of Face-to-Face Contact Patterns in a Primary School,
PLOS ONE 6(8): e23176 (2011)

Collaboration doene with SocioPatterns: http://www.sociopatterns.org/
"""

import pandas as pd
import networkx as nx
import matplotlib.pylab as pyplot
import scipy.stats

# read in the dataset
school = pd.read_csv('primaryschool.csv', delimiter = '\t', header=None,
                     names=['timestamp','node_from', 'node_to', 'classname_from',
                              'classname_to'])

# built the graph from the pandas dataset school
G = nx.from_pandas_edgelist(school, 'node_from', 'node_to', 'timestamp')

# print stats
print("Number of Nodes: " + str(nx.number_of_nodes(G)))
print("Number of Edges: " + str(nx.number_of_edges(G)))

# print out diameter and density of the graph
print("Density: " + str(nx.density(G)))
print("Diameter: " + str(nx.diameter(G)))

deg_centrality = nx.degree_centrality(G) # compute degree centrality for each node
eigen_centrality = nx.eigenvector_centrality(G) # compute eigenvector centrality for each node

# take the degree centrality and make it into it's own dataset
deg_centrality = pd.DataFrame.from_dict(deg_centrality, orient = 'index').rename(columns={0: 'degree_centrality'})
# since we had to use orient as index for the row indicies, make a column out of the nodes (row indicies)
deg_centrality['node'] = deg_centrality.index
# drop the row indicies
deg_centrality.reset_index(drop=True, inplace=True)
# sort by node id this will be easier to import the classnames for analysis
deg_centrality = deg_centrality.sort_values(by=['node'])

# Do the same for the eigenvector centrality

eigen_centrality = pd.DataFrame.from_dict(eigen_centrality, orient = 'index').rename(columns={0: 'eigenvector_centrality'})
# since we had to use orient as index for the row indicies, make a column out of the nodes (row indicies)
eigen_centrality['node'] = eigen_centrality.index
# drop the row indicies
eigen_centrality.reset_index(drop=True, inplace=True)
# sort by node id so this way we can import the classnames and gender easily
eigen_centrality = eigen_centrality.sort_values(by=['node'])

# make the gender/classname columns for analysis and testing
# 
metadata_school = pd.read_csv('metadata.txt', delimiter = '\t', header = None,
                              names = ['node', 'classname', 'gender'])
metadata_school = metadata_school.sort_values(by=['node'])

# add the classname and gender as well (attribute in question to the centrality datasets)
deg_centrality['classname'] = metadata_school['classname']
eigen_centrality['classname'] = metadata_school['classname']
deg_centrality['gender'] = metadata_school['gender']
eigen_centrality['gender'] = metadata_school['gender']

# group based on gender (Male, Female and Unknown)
male_deg = deg_centrality[deg_centrality['gender'] == 'M']
male_eigen = eigen_centrality[eigen_centrality['gender'] == 'M']

female_deg = deg_centrality[deg_centrality['gender'] == 'F']
female_eigen = eigen_centrality[eigen_centrality['gender'] == 'F']

unknown_deg = deg_centrality[deg_centrality['gender'] == 'Unknown']
unknown_eigen = eigen_centrality[eigen_centrality['gender'] == 'Unknown']

# degree and eigenvector centralities vs gender plots
fig, axes = pyplot.subplots(nrows=2, ncols=3)
(ax1, ax2, ax3, ax4, ax5, ax6) = axes.flatten()
ax1.hist(male_deg.degree_centrality)
ax2.hist(female_deg.degree_centrality)
ax3.hist(unknown_deg.degree_centrality)
ax4.hist(male_eigen.eigenvector_centrality)
ax5.hist(female_eigen.eigenvector_centrality)
ax6.hist(unknown_eigen.eigenvector_centrality)
ax1.set_title('Male degree centrality')
ax2.set_title('Female degree centrality')
ax3.set_title('Unknown gender degree centrality')
ax4.set_title('Male eigenvector centrality')
ax5.set_title('Female eigenvector centrality')
ax6.set_title('Unknown gender eigenvector centrality')
pyplot.show()

# t testing on the male and female means for degree and eigenvector centrality
t_test_degree_centrality = scipy.stats.ttest_ind(male_deg.degree_centrality, female_deg.degree_centrality)
print("t-test results for degree centrality - p-value: " + str(round(t_test_degree_centrality.pvalue, 4)))

t_test_eigenvector_centrality = scipy.stats.ttest_ind(male_eigen.eigenvector_centrality, female_eigen.eigenvector_centrality)
print("t-test results for eigenvector centrality - p-value: " + str(round(t_test_eigenvector_centrality.pvalue, 4)))

""" We see the p-values being pretty high for both centralities across the 2
gender groups. We can say we fail to reject the null hypothesis for both cases.
The average degree centrality and eigenvector centrality for the gender groups doesn't
change much regardless of gender (Male or Female)
"""