import sys

n, k = map(int, input().split())

# Initialize a dictionary to store the colors for each edge
colors = {}

# Loop through all possible edges and assign colors based on their start and end nodes
for i in range(1, n+1):
    for j in range(i+1, n+1):
        colors[(i, j)] = 1

# Set the minimum number of colors needed to be at least k
c = max(k, len(colors))

# Initialize an array to store the coloring
coloring = [0] * (n*(n-1)//2)

# Loop through all edges and assign colors based on their start and end nodes
count = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        coloring[count] = colors[(i, j)]
        count += 1

# Output the minimum number of colors needed and the valid edge coloring
print(c)
print(*coloring, sep=' ')
