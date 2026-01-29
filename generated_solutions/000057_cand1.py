import itertools
from math import factorial

# read input
k = int(input())
n = int(input())
edges = []
for i in range(n):
    v, s = input().split()
    edges.append((int(v), s))

# calculate number of good colorings
num_good_colorings = 0
for c in itertools.combinations(range(1<<k), k-1):
    if is_good_coloring(c, edges):
        num_good_colorings += 1

# print answer modulo 10^9+7
print(num_good_colorings % (10**9 + 7))

def is_good_coloring(c, edges):
    # check that all edges have colors that are neighboring sides in the Rubik's cube
    for i, j in edges:
        if not is_neighboring_colors(c[i], c[j]):
            return False
    return True

def is_neighboring_colors(ci, cj):
    # check that ci and cj are neighboring colors in the Rubik's cube
    if ci == 0:
        return cj in (1, 3)
    elif ci == 1:
        return cj in (2, 3)
    elif ci == 2:
        return cj in (0, 1)
    elif ci == 3:
        return cj in (0, 2)
    else:
        return False

# calculate number of ways to color the nodes
num_ways = factorial(2**k - 1) // factorial(k-1) // factorial(n)

# print answer modulo 10^9+7
print(num_good_colorings * num_ways % (10**9 + 7))
