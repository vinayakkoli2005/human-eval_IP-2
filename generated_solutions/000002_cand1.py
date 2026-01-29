import math

n, k = map(int, input().split())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

# calculate the minimum radius of the park that contains at least k bird habitats
r = math.sqrt(max([abs(point[0]) + abs(point[1]) for point in points]))

# check if the center of the park is inside at least k bird habitats
inside_count = 0
for point in points:
    if (point[0] - r)**2 + (point[1] - r)**2 <= r**2:
        inside_count += 1
    if inside_count >= k:
        break

# output the minimum radius of the park that contains at least k bird habitats
print(r)
