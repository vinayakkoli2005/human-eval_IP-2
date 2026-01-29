import math

def count_permutations(n):
    count = 0
    for i in range(1, n+1):
        if i*(i-1) % 2 == 0:
            count += 1
    return count

t = int(input())
for _ in range(t):
    n = int(input())
    print(count_permutations(n))
