import networkx as nx
import matplotlib.pyplot as plt
import random

def complex_contagion(graph, start, k):
    activated_nodes = set()
    activated_nodes.add(start)
    activated_nodes = activated_nodes.union(set(graph.neighbors(start)))

    time_step = 0
    prev_len = 0

    while ((len(activated_nodes) < graph.number_of_nodes()) or (time_step > 50000)):
        new_activated_nodes = set()
        for node in activated_nodes:
            neighbor_node = random.choices(list(graph.neighbors(node)))[0]

            # Check this node has enough critical mass to infect
            if len(activated_nodes.intersection(set(graph.neighbors(neighbor_node)))) >= k:
                new_activated_nodes.add(neighbor_node)

            time_step += 1

            if time_step >50000:
                break

        activated_nodes = activated_nodes.union(new_activated_nodes)

    return time_step

if __name__ == '__main__':
    n = int(input("Enter the n value: "))
    p = float(input("Enter Rewiring Probability: "))
    ring_lattice = nx.watts_strogatz_graph(n, 4, p)
    nx.draw(ring_lattice)
    plt.draw()
    plt.show()
    print(complex_contagion(ring_lattice, 0, 2))