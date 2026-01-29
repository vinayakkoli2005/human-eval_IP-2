import sys

def solve(n, a):
    # Sort the array in non-decreasing order using cyclic shifts of any segment
    k = 0
    while True:
        is_sorted = True
        for i in range(1, n):
            if a[i-1] > a[i]:
                is_sorted = False
                break
        if is_sorted:
            return k
        else:
            # Find the first unsorted element
            for i in range(n):
                if a[i] > a[i-1]:
                    l = i
                    r = i+1
                    d = r - l
                    break
            # Perform a cyclic shift of the segment [l, r) by d to the left
            temp = a[l:r]
            for j in range(d):
                a[l+j] = temp[(j+1)%len(temp)]
            k += 1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        k = solve(n, a)
        print(k)
        for i in range(k):
            l, r, d = map(int, input().split())
            print(l, r, d)
