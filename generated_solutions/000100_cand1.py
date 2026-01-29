for _ in range(int(input())):
    x_0, n = map(int, input().split())
    x = x_0
    for i in range(n):
        d = i + 1
        if x % 2 == 0:
            x -= d
        else:
            x += d
    print(x)
