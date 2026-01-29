for _ in range(int(input())):
    a, b, c = map(int, input().split())
    diff = abs(a*1 + b*2 + c*3 - (a+b+c)*2)
    print(diff if diff > 0 else 0)
