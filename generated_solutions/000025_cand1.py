import sys

def solve(n, m, q):
    # create a graph with n vertices and m edges
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        u, v, d = list(map(int, input().split()))
        graph[u - 1][v - 1] = d
        graph[v - 1][u - 1] = d
    
    # calculate the shortest paths from station 1 to all other stations
    distances = [float('inf') for _ in range(n)]
    queue = [(0, 1)]
    while queue:
        (d, u) = queue.pop(0)
        if d < distances[u - 1]:
            distances[u - 1] = d
            for v in range(n):
                if graph[u - 1][v] > 0 and d + graph[u - 1][v] < distances[v]:
                    queue.append((d + graph[u - 1][v], v + 1))
    
    # calculate the minimal cost of railway construction after all incidents
    total_cost = 0
    for _ in range(q):
        k, x = list(map(int, input().split()))
        total_cost += w_u * (distances[k - 1] + x)
    
    return total_cost

if __name__ == '__main__':
    n, m, q = list(map(int, sys.stdin.readline().split()))
    w_u = list(map(int, sys.stdin.readline().split()))
    for _ in range(m):
        u, v, d = list(map(int, sys.stdin.readline().split()))
        graph[u - 1][v - 1] = d
        graph[v - 1][u - 1] = d
    
    total_cost = solve(n, m, q)
    print(total_cost)
