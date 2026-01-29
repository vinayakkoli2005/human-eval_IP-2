import sys

def solve(n, m, k):
    if n == 1:
        return "YES"
    elif m >= (k-1)*(n-1):
        return "NO"
    else:
        return "YES"

for _ in range(int(sys.stdin.readline())):
    n, m, k = map(int, sys.stdin.readline().split())
    print(solve(n, m, k))
