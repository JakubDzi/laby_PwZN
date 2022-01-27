import networkx as nx
import matplotlib.pyplot as plt

g = nx.read_edgelist("CA-GrQc.txt")
#g = nx.read_edgelist("oregon1_010505.txt")
degrees = [val for (node, val) in g.degree()]
plt.hist(degrees)
plt.show()
sg = [g.subgraph(c).copy() for c in nx.connected_components(g)]
i=1
for comp in sg:
    print("składowa numer",i ,"ma", comp.number_of_nodes(), "węzły/ów")
    i+=1
sgn=nx.number_connected_components(g)
print("liczba spójnych składowych:",sgn)
try:
    print("średnia najkrótsza droga:", nx.average_shortest_path_length(g))
except:
    print("nie istnieje średnia najkrótsza droga")
subax1 = plt.subplot(111)
nx.draw(g, with_labels=False)
plt.show()
