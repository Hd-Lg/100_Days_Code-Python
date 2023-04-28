MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
espresso_ing = MENU["espresso"]["ingredients"]
latte_ing = MENU["latte"]["ingredients"]
cappuccino_ing = MENU["cappuccino"]["ingredients"]


def power_off():
    """End execution of the program"""
    global is_running
    is_running = False


def print_report():
    print(f"water: {resources['water']} ml.")
    print(f"milk: {resources['milk']} ml. ")
    print(f"coffee: {resources['coffee']} g. ")
    print(f"Money: ${profit}")


def check_resources(order_ingredients):
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] >= resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
        return True


def process_coins():
    """Return total from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters? $0.25: ")) * 0.25
    total += int(input("How many dimes? $0.10: ")) * 0.10
    total += int(input("How many nickles? $0.05: ")) * 0.05
    total += int(input("How many pennies? $0.01: ")) * 0.01
    return total


def is_transaction_passed(money, drink_cost):
    """Return True when payment is accepted, False otherwise"""
    if money >= drink_cost:
        global profit
        profit += drink_cost
        change = round(money - drink_cost, 2)
        print(f"Here is your change: ${change}")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {name}. Enjoy!")


is_running = True
while is_running:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    enough_resources = False
    match user_choice:
        case "report":
            print_report()
        case "off":
            power_off()
        case "espresso":
            if check_resources(espresso_ing):
                enough_resources = True
                price = MENU[user_choice]["cost"]
                print(f"${price}")
                payment = process_coins()
                if is_transaction_passed(payment, price):
                    make_coffee(user_choice, espresso_ing)
        case "latte":
            if check_resources(latte_ing):
                enough_resources = True
                price = MENU[user_choice]["cost"]
                print(f"${price}")
                payment = process_coins()
                if is_transaction_passed(payment, price):
                    make_coffee(user_choice, latte_ing)
        case "cappuccino":
            if check_resources(cappuccino_ing):
                enough_resources = True
                price = MENU[user_choice]["cost"]
                print(f"${price}")
                payment = process_coins()
                if is_transaction_passed(payment, price):
                    make_coffee(user_choice, cappuccino_ing)
