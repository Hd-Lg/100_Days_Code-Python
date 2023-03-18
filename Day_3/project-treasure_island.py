print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

direction = input("Left or Right?").lower()
if (direction == 'left'):
    activity = input("Swim or wait?").lower()
    if (activity == 'wait'):
        door = input("Which door?").lower()
        if (door == 'yellow'):
            print("You win")
        else:
            print("Game over")
    else:
        print("Game over")
else:
    print("Game Over!")
