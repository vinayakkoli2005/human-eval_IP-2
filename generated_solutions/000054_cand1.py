import sys

t = int(input())
for _ in range(t):
    n, c = input().split()
    n = int(n)
    s = input()
    
    x_set = []
    for i in range(1, n + 1):
        if i % 2 != 0 and i % 3 != 0:
            x_set.append(i)
    
    m = len(x_set)
    print(m)
    print(*x_set, sep=' ')
