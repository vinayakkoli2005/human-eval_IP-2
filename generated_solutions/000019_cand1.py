import sys

def solve(a, d):
    n = len(a)
    for i in range(n):
        a[i] &= a[(i + n - d) % n]
    return a.count(0)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, d = map(int, input().split())
        a = list(map(int, input().split()))
        print(solve(a, d))
