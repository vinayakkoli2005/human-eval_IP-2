# This program solves the problem of counting the number of possible integers represented by a string
# that are divisible by 25 and do not contain any leading zeros.

s = input() # read input from standard input

# initialize variables to keep track of the number of possible values
num_possible_values = 0
leading_zeros = 0

# loop through each character in the string
for char in s:
    if char == '_': # if the character is an underscore, replace it with any digit
        num_possible_values *= 10
    elif char == 'X': # if the character is an X, replace it with the same digit for every X
        num_possible_values *= 10
    else:
        num_possible_values += 1 # add 1 to the number of possible values

# check if the input string has any leading zeros
if s[0] == '0':
    leading_zeros = len(s) - s.find('0') - 1

# subtract the number of leading zeros from the total number of possible values
num_possible_values -= leading_zeros

# output the result
print(num_possible_values)
