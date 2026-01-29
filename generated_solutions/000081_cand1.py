import sys

def solve(a, b):
    c = a + b
    inv_count = 0
    for i in range(len(c)):
        for j in range(i+1, len(c)):
            if c[i] > c[j]:
                inv_count += 1
    return inv_count

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(solve(a, b))

if __name__ == '__main__':
    main()
