row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to  put the treasure?")

colum_position = int(position[0]) - 1
row_position = int(position[1]) 

if (row_position == 1):
    row1[colum_position] = '✖'
elif (row_position == 2):
    row2[colum_position] = '✖'
else:
    row3[colum_position] = '✖'

print(f"{row1}\n{row2}\n{row3}")
