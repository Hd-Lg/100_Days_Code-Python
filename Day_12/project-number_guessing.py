import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking a number between 1 and 100.")


def choose_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == 'easy':
        print("You have 10 attempts to guess the number.")
        return 10
    else:
        print("You have 5 attempts to guess the number.")
        return 5


number = random.randint(1, 100)
attempts = choose_difficulty()
is_find = False

while not is_find and attempts != 0:
    user_guess = int(input("Make a guess: "))

    if user_guess > number:
        print("Too high.")
        print("Guess again.")
        attempts -= 1
        print(
            f"You have {attempts} attempts remaining to guess the number.")
    elif user_guess < number:
        print("Too low.")
        print("Guess again.")
        attempts -= 1
        print(
            f"You have {attempts} attempts remaining to guess the number.")
    else:
        print("You found it!")
        is_find = True
