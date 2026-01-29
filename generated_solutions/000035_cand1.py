import sys

n = int(input())
a = list(map(int, input().split()))

# initialize variables
k = 0
x_values = []

# loop through each element in the array
for i in range(n):
    # get the current element and its index
    curr_element = a[i]
    curr_index = i
    
    # check if the current element is already in the x_values list
    if not any(x == curr_element for x in x_values):
        # if it's not, add it to the list and increment k
        x_values.append(curr_element)
        k += 1
    
    # loop through the remaining elements in the array
    for j in range(i+1, n):
        # get the current element and its index
        next_element = a[j]
        next_index = j
        
        # check if the bitwise XOR of the current and next elements is equal to the current element
        if curr_element ^ next_element == curr_element:
            # if it is, add the next element to the list and increment k
            x_values.append(next_element)
            k += 1
            
# sort the x_values list in increasing order
x_values.sort()

# print the number of found x values
print(k)

# print the found x values in increasing order
print(*x_values, sep=' ')
