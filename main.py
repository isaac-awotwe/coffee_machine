# import the menu of the various coffe types and the staring resource stock
from utils import MENU, resources

# Add "money" to the resources
resources["money"] = 0

# Add milk of zero ml to espresso
MENU["espresso"]["ingredients"]["milk"] = 0

# Define function for the resource report
def generate_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources["money"]}")

def coins_value(num_quarters, num_dimes, num_nickles, num_pennies):
    return (0.25 * num_quarters) + (0.10 * num_dimes) + (0.05 * num_nickles) + (0.01 * num_pennies)

def change(pmt_total, cost):
   return pmt_total - cost

def resources_check(coffee_type):
    if MENU[coffee_type]["ingredients"]["water"] > resources["water"]:
        print("Sorry, there is not enough water.")
        return False
    if MENU[coffee_type]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry, there is not enough coffee.")
        return False
    if MENU[coffee_type]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry, there is not enough milk.")
        return False
    return True

def resource_balance(coffee_type):
    resources['water'] -= MENU[coffee_type]["ingredients"]["water"]
    resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
    resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
    resources["money"] += MENU[coffee_type]['cost']

machine_on = True

while machine_on:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino). If you would rather want a report of resources, type 'report': ")
    if coffee_choice == "report":
        generate_report()
    elif coffee_choice == "espresso" or coffee_choice == "latte" or coffee_choice == "cappuccino":
        resources_enough = resources_check(coffee_choice)
        if resources_enough:
            payment_enough = False
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            amount_inserted = coins_value(quarters, dimes, nickles, pennies)
            change_amount = change(amount_inserted, MENU[coffee_choice]["cost"])
            if change_amount < 0:
                print("Sorry, that's not enough money. Money refunded.")
            elif change_amount > 0:
                print(f"Here is ${change_amount:.2f} in change.")
                payment_enough = True
            else:
                payment_enough = True
            if payment_enough:
                resource_balance(coffee_choice)
                print(f"Here is your {coffee_choice} ☕. Enjoy!")
    elif coffee_choice == "off":
        print("Goodbye")
        machine_on = False
    else:
        print("The input you provided is incorrect. Carefully type in one of the acceptable choices.")
