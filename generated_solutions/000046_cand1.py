# Read input from standard input
n = int(input())
a = list(map(int, input().split()))

# Initialize variables
height = 1
watered = False

# Iterate through the days
for i in range(n):
    # Check if the flower is watered on this day
    if a[i] == 1:
        watered = True
    # If the flower isn't watered for two days in a row, it dies
    elif not watered and i > 0 and a[i-1] == 0:
        height = -1
        break
    # If the flower is watered in this day, it grows by 1 centimeter
    elif watered:
        height += 1
    # If the flower isn't watered in this day, it doesn't grow
    else:
        pass

# Print the final height of the flower
print(height)
