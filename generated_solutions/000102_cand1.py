import sys

def solve(arr, color):
    # Initialize variables
    n = len(arr)
    blue_count = 0
    red_count = 0
    permuted = False

    # Count the number of blues and reds in the array
    for i in range(n):
        if color[i] == "B":
            blue_count += 1
        elif color[i] == "R":
            red_count += 1

    # Check if the number of blues is equal to the number of reds
    if blue_count != red_count:
        return False

    # Create a copy of the original array
    new_arr = arr.copy()

    # Loop through each element in the array and check its color
    for i in range(n):
        # If the current element is blue, decrease its value by 1
        if color[i] == "B":
            new_arr[i] -= 1
        # If the current element is red, increase its value by 1
        elif color[i] == "R":
            new_arr[i] += 1

    # Check if the new array is a permutation of 1 to n
    permuted = True
    for i in range(n):
        if new_arr[i] != i + 1:
            permuted = False
            break

    return permuted

# Read input from stdin
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    color = input()

    # Check if the array is a permutation of 1 to n
    permuted = solve(arr, color)

    # Print output
    if permuted:
        print("YES")
    else:
        print("NO")
