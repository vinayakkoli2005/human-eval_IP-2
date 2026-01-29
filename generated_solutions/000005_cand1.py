n, k = map(int, input().split())
a = list(map(int, input().split()))
rails = []
for i in range(n-1):
    u, v, t = map(int, input().split())
    rails.append((u, v, t))

# compute the happiness value of each tour
tours = []
for i in range(n):
    for j in range(i+1, n):
        if (i, j) not in tours:
            tours.append((i, j))

total_happiness = 0
for tour in tours:
    happiness = 0
    train_type = None
    for i in range(tour[0], tour[1]+1):
        # check if we need to switch trains
        if a[i] > happiness or (train_type == 1 and rails[i-1][2] == 0) or (train_type == 0 and rails[i-1][2] == 1):
            happiness += a[i]
            train_type = None
        # check if we need to use a ticket
        elif train_type is not None and k > 0:
            happiness += a[i]
            k -= 1
        else:
            happiness += a[i] // 2
            train_type = 1 if a[i] % 2 == 0 else 0
    total_happiness = (total_happiness + happiness) % (10**9 + 7)

print(total_happiness)
