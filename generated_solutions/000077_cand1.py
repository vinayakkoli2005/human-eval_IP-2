# Read input
n, m = map(int, input().split())
friendships = []
for _ in range(m):
    u, v = map(int, input().split())
    friendships.append((u, v))

# Build graph of friendships
graph = {}
for u, v in friendships:
    if u not in graph:
        graph[u] = []
    graph[u].append(v)
    if v not in graph:
        graph[v] = []
    graph[v].append(u)

# Find all groups of friends
groups = []
for i in range(1, n+1):
    if i not in groups:
        group = [i]
        j = i
        while j in graph and len(group) < 5:
            for k in graph[j]:
                if k not in group:
                    group.append(k)
                    break
            else:
                j = -1
        groups.append(group)

# Check if any of the groups is a successful party
for group in groups:
    if len(group) == 5:
        print(*group)
        break
else:
    print(-1)
