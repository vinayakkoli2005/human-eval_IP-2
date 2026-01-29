import math

n, x = map(int, input().split())

# Calculate the number of ways to choose the initial health points for each hero a_i, where 1 <= a_i <= x, so that there is no winner of the fight
ways = 0
for i in range(x+1):
    # Calculate the number of alive heroes after round i
    alive = math.factorial(n) // (math.factorial(n-i)*math.factorial(i))
    # Calculate the number of ways to choose the health points for each hero, given that there are alive heroes left
    choices = math.factorial(alive) // (math.factorial(alive-1)*math.factorial(1))
    # Add the number of ways to choose the initial health points for each hero a_i, where 1 <= a_i <= x, so that there is no winner of the fight
    ways += choices

# Print the number of ways modulo 998244353
print(ways % 998244353)
