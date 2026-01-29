import math

n = int(input())
a = list(map(int, input().split()))

sum = 0
for i in range(n):
    sum += (i - a[i]) % 998244353

print((sum % 10**9 + 7) % 10**9)
