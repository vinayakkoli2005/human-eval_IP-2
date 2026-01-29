import sys

n, m, q = map(int, input().split())
matrix = [[False for _ in range(m)] for _ in range(n)]
staircases = 0

for i in range(q):
    x, y = map(int, input().split())
    if matrix[x - 1][y - 1]:
        staircases -= 1
    else:
        staircases += 1
    matrix[x - 1][y - 1] ^= True

print(staircases)
