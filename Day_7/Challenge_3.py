import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(f"Psssst, the solution is {chosen_word}")

display = []
underscore = '_'

for _ in range(word_length):
    display += underscore

while underscore in display:
    guess = input('Guess a letter: ').lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
