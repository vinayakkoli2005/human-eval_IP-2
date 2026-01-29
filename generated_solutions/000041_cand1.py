import sys

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    q = int(input())
    queries = []
    for _ in range(q):
        a, b = map(int, input().split())
        queries.append([a, b])
    even_edges = set()
    for query in queries:
        path = []
        node = query[0]
        while node != query[1]:
            path.append(node)
            node = graph[node][0] if node in graph else None
        if not path:
            continue
        for i in range(len(path)-1):
            edge = (path[i], path[i+1])
            if edge in even_edges:
                continue
            elif edge[0]*edge[1]%2 == 0:
                even_edges.add(edge)
            else:
                break
        else:
            print("YES")
            for query in queries:
                path = []
                node = query[0]
                while node != query[1]:
                    path.append(node)
                    node = graph[node][0] if node in graph else None
                print(len(path))
                print(*path, sep=" ")
            return
    print("NO")
    print(q+2)

if __name__ == "__main__":
    main()
