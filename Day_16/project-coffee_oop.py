from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


is_running = True
while is_running:
    choices = menu.get_items()
    user_choice = input(f"What would you like? {choices}:")
    if user_choice == 'off':
        is_running = False
    elif user_choice == 'report':
        coffee_maker.report()
        machine.report()
    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink=drink):
            if machine.make_payment(drink.cost):
                coffee_maker.make_coffee(order=drink)
