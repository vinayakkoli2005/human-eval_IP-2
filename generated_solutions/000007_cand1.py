import math

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = int(input())
arr = list(map(int, input().split()))
prettiness_value = sum([sum([gcd(a[i], a[j]) * gcd(i, j) for i in range(n) for j in range(n) if i != j]) % (10**9 + 7) for a in arr])
print(prettiness_value)
