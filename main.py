##Print Reports
##Check Resource are Sufficiente
# recebe a escolha do café
##Insert coins penny0,01, nickel0,05, dime 0,10, quarter 0,25
##Receive the coins and calculate the price e change.
##process if the transaction sucessefull
##printa uma mensagem positiva que o café está pronto 
##updade report
##error msg case of no enough resources
from machine_data import MENU, resources

def format_current_resources():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    return f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}"

def check_resources(typeCoffee):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"] 

    if typeCoffee =="espresso":
        waterTest = MENU[f'{typeCoffee}']['ingredients']['water']
        coffeeTest = MENU[f'{typeCoffee}']['ingredients']['coffee']
        if water < waterTest:
            print("Sorry not enough milk")  
            return False
        elif coffee < coffeeTest:
            print("Sorry not enough coffee")
            return False
        else:
            print("Preparing 'espresso'...")
            return True
    else:
        milkTest = MENU[f'{typeCoffee}']['ingredients']['milk']
        if waterTest > water:
            print("Sorry is not enough water")
            return False
        elif milkTest > milk:
            print("Sorry is not enough milk")
            return False
        elif coffeeTest > coffee:
            print("Sorry is not enough coffee")
            return False
        else:
            return True
    
def check_coins(penny, nickle, dime, quarter, typeCoffee):
    total = penny * 0.01 + nickle * 0.05 + dime * 0.1 + quarter * 0.25
    cost = MENU[f'{typeCoffee}']['cost']
    if total < cost:
        print("Not enough coins. Refunded!")
        return False
    else:
        change = total - cost
        print("Transaction complete. Your change: %.2f." % change)
        return True
    
def update_resources(typeCoffee):

    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    if typeCoffee == "espresso":
        waterTest = MENU[f'{typeCoffee}']['ingredients']['water']
        coffeeTest = MENU[f'{typeCoffee}']['ingredients']['coffee']
        water -= waterTest
        coffee -= coffeeTest
    else:
        milkTest = MENU[f'{typeCoffee}']['ingredients']['milk']
        water -= waterTest
        milk -= milkTest
        coffee -= coffeeTest
    
    return "Resources Updated"
on = True
while on: 

    prompt = input('\nWhat would you like? (espresso/latte/cappuccino)').lower()

    if prompt == 'off':
        on = False
        print("Bye, you turned off me!")
    elif prompt == 'report':
        print(format_current_resources())
    else:
        if check_resources(prompt):
            print("Please insert coins:")

            penny = int(input("How much penny?"))
            nickle = int(input("How much nickle?"))
            dime = int(input("How much dime?"))
            quarter = int(input("How much quarter?"))

            check_coins(penny, nickle, dime, quarter, prompt)

            if check_coins:
                print(update_resources(prompt))
                print(f"Here is your {prompt}")
        


        




    
