from math import floor


class Machine:
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550
    espresso_availability = 0
    latte_availability = 0
    cappuccino_availability = 0

    def __init__(self):
        pass

    def check_ingredients(self, coffee_kind):
        if self.cups < 1:
            print("Sorry, not enough cups!")
            return False

        if coffee_kind == 'espresso':
            if self.water < 250:
                print("Sorry, not enough water!")
                return False
            elif self.beans < 16:
                print("Sorry, not enough coffee beans")
                return False
        elif coffee_kind == 'latte':
            if self.water < 350:
                print("Sorry, not enough water!")
                return False
            elif self.milk < 75:
                print("Sorry, not enough milk!")
                return False
            elif self.beans < 20:
                print("Sorry, not enough coffee beans")
                return False
        elif coffee_kind == 'cappuccino':
            if self.water < 200:
                print("Sorry, not enough water!")
                return False
            elif self.milk < 75:
                print("Sorry, not enough milk!")
                return False
            elif self.beans < 12:
                print("Sorry, not enough coffee beans")
                return False

        return True

    def availability(self):
        self.espresso_availability = min(floor(self.water / 250), floor(self.beans / 16), self.cups)
        self.latte_availability = min(floor(self.water / 350), floor(self.milk / 75), floor(self.beans / 20), self.cups)
        self.cappuccino_availability = min(floor(self.water / 200), floor(self.milk / 75), floor(self.beans / 12), self.cups)

    def buy_coffee(self):
        selection = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if selection == '1':
            if self.check_ingredients('espresso'):
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.cups -= 1
        elif selection == '2':
            if self.check_ingredients('latte'):
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.cups -= 1
        elif selection == '3':
            if self.check_ingredients('cappuccino'):
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.cups -= 1
        print()

    def fill_machine(self):
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:"))
        print()

    def take_money(self):
        print(f"I gave you ${self.money}")
        print()
        self.money = 0

    def print_states(self):
        print(f"""The coffee machine has:
        {self.water} of water
        {self.milk} of milk
        {self.beans} of coffee beans
        {self.cups} of disposable cups
        {self.money} of money
        Enough to make -- espresso: {self.espresso_availability} -- latte: {self.latte_availability} -- cappuccino: {self.cappuccino_availability}""")


def action(machine, selection):
    if selection == 'buy':
        machine.buy_coffee()
    elif selection == 'fill':
        machine.fill_machine()
    elif selection == 'take':
        machine.take_money()
    elif selection == 'remaining':
        machine.availability()
        machine.print_states()


m = Machine()
selection = input("Write action (buy, fill, take, remaining, exit):")
while selection != 'exit':
    print()
    action(m, selection)
    selection = input("Write action (buy, fill, take, remaining, exit):")
