import sys

def solve(n, a):
    x = a[n-1]
    i = 0
    while i < n and a[i] <= x:
        i += 1
    if i == n:
        return 0
    else:
        return 1 + solve(i, a[:i] + a[i:])

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
