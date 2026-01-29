import sys

n = int(input())
a = list(map(int, input().split()))

f = []
for i in range(n):
    if a[i] == i+1:
        f.append(1)
    else:
        f.append(0)

max_f = max(f)

print(max_f)
