from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


def main():
    """
    Executes all the coffee machine logic.
    """
    is_machine_off = False
    while not is_machine_off:
        options = menu.get_items()
        choice = input(f"What would you like to drink? ({options}): ")
        if choice == "off":
            is_machine_off = True
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
        else:
            print(f"You need to choose between ({options}).")


main()
