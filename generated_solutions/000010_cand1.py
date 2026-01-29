n, m, k = map(int, input().split())
a = []
for i in range(n):
    a.append([])
    for j in range(m):
        a[i].append(list(map(int, input().split())))

c = list(map(int, input().split()))

res = []
for i in range(k):
    row = 0
    col = c[i] - 1
    while True:
        if a[row][col] == 1:
            col += 1
        elif a[row][col] == 2:
            row += 1
        else:
            break
    res.append(col + 1)

print(*res, sep='\n')
