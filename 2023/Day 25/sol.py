from sys import stdin
import networkx as nx
import random
import matplotlib.pyplot as plt  # Visualization -> find the 3 wires

lines = [i.strip() for i in stdin.read().splitlines()]
G = nx.Graph()

forbidden = [("hcf","lhn"),("lhn","hcf"),("ldl","fpg"),("fpg","ldl"),("nxk","dfk"),("dfk","nxk")]

nodes = set()
edges = set()
for line in lines:
    part = line.split(':')
    nodes.add(part[0])
    for x in part[1].strip().split(' '):
        nodes.add(x)
    for a in part[1].strip().split(' '):
        if (part[0], a) not in forbidden:
            edges.add((part[0], a))

G.add_nodes_from(list(nodes))
G.add_edges_from(list(edges))
"""
pos = nx.spring_layout(G)  # Define a layout for better visualization
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue')
plt.show()
"""
connected_components = list(nx.connected_components(G))
solution = len(connected_components[0]) * len(connected_components[1])
print("Part 1:",solution)

