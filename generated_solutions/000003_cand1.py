import sys
from collections import Counter

def solve(n, m, k):
    b = [a_i for _ in range(m) for a_i in range(n)]
    counter = Counter()
    for i in range(len(b)):
        if sum(b[i:i+k]) % k == 0:
            counter.update([frozenset(range(i, i+k))])
    return len(counter) % (10**9 + 7)

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    a = [int(a_i) for a_i in input().split()]
    print(solve(n, m, k))
