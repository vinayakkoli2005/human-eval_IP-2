import sys
from collections import defaultdict

N, M = map(int, input().split())
edges = []
for _ in range(M):
    edges.append(list(map(int, input().split())))

def is_cactus(graph):
    for edge in graph:
        if len(edge) > 2:
            return False
    return True

def connected_components(graph):
    visited = set()
    components = []
    for node in graph:
        if node not in visited:
            component = []
            dfs(node, graph, visited, component)
            components.append(component)
    return components

def dfs(node, graph, visited, component):
    visited.add(node)
    component.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited, component)

def is_desert(graph):
    components = connected_components(graph)
    for component in components:
        if not is_cactus(component):
            return False
    return True

count = 0
for i in range(M):
    subgraph = defaultdict(list)
    for j in range(i, M):
        subgraph[edges[j][0]].append(edges[j][1])
        subgraph[edges[j][1]].append(edges[j][0])
    if is_desert(subgraph):
        count += 1
print(count)
