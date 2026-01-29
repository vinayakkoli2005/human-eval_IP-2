import sys

def solve(x, y):
    n = 2**18
    while True:
        if (n % x == y) and (n % n == 0):
            return n
        else:
            n += 1

for _ in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    print(solve(x, y))
