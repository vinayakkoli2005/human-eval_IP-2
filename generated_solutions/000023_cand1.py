n, m = map(int, input().split())
x, y = zip(*[map(int, input().split()) for _ in range(n)])
ops = [tuple(map(int, input().split())) for _ in range(m)]

trains = {i: 0 for i in range(1, n+1)}
maintenance = {}

for op, k in ops:
    if op == 1:
        trains[k] += 1
        maintenance[k] = y[k-1]
    else:
        trains[k] -= 1
        if k in maintenance:
            del maintenance[k]

for i in range(m):
    print(sum(trains.values()) - sum(maintenance.values()))
