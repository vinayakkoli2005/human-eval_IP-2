import sys

def check_rbs(s):
    # Check if a bracket sequence is a regular bracket sequence
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
    return not stack

def get_rbs_prefixes(s):
    # Get all prefixes of a bracket sequence that are regular bracket sequences
    prefixes = []
    for i in range(len(s)):
        prefix = s[:i+1]
        if check_rbs(prefix):
            prefixes.append(prefix)
    return prefixes

def solve(n, strings):
    # Find the maximum number of non-empty prefixes that are regular bracket sequences
    max_prefixes = 0
    for s in strings:
        prefixes = get_rbs_prefixes(s)
        max_prefixes = max(max_prefixes, len(prefixes))
    return max_prefixes

if __name__ == '__main__':
    n = int(input())
    strings = []
    for _ in range(n):
        strings.append(input())
    print(solve(n, strings))
