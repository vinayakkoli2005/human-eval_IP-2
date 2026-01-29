import itertools

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def c(l, r):
    count = 0
    for i in range(l+1, r+1):
        if gcd(i, i+1) >= l:
            count += 1
    return count

def f(n, k):
    min_sum = float('inf')
    for seq in itertools.combinations(range(n+1), k):
        sum = 0
        for i in range(k-1):
            sum += c(seq[i]+1, seq[i+1])
        min_sum = min(min_sum, sum)
    return min_sum

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(f(n, k))
