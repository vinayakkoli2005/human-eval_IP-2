import sys

n = int(input())
arr = list(map(int, input().split()))

# Create a dictionary to store the sum of each pair of elements
pair_sums = {}
for i in range(n):
    for j in range(i+1, n):
        pair_sums[(arr[i], arr[j])] = 0

# Check if there is a pair of elements that sum to the elements in the output array
found = False
for i in range(n-1):
    for j in range(i+1, n):
        if arr[i] + arr[j] == arr[n-1]:
            found = True
            break
    if found:
        break

# If a pair is found, print "YES" and the input array with the indices of the elements swapped
if found:
    print("YES")
    for i in range(n):
        print(arr[i], end=" ")
else:
    print("NO")
