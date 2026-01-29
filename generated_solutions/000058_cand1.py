import sys

def solve(s, n, k):
    if s >= n * k:
        return "YES"
    else:
        return "NO"

t = int(input())
for i in range(t):
    s, n, k = map(int, input().split())
    print(solve(s, n, k))
