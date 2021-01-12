# Write your code here
from math import floor

water_in_machine = 400
milk_in_machine = 540
coffee_beans_in_machine = 120
cups_of_coffee = 9
money = 550

maximum_cups = floor(min(water_in_machine / 200, milk_in_machine / 50, coffee_beans_in_machine / 15))


def remaining():
    print(f"""
The coffee machine has:
{water_in_machine} of water
{milk_in_machine} of milk
{coffee_beans_in_machine} of coffee beans
{cups_of_coffee} of disposable cups
{money} of money
""")


def fill_machine():
    global water_in_machine
    global milk_in_machine
    global coffee_beans_in_machine
    global cups_of_coffee
    global money

    print("Write how many ml of water do you want to add:")
    water = int(input())
    water_in_machine += water
    print("Write how many ml of milk do you want to add:")
    milk = int(input())
    milk_in_machine += milk
    print("Write how many grams of coffee beans do you want to add:")
    coffee = int(input())
    coffee_beans_in_machine += coffee
    print("Write how many disposable cups of coffee do you want to add:")
    cups = int(input())
    cups_of_coffee += cups


def resources(coffee):
    if coffee == 'espresso':
        if water_in_machine < 250:
            print("Sorry, not enough water!")
            return False
        elif coffee_beans_in_machine < 16:
            print("Sorry, not enough coffee beans!")
            return False
        elif cups_of_coffee <= 0:
            print("Sorry, not enough cups!")
            return False
        else:
            print("I have enough resources, making you a coffee!")
            return True
    elif coffee == 'cappuccino':
        if water_in_machine < 350:
            print("Sorry, not enough water!")
            return False
        elif milk_in_machine < 75:
            print("Sorry, not enough milk!")
            return False
        elif coffee_beans_in_machine < 20:
            print("Sorry, not enough coffee beans!")
            return False
        elif cups_of_coffee <= 0:
            print("Sorry, not enough cups!")
            return False
        else:
            print("I have enough resources, making you a coffee!")
            return True
    elif coffee == 'latte':
        if water_in_machine < 200:
            print("Sorry, not enough water!")
            return False
        elif milk_in_machine < 100:
            print("Sorry, not enough milk!")
            return False
        elif coffee_beans_in_machine < 12:
            print("Sorry, not enough coffee beans!")
            return False
        elif cups_of_coffee <= 0:
            print("Sorry, not enough cups!")
            return False
        else:
            print("I have enough resources, making you a coffee!")
            return True


def buy_coffee():
    global water_in_machine
    global milk_in_machine
    global coffee_beans_in_machine
    global cups_of_coffee
    global money

    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    type_coffee = input()
    if type_coffee == '1':
        if resources('espresso'):
            water_in_machine -= 250
            coffee_beans_in_machine -= 16
            money += 4
            cups_of_coffee -= 1
    elif type_coffee == '2':
        if resources('cappuccino'):
            water_in_machine -= 350
            milk_in_machine -= 75
            coffee_beans_in_machine -= 20
            money += 7
            cups_of_coffee -= 1
    elif type_coffee == '3':
        if resources('latte'):
            water_in_machine -= 200
            milk_in_machine -= 100
            coffee_beans_in_machine -= 12
            money += 6
            cups_of_coffee -= 1
    elif type_coffee == 'back':
        return 0


def take_money():
    global money
    print("I gave you", money)
    money = 0


while 1:
    print("What action (buy, fill, take, remaining, exit):")
    action = input()
    if action == 'buy':
        buy_coffee()
    elif action == 'fill':
        fill_machine()
    elif action == 'take':
        take_money()
    elif action == 'remaining':
        remaining()
    elif action == 'exit':
        break
