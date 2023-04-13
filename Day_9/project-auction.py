import os


def clear(): return os.system('clear')


print("Welcome to the secret auction program")

bidders = {}


def place_a_bid():
    name = input("What is your name? ")
    bid = int(input("What's your bid? $"))
    bidders[name] = bid


run = True
while run == True:
    place_a_bid()
    others = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if others == 'no':
        run = False
    else:
        clear()

higher_bid = 0
winner = ''
for name in bidders:
    if bidders[name] > higher_bid:
        higher_bid = bidders[name]
        winner = name


print(f"The highest bid is {winner} with a bid of ${higher_bid}")
print(bidders)
