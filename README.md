# [TODO]: Clean notebooks
# PHYS 1600 Final Project
This project extends the Ising model to general, undirected graphs. We apply the same heat-bath dynamics to simulate spin-spin interactions. The graphs are generated randomly, with each simulation focusing on a different graph-theoretic quantifier related to the connectivity of the graph. 

We explore the relation between the connectivity and the critical temperature at which alignment occurs, along with whether or not certain classes of graphs can fall under the Ising universality class.

## Repo Structure
The folder `simulation` contains the simulations for each of the 3 properties explored in this project. The notebook `triangular_lattice` was used to verify correctness of the simulation framework by comparing with the results from [Lipowski et al](https://arxiv.org/pdf/1510.00423).

In the main directory, we have several utility functions used for the simulations:
- `ising_graph` defines the IsingGraph class, which keeps track of spin state
- `ising_node` are the nodes of the IsingGraph class, which maintain their own state and have internal state switching functions according to certain dynamics
- `ising_magnetic` simulates the magnetization of a fully spin aligned graph
- `nx_util` is used to convert from `networkx` graphs to our custom `IsingGraph` object.
