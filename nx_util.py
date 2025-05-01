import networkx as nx
import numpy as np
from ising_node import IsingNode
from ising_graph import IsingGraph

class GraphUtil:
    def __init__(self):
        pass
    
    def nx_to_ising_graph(self, G):
        """
        Convert a NetworkX graph to an IsingGraph.
        """
        ising_graph = IsingGraph(G.number_of_nodes())        
        ising_graph.set_edges(nx.to_edgelist(G), directed=False)

        return ising_graph