import math

n, m, k, r, c = map(int, input().split())
a_x, a_y, b_x, b_y = map(int, input().split())

# Calculate the number of possible color combinations for sub-rectangle 1
num_colors_sub1 = math.ceil((r * c) / k)

# Calculate the number of possible color combinations for sub-rectangle 2
num_colors_sub2 = math.ceil(((n - a_x + 1) * (m - a_y + 1)) / k)

# Calculate the number of possible color combinations for the entire batik
num_colors_batik = num_colors_sub1 * num_colors_sub2

print(pow(num_colors_batik, modulo=1000000007))
