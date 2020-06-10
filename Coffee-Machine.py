class CoffeeMachine:
    """A class of Coffee Machine"""
    coffee_options = {
        "espresso(1)": {"water": 250, "milk": 0, "coffee": 16, "price": 4},
        "latte(2)": {"water": 350, "milk": 75, "coffee": 20, "price": 7},
        "cappuccino(3)": {"water": 200, "milk": 100, "coffee": 12, "price": 6}
    }

    list_of_resources = [
        "disposable cups", "water", "milk", "coffee beans"
    ]

    def __init__(self,
                 water=0,
                 milk=0,
                 coffee_beans=0,
                 cups=0
                 ):
        """Amount of water in ml, milk in ml and coffee beans in grams"""
        self.water = water
        self.milk = milk
        self.coffee = coffee_beans
        self.cups = cups
        self.active = False
        self.coffee_type_bought = None
        self.money = 550

    def __repr__(self):
        return "The is an object of CoffeeMachine class. water = 0, milk = 0, coffee_beans = 0, cups = 0"

    def __str__(self):
        return """
The coffee machine has:\n{} of water\n{} of milk\n{} of coffee beans\n{} of disposable cups\n{} of money
        """.format(self.water, self.milk, self.coffee, self.cups, self.money)

    def __user_entry_into_coffee_option(self, user_entry):
        """This method takes the user input for the buy action and return dic of ingredients"""
        if user_entry == "1":
            return self.coffee_options["espresso(1)"]
        elif user_entry == "2":
            return self.coffee_options["latte(2)"]
        elif user_entry == "3":
            return self.coffee_options["cappuccino(3)"]
        else:
            return None

    def __check_for_resource(self, coffee_type):
        """This method checks if the machine has enough resources to make the particular coffee type"""
        if self.cups == 0:
            print("Sorry, not enough disposable cups!")
            return False

        coffee_option_ingredients = self.__user_entry_into_coffee_option(coffee_type)

        if coffee_option_ingredients is None:
            print("Unrecognised selection!")
            return False
        else:
            if self.water < coffee_option_ingredients["water"]:
                print("Sorry, not enough water!")
                return False
            elif self.coffee < coffee_option_ingredients["coffee"]:
                print("Sorry, not enough coffee beans!")
                return False
            elif self.milk < coffee_option_ingredients["milk"]:
                print("Sorry, not enough milk!")
                return False
            else:
                return True

    def __update_machine_state(self, coffee_type):
        """This method process buy order and update machine resources"""
        if self.__check_for_resource(coffee_type):  # checking if there is enough resources before proceeding
            print("I have enough resources, making you a coffee!")
            self.coffee_type_bought = coffee_type
            self.cups -= 1
            coffee_option_ingredients = self.__user_entry_into_coffee_option(coffee_type)
            self.money += coffee_option_ingredients["price"]
            self.water -= coffee_option_ingredients["water"]
            self.milk -= coffee_option_ingredients["milk"]
            self.coffee -= coffee_option_ingredients["coffee"]

    def __add_resources(self):
        """This method add resources to the machine"""
        water_input = int(input("Write how many ml of water do you want to add: "))
        self.water += water_input
        milk_input = int(input("Write how many ml of milk do you want to add: "))
        self.milk += milk_input
        coffee_input = int(input("Write how many grams of coffee beans do you want to add: "))
        self.coffee += coffee_input
        cups_input = int(input("Write how many disposable cups of coffee do you want to add: "))
        self.cups += cups_input

    def __reverse_update(self, coffee_type):
        """This method allow user to cancel order"""
        if self.coffee_type_bought is not None:
            self.cups += 1
            coffee_option_ingredients = self.__user_entry_into_coffee_option(coffee_type)
            self.money -= coffee_option_ingredients["price"]
            self.water += coffee_option_ingredients["water"]
            self.milk += coffee_option_ingredients["milk"]
            self.coffee += coffee_option_ingredients["coffee"]
            self.coffee_type_bought = None
        else:
            print("Sorry, you have not made any purchase")

    def __withdraw_money(self):
        """This method withdraw the money and set the attribute 'money to zero"""
        print(f"I gave you ${self.money}")
        self.money = 0

    def __buy(self):
        """This method allows you to issue the buy order"""
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
        self.__update_machine_state(coffee_type)

    def __back(self):
        """The method allow user to cancel order"""
        if self.coffee_type_bought is not None:
            self.__reverse_update(self.coffee_type_bought)
            self.coffee_type_bought = None
        else:
            print("Sorry, you have not made any order")

    def __remaining(self):
        """This method prints the status of the coffee machine"""
        print(self)

    def __switch_off_on(self):
        """This method turns the machine off if on and verse versa"""
        if not self.active:
            print()
            print("Turning machine on")
            self.active = True
        else:
            print()
            print("Turning machine off")
            self.active = False

    def select_action(self):
        """
        This method allow users to interact with the machine by selecting one of the following
        actions:buy, fill, take, remaining, exit, back
        """
        self.__switch_off_on()
        while self.active:
            print()
            action = input("Write action: buy, fill, withdraw, remaining, exit, or back?):__")
            if action == "buy":
                self.__buy()
            elif action == "fill":
                self.__add_resources()
            elif action == "withdraw":
                self.__withdraw_money()
            elif action == "remaining":
                self.__remaining()
            elif action == "back":
                self.__back()
            elif action == "exit":
                self.__switch_off_on()
            else:
                print("Sorry, action not recognise!")


# testing the code
machine = CoffeeMachine()
machine.select_action()
