from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

bank = MoneyMachine()
maker = CoffeeMaker()
menu = Menu()

running = True

#possible bug?? returns an extra "/" used a slice last method to remove last char.
options = menu.get_items()[:-1]

while running:
    choice = input(f'What would you like? ({options}): ')

    if choice == "off":
        running = False
    elif choice == "report":
        maker.report()
        bank.report()
    else:
        drink = menu.find_drink(choice)
        resource_ok = maker.is_resource_sufficient(drink)
        
        if resource_ok:
            paid = bank.make_payment(drink.cost)
            if paid:
                maker.make_coffee(drink)
