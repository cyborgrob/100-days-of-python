from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Creates a menu object and stores it in the variable 'menu'
menu = Menu()
# Creates a CoffeeMaker object and stores it in the variable 'machine'
machine = CoffeeMaker()
# Creates a MoneyMachine object and stores it in the variable 'money'
money = MoneyMachine()
run = True

# Machine runs while the 'run' variable is set to True
while run:
    # Fetches the list of current menu options and stores them in the variable 'options'
    options = menu.get_items()
    # Asks user what they'd like to drink from the list of options
    choice = input(f"What would you like? {options}: ")

    # Turns off the coffee machine/ends the program
    if choice == "off":
        run = False
    # Prints a report of the current ingredients in the machine and goes back to start of while loop.
    elif choice == "report":
        machine.report()
        money.report()
    else:
        # Returns a MenuItem object with the name of the user's choice (if it exists) and stores it in the variable
        # 'drink'
        drink = menu.find_drink(choice)
        # Checks to see if there's enough resources to make the drink the user requested
        if machine.is_resource_sufficient(drink):
            # This runs the make_payment method of the MoneyMachine and both asks how much money the user wants to
            # input as well as checks it against the cost of the drink. Returns True if enough money, False if not
            # enough. Also provides change.
            if money.make_payment(drink.cost):
                # If there are enough resources to make the drink, and enough money has been put in, it will make the
                # drink.
                machine.make_coffee(drink)
