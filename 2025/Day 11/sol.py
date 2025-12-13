import networkx as nx
from sys import stdin
from functools import cache

G = nx.DiGraph()

def count_paths_between(graph, start, end):
    @cache
    def path(cur):
        if cur == end:
            return 1
        co = 0
        for n in graph.neighbors(cur):
            co += path(n)
        return co
    return path(start)

def count_paths_for_sequence(graph, sequence):
    t = 1
    for i in range(len(sequence)-1):
        c = count_paths_between(graph, sequence[i], sequence[i+1])
        t *= c
        if t == 0:
            break
    return t

for line in stdin:
    a,b = line.strip().split(':')
    for e in b.split():
        G.add_edge(a,e)
sol1 = nx.all_simple_paths(G, source="you", target="out")
sol2 = 0
seq = [("svr", "dac", "fft", "out"),("svr", "fft", "dac", "out")]
for s in seq:
    sol2 += count_paths_for_sequence(G,s)
print(len(list(sol1)))
print(sol2)