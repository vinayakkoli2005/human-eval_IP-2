import sys

n = int(input())
p = list(map(int, input().split()))

queries = []
for _ in range(2*n):
    queries.append(list(map(int, input().split())))

results = []
for query in queries:
    s = [i + j for i, j in zip(p, query)]
    k = min([j for j, x in enumerate(s) if s.count(x) > 1])
    results.append(k if k != 0 else 0)

print('!', *p)
for result in results:
    print(result)
