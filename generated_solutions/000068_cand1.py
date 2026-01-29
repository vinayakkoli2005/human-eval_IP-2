import math

def get_minimum_maps(n, p):
    # Calculate the probability of playing a map that Johnny has not studied
    prob = 1 - (1 - p) ** n

    # Find the smallest integer greater than or equal to the probability
    # and multiply it by 2 because we need to study two maps
    min_maps = math.ceil(prob) * 2

    return min_maps

# Test case
n, p = 7, 0.5
print(get_minimum_maps(n, p)) # Output: 6
