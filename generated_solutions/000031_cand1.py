import sys

# Read input
t = int(input())
for i in range(t):
    n = int(input())
    s = input()

    # Check if string is already a palindrome
    if s == s[::-1]:
        print("0")
        continue

    # Find the first non-palindromic letter in the string
    non_palindromic_letter = ""
    for j in range(n):
        if s[j] != s[-j-1]:
            non_palindromic_letter = s[j]
            break
    
    # Check if it's possible to make the string a palindrome by erasing some occurrences of this letter
    if non_palindromic_letter == "":
        print("-1")
    else:
        count = 0
        for j in range(n):
            if s[j] == non_palindromic_letter:
                count += 1
        print(count)
