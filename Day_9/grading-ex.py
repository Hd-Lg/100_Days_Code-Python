student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

student_grades = {}

for key in student_scores:
    score_student = student_scores[key]
    if score_student >= 91:
        student_grades[key] = "Outstanding"
    elif score_student >= 81:
        student_grades[key] = "Exceed Expectations"
    elif score_student >= 71:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)
