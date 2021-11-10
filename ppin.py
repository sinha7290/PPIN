import networkx as nx
import numpy as np
import itertools
import collections
A=nx.Graph()
A=nx.read_edgelist("hppin.txt")
f3 = open("13_14.txt","r")
B=[]
for line in f3:
	for word in line.split():
		B.append(word)
f3.close() 
C= itertools.combinations(B, 2)
D=[]
for i in C:
	D.append(i)
f = open('edge_list.txt','w')
for node_set in D:
	SP=nx.shortest_path(A, source=node_set[0], target=node_set[1])
	route_edges = [(SP[n],SP[n+1]) for n in range(len(SP)-1)]
	for e in route_edges:
		f.write('%s\t%s\n'%(e[0],e[1]))
f.close()
#ST=nx.read_edgelist("edge_list.txt")
#f1 = open('MST_edge_list.txt','w')
#MST=nx.minimum_spanning_edges(ST, data=False)
#for j in MST:
#	f1.write('%s\t%s\n'%(j[0],j[1]))
#f1.close()
f2 = open('node_list_sp.txt','w')
#f3 = open('node_list_mst.txt','w')
G=nx.read_edgelist("edge_list.txt")
for i in G.nodes():
	f2.write('%s\n'%(i))
f2.close()
#H=nx.read_edgelist("MST_edge_list.txt")
#for j in H.nodes():
#	f3.write('%s\n'%(j))	
#f3.close()

