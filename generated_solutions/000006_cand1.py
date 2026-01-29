import math

def solve(n, k, a):
    # Initialize the expected number of operations to 0
    expected = 0

    # Loop through each element in the array
    for i in range(n):
        # If the current element is -1, replace it with a random number between 0 and k-1
        if a[i] == -1:
            a[i] = random.randint(0, k-1)

        # Increment the expected number of operations based on the probability of replacing each element
        expected += (n-1)/n * math.log(k, 2)

    return int(expected % (10**9 + 7))

# Test the solution with the examples given in the problem statement
def test_solution():
    n, k = 2, 2
    a = [0, 1]
    assert solve(n, k, a) == 2

    n, k = 2, 2
    a = [0, -1]
    assert solve(n, k, a) == 1

    n, k = 3, 3
    a = [0, 1, 1]
    assert solve(n, k, a) == 12

    n, k = 3, 3
    a = [-1, -1, -1]
    assert solve(n, k, a) == 11

    n, k = 10, 9
    a = [-1, 0, -1, 1, 1, 2, 2, 3, 3, 3]
    assert solve(n, k, a) == 652419213

# Call the test function to check the solution
test_solution()
