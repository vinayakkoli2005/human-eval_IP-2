import sys

def solve(n):
    level = [[int(x) for x in input().split()] for _ in range(n)]
    if level[0][0] == 1 or level[1][n-1] == 1:
        return "NO"
    for i in range(2, n):
        if level[1][i] == 1:
            return "NO"
    for i in range(2, n):
        if level[i][n-1] == 1:
            return "NO"
    return "YES"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(solve(n))
