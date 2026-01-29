import sys

def solve(matrix):
    # Check if it is possible to color the matrix with red and blue rows
    if not can_color(matrix, 'red') or not can_color(matrix, 'blue'):
        return "NO"
    
    # Find a perfect coloring and cut
    for k in range(1, len(matrix[0])):
        if is_perfect(matrix[:k], 'red') and is_perfect(matrix[k:], 'blue'):
            return "YES", get_coloring(matrix[:k]), str(len(matrix[0]) - k)
    
    # If no perfect coloring and cut was found, report that there are none
    return "NO"

def can_color(matrix, color):
    # Check if it is possible to color the matrix with red or blue rows
    for row in matrix:
        if all(cell == color for cell in row):
            return False
    return True

def is_perfect(matrix, color):
    # Check if a perfect coloring and cut exists for the given color
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > matrix[i-1][j]:
                return False
    return True

def get_coloring(matrix):
    # Get the coloring of the matrix with red and blue rows
    coloring = ""
    for i in range(len(matrix)):
        if matrix[i] == "red":
            coloring += "R"
        else:
            coloring += "B"
    return coloring

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        matrix = []
        for _ in range(n):
            row = list(map(int, input().split()))
            matrix.append(row)
        print(solve(matrix))
