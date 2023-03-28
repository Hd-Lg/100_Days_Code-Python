import random

stages = ['0 life - Dead', '1 life', '2 lives', '3 lives', '4 lives', '5 lives', '6 lives']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(f"Psst, the solution is {chosen_word}")

lives = 6
display = []
for _ in range(word_length):
    display += '_'


while end_of_game == False:
    guess = input('Guess a letter: ').lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("You lose")
            end_of_game = True


    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])


