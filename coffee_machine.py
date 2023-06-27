MENU = {
    "espresso": {
        "ingredients": {
            "milk": 0,
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

#TODO 10 Function to check if resources are sufficient
def check_resources(coffee) :
    if resources["water"] < MENU[coffee]["ingredients"]["water"] :
        print("Sorry, there is not enough water.")
        return False
    elif resources["milk"] < MENU[coffee]["ingredients"]["milk"] :
        print("Sorry, there is not enough milk.")
        return False
    elif resources["coffee"] < MENU[coffee]["ingredients"]["coffee"] :
        print("Sorry, there is not enough coffee.")
        return False
    else :
        return True

#TODO 11 A function to check if transaction is successful
def check_transaction(q,d,n,p,coffee) :
    given = (0.25*q)+(0.1*d)+(0.05*n)+(0.01*p)
    if given >= MENU[coffee]["cost"] :
        change = round(given - MENU[coffee]["cost"],2)
        if not change == 0 :

            print(f"Here is ${change} in change.")
        return True
    else :
        print("Sorry that's not enough money. Money refunded.")
        return False

MONEY = 0

#TODO 1 Ask user what they like
def game() :

    user_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    global MONEY

#TODO 2 if they ask for report print resources
    if user_coffee == "report" :
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${MONEY}")
        game()


#TODO 3 or else check if the resources are sufficient or not
    else :
        if check_resources(user_coffee) :
            print("Insert coins")
            q = int(input("How many quarters?: "))
            d = int(input("How many dimes?: "))
            n = int(input("How many nickles?: "))
            p = int(input("How many pennies?: "))
            if check_transaction(q,d,n,p,user_coffee) :
                MONEY += MENU[user_coffee]["cost"]
                for key in resources :
                    resources[key] -= MENU[user_coffee]["ingredients"][key]
                print(f"Here is your {user_coffee} . Enjoy!")
                game()
            else :
                game()
        else :
            game()


game()







#TODO 4 If sufficient ask them to insert coins  ((((DONE))))

#TODO 5 If not tell them which resource is insufficient    ((((DONE))))

#TODO 6 Check if transaction is succesful and return change if necessary   ((((DONE))))

#TODO 7 If succesful deduct ingridients and give them coffee  ((((DONE))))

#TODO 8 If not succesful ,say money refunded as money is insufficient   ((((DONE))))

#TODO 9 Repeat the same process after coffee is given
