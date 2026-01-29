import sys

def solve(n, student_days):
    """
    Given a list of n students and their preferences for attending lessons on different days, determine if it is possible to divide the students into two groups of equal sizes and choose different days for the groups so each student can attend the lesson in the chosen day of their group.

    Args:
        n (int): The number of students.
        student_days (list[list[int]]): A list of lists, where each inner list contains the preference of a student for attending lessons on different days.

    Returns:
        bool: True if it is possible to divide the students into two groups of equal sizes and choose different days for the groups so each student can attend the lesson in the chosen day of their group, False otherwise.
    """
    # Initialize a dictionary to keep track of the number of students who prefer each day
    day_count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    for student in student_days:
        for i, day in enumerate(student):
            if day == 1:
                day_count[i] += 1

    # Check if there are an even number of students who prefer each day
    for count in day_count.values():
        if count % 2 != 0:
            return False

    # Divide the students into two groups based on their preferences
    group1 = []
    group2 = []
    for student, days in zip(student_days, enumerate(day_count)):
        if days[1] % 2 == 0:
            group1.append(student)
        else:
            group2.append(student)

    # Check if the groups have equal sizes and if each student can attend the lesson in the chosen day of their group
    for student in group1:
        if not any(day == 1 for i, day in enumerate(student)):
            return False
    for student in group2:
        if not any(day == 1 for i, day in enumerate(student)):
            return False

    return True


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        student_days = []
        for _ in range(n):
            student_days.append(list(map(int, input().split())))
        if solve(n, student_days):
            print("YES")
        else:
            print("NO")
