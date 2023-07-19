MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0
}


def check_resources(selection, water_left, water_needed, milk_left, milk_needed, coffee_left, coffee_needed):
    if water_left > water_needed and milk_left > milk_needed and coffee_left > coffee_needed:
        return process_coins(selection, water_left, water_needed, milk_left, milk_needed, coffee_left, coffee_needed)
    else:
        if water_needed > water_left:
            return f"Sorry there is not enough water!"
        elif milk_needed > milk_left:
            return f"Sorry there is not enough milk!"
        elif coffee_needed > coffee_left:
            return f"Sorry there is not enough coffee!"


def process_coins(selection, water_left, water_needed, milk_left, milk_needed, coffee_left, coffee_needed):
    coffee_price = MENU[selection]["cost"]
    quarters = 0.25
    dimes = 0.10
    nickels = 0.05
    pennies = 0.01
    print("Please insert coins.")
    quarters_paid = int(input("How many quarters?: "))
    dimes_paid = int(input("How many dimes?: "))
    nickels_paid = int(input("How many nickels?: "))
    pennies_paid = int(input("How many pennies?: "))
    money_paid = (quarters * quarters_paid) + (dimes * dimes_paid) + (nickels * nickels_paid) + (pennies * pennies_paid)
    if money_paid > coffee_price:
        change = money_paid - coffee_price
        resources["money"] += (money_paid - change)
        resources["water"] -= (water_left - water_needed)
        resources["milk"] -= (milk_left - milk_needed)
        resources["coffee"] -= (coffee_left - coffee_needed)
        return f"Here is ${round(change, 2)} in change.\nHere is your {selection} ☕. Enjoy!"
    elif money_paid == coffee_price:
        resources["money"] += money_paid
        return f"Here is your {selection} ☕. Enjoy!"
    else:
        return "Sorry that's not enough money. Money refunded."


def working():
    selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if selection == "off":
        pass
        working()
    elif selection == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")
        working()
    elif selection != "espresso" and selection != "latte" and selection != "cappuccino":
        print("Sorry, I didn't understand you.")
        working()
    elif selection == "espresso" or "latte" or "cappuccino":
        water_left = resources['water']
        water_needed = MENU[selection]["ingredients"]["water"]
        milk_left = resources['milk']
        milk_needed = MENU[selection]["ingredients"]["milk"]
        coffee_left = resources['coffee']
        coffee_needed = MENU[selection]["ingredients"]["coffee"]
        # check_resources(selection, water_left, water_needed, milk_left, milk_needed, coffee_left, coffee_needed)
        print(check_resources(selection, water_left, water_needed, milk_left, milk_needed, coffee_left, coffee_needed))
        working()


working()
