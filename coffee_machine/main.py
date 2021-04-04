from data import beverages, resources, coin


def turn_off_machine():
    """
    For maintainers of the coffee machine, they can use "off" as the secret word to turn off
    the machine. Your code should end execution when this happens.
    """
    return True


def report():
    """
    When the user enters "report" to the prompt, a report should be generated that shows
    the current resource values.
    """
    msg = f"""Water:\t{resources['water']}ml
Milk:\t{resources['milk']}ml
Coffee:\t{resources['coffee']}g
Money:\t${resources['money']:.2f}"""
    return msg


def check_machine_resources(beverage):
    """
    Check if all the resources are sufficient to make a beverage
    """
    if beverage == "espresso":
        if (
            resources["water"] >= beverages[beverage]["ingredients"]["water"] and
            resources["coffee"] >= beverages[beverage]["ingredients"]["coffee"]
        ):
            return True, "OK"
        elif resources["water"] < beverages[beverage]["ingredients"]["water"]:
            return False, "water"
        elif resources["coffee"] < beverages[beverage]["ingredients"]["coffee"]:
            return False, "coffee"
    elif beverage == "latte" or beverage == "cappuccino":
        if (
            resources["water"] > beverages[beverage]["ingredients"]["water"] and
            resources["coffee"] > beverages[beverage]["ingredients"]["coffee"] and
            resources["milk"] > beverages[beverage]["ingredients"]["milk"]
        ):
            return True, "OK"
        elif resources["water"] < beverages[beverage]["ingredients"]["water"]:
            return False, "water"
        elif resources["coffee"] < beverages[beverage]["ingredients"]["coffee"]:
            return False, "coffee"
        elif resources["milk"] < beverages[beverage]["ingredients"]["milk"]:
            return False, "milk"


def process_coins(pennies, nickles, dimes, quarters):
    """
    Calculate the monetary value of the coins inserted.
    """
    total_coins = coin["penny"] * pennies + coin["nickel"] * nickles + coin["dime"] * dimes + coin["quarter"] * quarters
    resources["money"] = total_coins


def check_transaction(beverage):
    """
    Check that the user has inserted enough money to purchase the drink they selected.
    """
    if resources["money"] >= beverages[beverage]["cost"]:
        return True
    else:
        return False


def reduce_resource_limit(beverage):
    """
    Get the machine resources and reduce according each beverage prepared.
    """
    if check_machine_resources(beverage)[0] and beverage == "espresso":
        resources["water"] = resources["water"] - beverages[beverage]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - beverages[beverage]["ingredients"]["coffee"]
        resources["money"] = resources["money"] - beverages[beverage]["cost"]
    elif check_machine_resources(beverage)[0] and (beverage == "latte" or beverage == "cappuccino"):
        resources["water"] = resources["water"] - beverages[beverage]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - beverages[beverage]["ingredients"]["coffee"]
        resources["milk"] = resources["milk"] - beverages[beverage]["ingredients"]["milk"]
        resources["money"] = resources["money"] - beverages[beverage]["cost"]


def check_change():
    """
    Check if there is some change after preparing a beverage
    """
    if resources["money"] > 0:
        return True
    else:
        return False


def main():
    """
    Executes all the machine logic.
    """
    is_machine_off = False
    while not is_machine_off:
        option = input("What would you like? (espresso/latte/cappuccino): ")
        if option == "off":
            is_machine_off = turn_off_machine()
        elif option == "report":
            print(report())
        elif option == "espresso" or option == "latte" or option == "cappuccino":
            status = check_machine_resources(option)
            if status[0]:
                pennies = int(input("How many pennies $0.01? "))
                nickles = int(input("How many nickles $0.05? "))
                dimes = int(input("How many dimes $0.10? "))
                quarters = int(input("How many quarters $0.25? "))
                process_coins(pennies, nickles, dimes, quarters)
                if check_transaction(option):
                    print(f"Here is your {option}. Enjoy!")
                    print(f"Report before purchasing {option}:")
                    print(report())
                    reduce_resource_limit(option)
                    print(f"Report after purchasing {option}:")
                    print(report())
                    if check_change():
                        print(f"Here is ${resources['money']:.2f} dollars in change.")
                        resources["money"] = 0.00
                else:
                    print("Sorry that is not enough money. Money refunded.")
                    print(f"Here is ${resources['money']:.2f} dollars.")
                    resources["money"] = 0.00
            else:
                if status[1] == "water":
                    print("Sorry there is not enough water.")
                    print(f"{option} needs {beverages[option]['ingredients']['water']}ml of water.")
                    print(f"The machine has {resources['water']}ml of water.")
                elif status[1] == "coffee":
                    print("Sorry there is not enough coffee.")
                    print(f"{option} needs {beverages[option]['ingredients']['coffee']}g of coffee.")
                    print(f"The machine has {resources['coffee']}g of coffee.")
                elif status[1] == "milk":
                    print("Sorry there is not enough milk.")
                    print(f"{option} needs {beverages[option]['ingredients']['milk']}ml of milk.")
                    print(f"The machine has {resources['milk']}ml of milk.")
        else:
            print("You need to choose between (espresso/latte/cappuccino).")


main()
