from ising_graph import IsingGraph, IsingNode
import numpy as np
def ising(graph,T,num_steps, reset=False):
    """ Runs Metropolis algorithm on Ising Graph
    Returns average magnetization over num_steps time steps.

    Based on code from class

    Args:
        graph       : IsingGraph
        T           : Temperature
        num_steps   : Number of time steps
    """
    if reset:
        graph.align()
    # strt = graph.magnetization()
    total = graph.magnetization()

    for _ in range(1, num_steps):
        for _ in range(graph.N):
            # pick random number in range(N)
            i = np.random.randint(0, graph.N)
            node = graph.nodes[i]
            node.heat_bath_flip(T)
        # Update magnetization
        total += graph.magnetization()
    return total / num_steps