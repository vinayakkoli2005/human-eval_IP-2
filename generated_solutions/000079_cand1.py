import sys

def eliminate(a, k):
    # Find the smallest element in the array
    min_val = min(a)
    
    # Initialize the result array with the smallest element
    res = [min_val] * len(a)
    
    # Iterate through the array and find the elements to eliminate
    for i in range(len(a)):
        if a[i] == min_val:
            # If the current element is the smallest, eliminate it
            res[i] = 0
        else:
            # Otherwise, subtract the smallest element from the current element
            res[i] = a[i] - min_val
    
    return res

def find_k(a):
    # Initialize the result array with the original values
    res = list(a)
    
    # Iterate through the array and eliminate elements until all are equal to 0
    while True:
        k = 1
        
        # Find the smallest element in the array
        min_val = min(res)
        
        # If all elements are equal to 0, return the current value of k
        if min_val == 0:
            return k
        
        # Eliminate the smallest element and update the result array
        res = eliminate(res, k)
        
        # Increment the value of k by 1
        k += 1

def solve():
    # Read the number of test cases from standard input
    t = int(input())
    
    # Iterate through the test cases
    for _ in range(t):
        # Read the length of the array and the array itself from standard input
        n = int(input())
        a = list(map(int, input().split()))
        
        # Find the smallest element in the array and eliminate it
        k = find_k(a)
        
        # Print the result of the test case
        print(k)

solve()
