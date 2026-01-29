import sys

def get_axis_coverage(segments):
    coverage = []
    for segment in segments:
        coverage.extend([segment[0], segment[1]])
    return sorted(list(set(coverage)))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        segments = []
        for _ in range(n):
            a_i = list(map(int, input().split()))
            segments.append(a_i)
        axis_coverage = get_axis_coverage(segments)
        print(max(axis_coverage) - min(axis_coverage))
