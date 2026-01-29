import sys

def read_data():
    n, q = map(int, input().split())
    e = list(map(int, input().split()))
    roads = []
    for _ in range(n - 1):
        a, b, c, t = map(int, input().split())
        roads.append([a, b, c, t])
    groups = []
    for _ in range(q):
        v, x = map(int, input().split())
        groups.append([v, x])
    return n, e, roads, groups

def get_max_reachable(n, e, roads, group):
    visited = [0] * n
    queue = [[group[1], 0]]
    max_reachable = 0
    while queue:
        node, cost = queue.pop(0)
        if visited[node - 1]:
            continue
        visited[node - 1] = 1
        if e[node - 1] > max_reachable:
            max_reachable = e[node - 1]
        for r in roads:
            if node == r[0] or node == r[1]:
                next_node = r[0] if node == r[1] else r[1]
                queue.append([next_node, cost + r[3]])
    return max_reachable

def get_cost(n, e, roads, group):
    visited = [0] * n
    queue = [[group[1], 0]]
    cost = 0
    while queue:
        node, c = queue.pop(0)
        if visited[node - 1]:
            continue
        visited[node - 1] = 1
        cost += c
        for r in roads:
            if node == r[0] or node == r[1]:
                next_node = r[0] if node == r[1] else r[1]
                queue.append([next_node, c + r[2]])
    return cost

n, e, roads, groups = read_data()
for group in groups:
    max_reachable = get_max_reachable(n, e, roads, group)
    cost = get_cost(n, e, roads, group)
    print(f"The largest reachable enjoyment value is {max_reachable}.")
    print(f"Omkar will have to pay {cost} per vehicle.")
