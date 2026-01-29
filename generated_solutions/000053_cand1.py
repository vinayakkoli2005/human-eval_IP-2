import math

def solve(n, k):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (pow(n-1,k) + pow(n-1,k-1)) % (10**9 + 7)

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    print((solve(n, k) % (10**9 + 7)))
