student_scores = input("Input a list of student scores: ").split()

highest_score = 0
for score in range(0, len(student_scores)):
    student_scores[score] = int(student_scores[score])
    if (student_scores[score] > highest_score) :
        highest_score = student_scores[score]


print(f"The highest score in the class is: {highest_score}.")