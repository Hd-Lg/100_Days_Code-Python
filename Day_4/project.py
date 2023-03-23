import random

rock = '🪨'
paper = '📜'
scissors = '✂️'
choice = [rock, paper, scissors]

computer_choice = random.randint(0, 2)
user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors "))

display_choice = f"{choice[user_choice]}\nComputer chose:\n{choice[computer_choice]}"
win = 'You win!'


if (user_choice == 0 and computer_choice == 2):
    print(display_choice)
    print(win)
elif (user_choice == 1 and computer_choice == 0):
    print(display_choice)
    print(win)
elif (user_choice == 2 and computer_choice == 1):
    print(display_choice)
    print(win)
else:
    print(display_choice)
    print("You lose!")
