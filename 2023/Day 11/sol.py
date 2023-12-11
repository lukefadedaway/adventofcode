from sys import stdin
import networkx as nx

lines = [i.strip() for i in stdin.read().splitlines()]

def distance(p1, p2):
    return abs(p2[0]-p1[0]) + abs(p2[1]-p1[1])
    
def newgalaxy(galaxy, factor, s=0):
    Xs = [0] * len(lines[0])
    Ys = [0] * len(lines)
    for i in range(len(lines[0])):
        se = []
        for y in range(len(lines)):
            se.append(lines[y][i])
        if set(se) == set('.'):
            Xs[i] += 1
    for i in range(len(lines)):
        se = set(lines[i])
        if se == set('.'):
            Ys[i] += 1
    for i in range(len(galaxy)):
        for j in range(i+1,len(galaxy),1):
            x1, x2 = sorted([galaxy[i][1],galaxy[j][1]])
            y1, y2 = sorted([galaxy[i][0],galaxy[j][0]])
            s += distance(galaxy[i],galaxy[j]) + (sum(Xs[x1+1:x2])*factor + sum(Ys[y1+1:y2])*factor)
    return s

vertices = {}
counter = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '#':
            vertices[counter] = [i,j]
            counter += 1

""" # if only this was minimum matching
leng = len(lines[0])
for i in range(leng):
    se = []
    for y in range(len(lines)):
        se.append(lines[y][i+additions])
    if set(se) == set('.'):
        for y in range(len(lines)):
            lines[y] = lines[y][:i+additions] + '.' + lines[y][i+additions:]
        additions += 1
leng = len(lines)
additions = 0
for i in range(leng):
    se = set(lines[i+additions])
    if se == set('.'):
        lines = lines[:i+additions] + [lines[i+additions]] + lines[i+additions:]
        additions += 1

vertices = {}
counter = 0
G = nx.Graph()
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '#':
            vertices[counter] = [i,j]
            counter += 1
for i in range(len(vertices)):
    for j in range(i+1,len(vertices),1):
        G.add_edge(i, j, weight=-1*distance(vertices[i],vertices[j]))
matching = nx.max_weight_matching(G, weight='weight', maxcardinality=True)
solution = -1 * sum([G[u][v]['weight'] for u, v in matching])
"""
print("Part 1:",newgalaxy(vertices, 1))
print("Part 2:",newgalaxy(vertices, 1000000-1))

