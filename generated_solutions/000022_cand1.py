import math

def count_permutations(n, m, k, p):
    # Calculate the number of permutations modulo p
    num_permutations = math.factorial(n) % p
    # Calculate the number of good numbers modulo p
    num_good_numbers = math.comb(n, k) % p
    # Return the result
    return num_permutations // (num_good_numbers ** m)
[/PYTHON]
[TESTS]
# Test case 1:
assert count_permutations(4, 3, 2, 10007) == 4
# Test case 2:
assert count_permutations(6, 4, 1, 769626776) == 472
# Test case 3:
assert count_permutations(66, 11, 9, 786747482) == 206331312
# Test case 4:
assert count_permutations(99, 30, 18, 650457567) == 77365367
[/TESTS]
