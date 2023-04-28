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
        case "latte":
            if check_resources(latte_ing):
                enough_resources = True
            price = MENU[user_choice]["cost"]
        case "cappuccino":
            if check_resources(cappuccino_ing):
                enough_resources = True
            price = MENU[user_choice]["cost"]
    print(f"${price}")
    print("Please insert coins.")
    quarters = int(input("How many quarters? $0.25: "))
    dimes = int(input("How many dimes? $0.10: "))
    nickles = int(input("How many nickles? $0.05: "))
    pennies = int(input("How many pennies? $0.01: "))
    total = quarters + dimes + nickles + pennies
    give_back = total - price

    if total < price:
        print("Sorry, that's not enough money. Money refunded.")
    else:
        print(f"Here is ${give_back:.2f} in change.")
        print(f"Here is your {user_choice}. Enjoy!")
