import sys

n = int(input())
a = list(map(int, input().split()))

# Initialize the result list and the current sum
result = []
current_sum = 0

for i in range(n):
    # If the current sum is equal to x, add it to the result list
    if current_sum == a[i]:
        result.append(a[i])
    
    # Increment the current sum by the element at the current index
    current_sum += a[i]
    
# Print the number of found x values and the found x values in increasing order
print(len(result))
print(*result, sep=" ")
