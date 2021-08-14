import networkx as nx
import matplotlib.pyplot as plt
from netgraph import Graph, InteractiveGraph
import numpy as np

# DG = nx.DiGraph()
# DG.add_weighted_edges_from([(1, 2, 20), (2, 1, 0.75), (3,1,0.6), (8,9, 100)])

Graph([(0, 1), (1, 2), (2, 0)],
      edge_color={(0, 1) : 'g', (1, 2) : 'lightblue', (2, 0) : np.array([1, 0, 0])},
      node_size={0 : 20, 1 : 4.2, 2 : np.pi},
)


plt.show()
