import numpy as np
from ising_node import IsingNode

# Graph for running Ising model simulations
class IsingGraph:
    def __init__(self, N):
        self.nodes = [IsingNode(i) for i in range(N)]
        self.N = N
    
    def set_edges(self, edge_list, directed=False): # assume list of (v1, v2)
        for e in edge_list:
            self.nodes[e[0]].add_neighbor(self.nodes[e[1]])
            if not directed:
                self.nodes[e[1]].add_neighbor(self.nodes[e[0]])

    def magnetization(self):
        return sum(node.spin for node in self.nodes) / self.N
    
    def susceptibility(self):
        return np.var([node.spin for node in self.nodes]) / self.N
    
    # Reset all spins to 1
    def align(self):
        for node in self.nodes:
            node.spin = 1