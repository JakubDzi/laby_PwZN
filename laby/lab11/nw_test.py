import networkx as nx
import matplotlib.pyplot as plt

g = nx.dodecahedral_graph()
shells = [[2, 3, 4, 5, 6], [8, 1, 0, 19, 18, 17, 16, 15, 14, 7], [9, 10, 11, 12, 13]]
print(g)
subax1 = plt.subplot(111)
nx.draw(g, with_labels=False)
plt.show()
