import sys

def solve(a):
    n = len(a)
    h = [1] * n
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j]:
                h[i] = max(h[i], h[j] + 1)
    return h

if __name__ == '__main__':
    input = sys.stdin.read()
    n_cases = int(input)
    for case in range(n_cases):
        n = int(input)
        a = list(map(int, input.split()))
        h = solve(a)
        xor = 0
        for i in range(len(h)):
            xor ^= h[i]
        if xor == 0:
            print("YES")
        else:
            print("NO")
