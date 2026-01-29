import sys

def solve(n, a):
    # find the longest increasing subsequence of lengths k
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j]:
                lis[i] = max(lis[i], lis[j] + 1)

    # find the maximum value of k such that the sum of the segments is strictly increasing
    max_k = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += a[j]
            if sum > max_k:
                max_k = sum

    return max_k

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(n, a))

if __name__ == "__main__":
    main()
