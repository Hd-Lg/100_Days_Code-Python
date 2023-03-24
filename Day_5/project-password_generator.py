import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator")
nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

length_password = nr_letters + nr_symbols + nr_numbers

# Easy level
password = ''
for letter in range(0, nr_letters):
    random_letter = random.choice(letters)
    password += random_letter
for symbol in range(0, nr_symbols):
    random_symbol = random.choice(symbols)
    password += random_symbol
for number in range(0, nr_numbers):
    random_number = random.choice(numbers)
    password += random_number

print(f"Your password is: {password}")

# Hard Level
password = ''
for char in range(0, length_password):
    random_order = random.randint(0, 2)
    if(random_order == 0):
        # Letters
        password += random.choice(letters)
    elif (random_order == 1):
        # Symbols
        password += random.choice(symbols) 
    else:
        # Numbers
        password += random.choice(numbers)
print(f"Hard Level password is: {password}")

# Hard level - 2nd possibility
password=''
password_list = []
for letter in range(0, nr_letters):
   password_list.append(random.choice(letters))
for symbol in range(0, nr_symbols):
   password_list.append(random.choice(symbols))
for number in range(0, nr_numbers):
   password_list.append(random.choice(numbers))

random.shuffle(password_list)
for char in password_list:
    password += char
print(f"Hard Level password 2nd possibility is: {password}")
