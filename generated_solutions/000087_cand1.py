import sys

# Read input
t = int(input())

# Loop through each test case
for i in range(t):
    # Read input for current test case
    n, k, x = map(int, input().split())

    # Initialize variables
    valid_sequences = 0
    sequence_length = 2**k
    mask = 1 << (sequence_length - 1)

    # Loop through all possible sequences of length n
    for j in range(sequence_length**n):
        # Convert to binary representation
        binary_rep = bin(j)[2:]
        binary_rep = '0' * (sequence_length - len(binary_rep)) + binary_rep

        # Check if sequence satisfies conditions
        if all([int(binary_rep[i]) < 2**k for i in range(n)]):
            subsequence_xor = sum([int(binary_rep[i]) ^ int(binary_rep[i+1]) for i in range(n-1)])
            if subsequence_xor == x:
                valid_sequences += 1

    # Print answer for current test case
    print(valid_sequences)
