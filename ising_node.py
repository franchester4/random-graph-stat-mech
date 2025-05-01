import numpy as np
# Node for Ising Graph
class IsingNode:
    def __init__(self, id):
        self.id = id
        self.spin = 1
        self.neighbors = []
    
    def add_neighbor(self, node):
        self.neighbors.append(node)

    # Flips sign according to heat bath dynamics
    def heat_bath_flip(self, T):
        p = 1 / (1 + np.exp((-2 / T) * np.sum(v.spin for v in self.neighbors)))
        if np.random.rand() < p:
            self.spin = 1
        else:
            self.spin = -1