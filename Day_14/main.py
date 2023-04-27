import random
from data import data
import os


def clear(): return os.system('clear')


def display_data(account):
    """Format the data into printable string"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """ Check if user is correct """
    if a_followers > b_followers:
        return user_guess == 'a'
    else:
        return user_guess == 'b'


choice_B = random.choice(data)


score = 0
continue_game = True

while continue_game:
    choice_A = random.choice(data)
    choice_B = random.choice(data)

    if choice_A == choice_B:
        choice_B = random.choice(data)

    print("Higher or Lower Game")
    print(f"Compare A: {display_data(choice_A)}")
    print('vs')
    print(f"Against B: {display_data(choice_B)}")

    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_followers = choice_A["follower_count"]
    b_followers = choice_B["follower_count"]

    is_right = check_answer(user_guess, a_followers, b_followers)

    if is_right:
        score += 1
        clear()
        print(f"Right. Current score: {score}")
    else:
        print(f"Wrong. Final score: {score}")
        continue_game = False
