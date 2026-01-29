import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# Sort the array in ascending order
arr.sort()

# Initialize variables to keep track of the current sequence and the winner
sequence = []
winner = "Alice"

# Loop through the array and append numbers to the sequence
for i in range(n):
    if i == 0 or arr[i] > arr[i-1]:
        sequence.append(arr[i])

# Check if the sequence is strictly increasing, if not then Bob wins
if not sequence:
    winner = "Bob"
else:
    # If the sequence is strictly increasing, check who made the last move
    if len(sequence) % 2 == 0:
        winner = "Alice"
    else:
        winner = "Bob"

# Output the name of the winner
print(winner)
