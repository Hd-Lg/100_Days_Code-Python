print("Welcome to the Love Calculator!")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

name1 = name1.lower()
name2 = name2.lower()

letter_t = name1.count("t") + name2.count("t")
letter_r = name1.count("r") + name2.count("r")
letter_u = name1.count("u") + name2.count("u")
letter_e = name1.count("e") + name2.count("e")
total_true = letter_t + letter_r + letter_u + letter_e

letter_l = name1.count("l") + name2.count("l")
letter_o = name1.count("o") + name2.count("o")
letter_v = name1.count("v") + name2.count("v")
letter_e = name1.count("e") + name2.count("e")
total_love = letter_l + letter_o + letter_v + letter_e

total = int(f"{total_true}{total_love}")

if (total < 10 or total > 90):
    print(f"Your score is {total}, you go together like coke and mentos.")
elif (total >= 40 and total <= 50):
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}")
