n = int(input())
a = list(map(int, input().split()))
b = input()

simple_segments = 0
for i in range(len(b)):
    if b[i] == '*':
        x = 1
    else:
        x = a[i]
    for j in range(i+1, len(b)):
        if b[j] == '*':
            x *= a[j]
        elif b[j] == '/':
            x /= a[j]
        if x % 1 == 0:
            simple_segments += 1

print(simple_segments)
