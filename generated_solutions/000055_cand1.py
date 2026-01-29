import sys
input = sys.stdin.read()
n = int(input)
m = int(input)
max_imposters = []
for i in range(n):
    max_imposters.append(0)
for i in range(m):
    a, b, c = input().split()
    a, b = int(a), int(b)
    if a == 1:
        if c == "imposter":
            max_imposters[b - 2] += 1
        else:
            max_imposters[b - 2] -= 1
    elif b == 1:
        if c == "imposter":
            max_imposters[a - 2] += 1
        else:
            max_imposters[a - 2] -= 1
    else:
        continue
for i in range(n):
    if max_imposters[i] > 0:
        print("-1")
        break
else:
    print(max(max_imposters))
