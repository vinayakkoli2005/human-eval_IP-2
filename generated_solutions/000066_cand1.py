import sys

def balance(weights, sides):
    """
    weights: list of integers representing the weights to be balanced
    sides: string of characters 'L' and 'R' indicating which side of the balance should be heavier after putting the i-th weight

    returns: a list of pairs (weight, side) where weight is an integer and side is a character in {'L', 'R'} representing the weight to put on the balance in that move and the side of the balance where it should be put
    """
    if len(weights) != len(sides):
        return [-1]

    result = []
    for i in range(len(weights)):
        if sides[i] == 'L':
            result.append((weights[i], 'L'))
        else:
            result.append((weights[i], 'R'))

    return result

if __name__ == "__main__":
    input = sys.stdin.read()
    weights, sides = input.split("\n")[1:3]
    weights = [int(w) for w in weights.split(" ")]
    sides = sides.strip()

    result = balance(weights, sides)
    if result == [-1]:
        print(-1)
    else:
        for r in result:
            print(r[0], end=" ")
            print(r[1])
