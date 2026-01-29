import math

# Read input
n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
q = int(input())
finalists = []
for _ in range(q):
    dx, dy, k = map(int, input().split())
    finalists.append((dx, dy, k))

# Calculate distance between bubbles
distances = []
for i in range(n):
    for j in range(i+1, n):
        distances.append(math.sqrt((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2))

# Sort bubbles by distance
sorted_bubbles = sorted(range(n), key=lambda k: distances[k])

# Calculate the last bubble popped for each finalist
last_bubble = []
for finalist in finalists:
    dx, dy, k = finalist
    x, y = 0, 0
    for i in range(n):
        if distances[i] > 0:
            distances[i] -= 1
        else:
            x += points[i][0] * (distances[i] + 1)
            y += points[i][1] * (distances[i] + 1)
    last_bubble.append(sorted_bubbles.index((x//k, y//k)))

# Print the answer
for finalist in range(q):
    print(last_bubble[finalist]+1)
