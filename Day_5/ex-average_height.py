student_heights = input("Input a list of student heights: ").split()


sum_heights = 0
length = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    sum_heights += student_heights[n]
    length += 1
    print(length)

average_height = round(sum_heights / length)
print(average_height)