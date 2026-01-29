import math

# Read input from standard input
n, m = map(int, input().split())
grid = []
for _ in range(n+1):
    grid.append([])
    for _ in range(m+1):
        grid[_].append(0)
for i in range(n+1):
    for j in range(m+1):
        grid[i][j] = int(input())

# Calculate the sum of S(x, y) for each point (x, y)
sum_S = 0
for i in range(n+1):
    for j in range(m+1):
        if grid[i][j] == 1:
            # Find the nearest pole to (x, y) and calculate its distance
            dist = math.sqrt((i-0)**2 + (j-0)**2)
            sum_S += dist**2

# Print the sum of S(x, y) for each point (x, y)
print(sum_S)
