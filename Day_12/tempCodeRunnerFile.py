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