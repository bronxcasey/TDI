## Drug-chemical interaction network
## TDI Interview 2020

import networkx as nx
import matplotlib.pyplot as plt
import csv
import collections
import numpy as np
import pandas as pd
from networkx import bipartite

###################
#Makes degree histogram
def grapher(G):
	degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
	# print "Degree sequence", degree_sequence
	degreeCount = collections.Counter(degree_sequence)
	deg, cnt = zip(*degreeCount.items())

	fig, ax = plt.subplots()
	plt.bar(deg, cnt, width=0.80, color='b')

	plt.title("Degree Histogram")
	plt.ylabel("Count")
	plt.xlabel("Degree")
	
# log-log option
	# ax.set_xscale("log")
	# ax.set_yscale("log")

	ax.set_xticks([d + 0.1 for d in deg])
	ax.set_xticklabels(deg)
	plt.show()
    

p = nx.read_edgelist('DCh-Miner_miner-disease-chemical.tsv')
