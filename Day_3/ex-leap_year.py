year = int(input("Which year do you want to check? "))

year_div_4 = year / 4
year_div_100 = year / 100
year_div_400 = year / 400


if (year_div_4 % 2 == 0):
    if (year_div_100 % 2 != 0):
        print("Normal year")
    elif (year_div_400 % 2 == 0):
        print("Leap year")
    else:
        print("Normal year")
else:
    print("Normal year")
