from os import system
from menu import MENU
from art import logo

machine_on = True

resource = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "profit": 0.0
}

def clear():
    system('cls')
    print(logo)

def print_report(res):
    print(f"Water: {res['water']}ml")
    print(f"Milk: {res['milk']}ml")
    print(f"Coffee: {res['coffee']}g")
    print(f"Money: ${res['profit']}")

def check_resource(drink):
    for ingredient in drink:
        if drink[ingredient] >= resource[ingredient]:
            print(f"⚠️  Sorry we are low on {ingredient}. Please try another beverage.")
            return False
    return True

def process_pay(cost):
    print(f"The cost is ${cost}, please insert coins...")
    payment = int(input("how many quarters? ")) * 0.25
    print(f"Balance ${payment}")
    payment += int(input("how many dimes? ")) * 0.10
    print(f"Balance ${payment}")
    payment += int(input("how many nickles? ")) * 0.05
    print(f"Balance ${payment}")
    payment += int(input("how many pennies? ")) * 0.01
    print(f"Your total payment was ${payment}")

    if cost > payment:
        print("❌ Sorry that's not enough money. Money refunded.")
        return False
    else:
        print(f"Here is ${round(payment - cost, 2)} in change.")
        return True

def make_drink(drink):

    ingredients = drink["ingredients"]

    for items in ingredients:
        resource[items] -= ingredients[items]
    
    resource["profit"] += drink["cost"]

clear()

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    if choice == "off":
        machine_on = False
    elif choice == "clear":
        clear()
    elif choice == "report":
        print_report(resource)
    elif choice in ["espresso", "latte", "cappuccino"]:
        drink = MENU[choice]
        resource_ok = check_resource(drink["ingredients"])

        if resource_ok:
            payment_received = process_pay(drink["cost"])

            if payment_received:
                make_drink(drink)
                print(f"Your ☕ {choice.title()} is ready. Enjoy!")
            
    else:
        print("That drink does not exists. Please try again!")