import csv
from typing import List


def calculate(student_num: int, score: List[int]) -> None:
    """
    Calculate grades based on the scores and number of students.
    Doesn't return anything, but writes the results to 'grades.csv'.
    """
    students = student_num
    scores = score
    best = max(scores)
    j = 0

    with open('grades.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Student', 'Score', 'Grade'])
        for i in scores:
            j += 1
            if i >= (best - 10):
                grade = 'A'
            elif i >= (best - 20):
                grade = 'B'
            elif i >= (best - 30):
                grade = 'C'
            elif i >= (best - 40):
                grade = 'D'
            else:
                grade = 'F'
            csv_writer.writerow([f'Student {j}', i, grade])
