import random 


name_string = input("Give me everybody's names, separated by a comma.")
names = name_string.split(', ')

length_list = len(names)

random_number = random.randint(0, length_list) 

print(f"{names[random_number]} is going to buy the meal today!")