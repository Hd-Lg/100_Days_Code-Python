print('Welcome to the tip calculator.')
bill = input('What was the total bill? $')
percentage_tip = input(
    'What percentage tip would you like to give? 10, 12 or 15? ')
number_people = input('How many people to split the bill?')

bill_tip = float(bill) * (1 + int(percentage_tip) / 100)
per_person = bill_tip / int(number_people)
result = round(per_person, 2)
result = "{:.2f}".format(per_person)
print(f"Each person should pay: ${result}")
