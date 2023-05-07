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
    "money": 0
}


def response_query(drink):

    for k in MENU[drink]['ingredients']:
        if resources[k] - MENU[drink]['ingredients'][k] < 0:
            print(f"Sorry We do not have enough {k}")
            return 0
    return 1


def ask_money(drink):
    q = int(input("How many Quarters? : "))
    d = int(input("How many dimes? :"))
    n = int(input("How many nickels? :"))
    p = int(input("How many pennies? :"))

    amount = round(((q*25)+(d*10)+(n*5)+(p*1))/100, 2)
    return amount - MENU[drink]['cost']


def making_drink(drink):
    for j in MENU[drink]['ingredients']:
        resources[j] = resources[j] - MENU[drink]['ingredients'][j]
    resources["money"] = resources["money"] + MENU[drink]['cost']
    print(f"Here is your ☕ {drink}, Enjoy !")


while True:
    flag = 0
    query = input("What would you like (espresso/latte/cappuccino):")
    if query == 'report':
        for i in resources:
            print(f"{i}: {resources[i]}")
    elif query == 'off':
        break
    elif query in ['espresso', 'latte', 'cappuccino']:
        flag = response_query(query)  # checking if the resources are enough or not

    if flag == 1:  # if enough asking the money
        change = ask_money(query)

        if change < 0:  # if money given is less
            print("You haven't entered enough money")
        elif change > 0:  # if money given is more returning the change and giving the drink
            print(f"Here is your ${round(change,4)} change")
            making_drink(query)
        else:   # if exact giving the drink
            making_drink(query)








