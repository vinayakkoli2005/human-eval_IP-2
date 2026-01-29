import sys

def solve(a):
    deque = []
    inv_count = 0
    for elem in a:
        if elem not in deque:
            deque.append(elem)
        else:
            idx = deque.index(elem)
            if idx == len(deque) - 1:
                deque.insert(0, elem)
            else:
                deque.insert(len(deque), elem)
        inv_count += len(deque) - idx - 1
    return inv_count

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(a))
