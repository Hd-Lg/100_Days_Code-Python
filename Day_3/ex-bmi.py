height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / (height ** 2)


if (bmi < 18.5):
    print("You are underweight.")
elif (18.5 < bmi < 25):
    print("You have a normal weight.")
elif (25 < bmi < 30):
    print("You are obese")
elif (30 < bmi < 35):
    print("You are obese")
elif (bmi > 35):
    print("You are clinically obese")
