import sys

def solve(n, a):
    b = [0] * n
    for i in range(n):
        if a[i] != 0:
            b[i] = 1 / abs(a[i])
    return b

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = solve(n, a)
        print(*b, sep=" ")
