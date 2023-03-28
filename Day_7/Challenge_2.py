import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

print(f"Psssst, the solution is {chosen_word}")

display = []

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if(letter == guess):
        display.append(letter)
    else:
        display.append('_')

print(display)