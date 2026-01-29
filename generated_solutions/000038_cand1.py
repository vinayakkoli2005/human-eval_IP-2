import sys

def solve(n, m):
    # Create a graph with n nodes and no edges
    graph = {i: set() for i in range(1, n+1)}

    # Add edges to the graph based on the restrictions
    for i in range(m):
        a, b, c = map(int, input().split())
        if not (b in graph[a] or b in graph[c]):
            graph[a].add(b)
            graph[b].add(a)
            graph[c].add(b)
            graph[b].add(c)

    # Find a root node for the tree
    root = 1
    while len(graph[root]) > 1:
        root += 1

    # Print the edges of the tree
    print(*graph, sep="\n")
