"""Coffeemachine project: driver program"""

# 6-th stage
print("\nCOFFEEMACHINE")  # Program name

# Initial number of resources
main_resources = [400, 540, 120, 9, 550]


class CoffeeMachine:
    """
    Class CoffeeMachine: The class represents the coffee machine; its method takes a string as input; whenever the
    user types a string into the console, the program calls this method with one argument: the string the user types
    into the console; the class will only process input that comes to it through this method and its string argument.

    ...

    Attributes
    ----------
    main_res : list[int]
        detected resorses status of coffeemachine

    Methods
    -------
    action_control(user_word="", acts="error", act_number=0):
        Saves user interface status flag in current moment.
    buy():
        Calculates resources after 1 cup of some type of coffee.
    fill():
        Static method. Adds some resource to coffeemachine.
    take():
        Takes all the money out of the coffeemachine.
    remaining():
        Prints all resuorces in the coffeemachine now.
    input_control(user_com="_", user_cof="_"):
        Checks input errors for different menus.
    coffeemachine_do_something(act_num2=0):
        Coffeemachine do some action in cycle.
    """
    # Number of resources for 1 cup of espresso
    res_esp = {"water": 250, "milk": 0, "beans": 16, "cups": 1, "money": 4}
    # Number of resources for 1 cup of latte
    res_lat = {"water": 350, "milk": 75, "beans": 20, "cups": 1, "money": 7}
    # Number of resources for 1 cup of cappuccino
    res_cap = {"water": 200, "milk": 100, "beans": 12, "cups": 1, "money": 6}

    def __init__(self, main_res):
        """
        Constructs all the necessary attributes for the resources status object.

        Parameters
        ----------
            main_res : list[int]
                detected resources status of coffeemachine
        """
        self.main_res = main_res

    def action_control(self, user_word="") -> tuple[str, int]:
        """
        Saves user interface status flag in current moment.

        If the argument 'user_word' is passed, then it is appended after the main info.

        Parameters
        ----------
        user_word : str, optional
            More info to be displayed (default is "")

        Returns
        -------
        Tuple:
             acts (str): String;
             act_number (int): A decimal integer.
        """
        self.main_res = self.main_res

        if user_word == "buy" or user_word == "fill" or user_word == "take" \
                or user_word == "remaining" or user_word == "exit":
            acts = "main_menu"
        elif user_word == "1" or user_word == "2" or user_word == "3" or user_word == "back":
            acts = "coffee_buy"
        else:
            acts = "error"

        if user_word == "buy":
            act_number = 1
        elif user_word == "fill":
            act_number = 2
        elif user_word == "take":
            act_number = 3
        elif user_word == "remaining":
            act_number = 4
        elif user_word == "exit":
            act_number = 5
        elif user_word == "1":
            act_number = 6
        elif user_word == "2":
            act_number = 7
        elif user_word == "3":
            act_number = 8
        elif user_word == "back":
            act_number = 9
        else:
            act_number = 0

        return acts, act_number

    def buy(self, coffee_command: int) -> list[int]:
        """
        Calculates resources after 1 cup of some type of coffee.

        Parameters:
        -------
            self.main_res (list[int]): List of a decimal integers';
            coffee_command (int): A decimal integers'.
            CoffeeMachine.res_esp dict[str, int]: Dictionary of string keys and decimal integers' values
            CoffeeMachine.res_lat dict[str, int]: Dictionary of string keys and decimal integers' values
            CoffeeMachine.res_cap dict[str, int]: Dictionary of string keys and decimal integers' values

        Returns:
        -------
            self.main_res (list[int]): List of a decimal integers'.
        """

        def unpuck_func(water, milk, beans, cups, money):
            return [water, milk, beans, cups, money]

        if coffee_command == 6:
            coffee_res = unpuck_func(**CoffeeMachine.res_esp)  # 1 - espresso,
        elif coffee_command == 7:
            coffee_res = unpuck_func(**CoffeeMachine.res_lat)  # 2 - latte,
        else:
            coffee_res = unpuck_func(**CoffeeMachine.res_cap)  # 3 - cappuccino.

        d_res = [(v1 - v2) for v1, v2 in zip(self.main_res, coffee_res)]  # Subtract resources for 1 cup of coffee
        d_res[4] = self.main_res[4] + coffee_res[4]  # Add money for 1 cup of coffee

        if d_res[0] >= 0 and d_res[1] >= 0 and d_res[2] and d_res[3]:
            print("I have enough resources, making you a coffee!")
            self.main_res = [val for val in d_res]
        elif d_res[0] < 0:
            print("Sorry, not enough water!")
        elif d_res[1] < 0:
            print("Sorry, not enough milk!")
        elif d_res[2] < 0:
            print("Sorry, not enough coffee beans!")
        elif d_res[3] < 0:
            print("Sorry, not enough disposable coffee cups!")
        else:
            print("Sorry, not enough resorces!")

        return self.main_res

    def fill(self, i: int, str1: str, add: str) -> int:
        """
        Adds some resource to coffeemachine.

        Parameters:
        -------
            self.main_res (list[int]): List of a decimal integers';
            i (int): A decimal integer;
            str1 (str): String;
            add (int): String.

        Returns:
        -------
            self.main_res[i] (int): A decimal integers'.
        """
        while not add.isnumeric() or int(add) < 0:
            print("Number of this resource must be numeric and positive!!!")
            add = input(str1)
        else:
            add = int(add)
            self.main_res[i] = self.main_res[i] + add

        return self.main_res[i]

    def take(self):
        """
        Takes all the money out of the coffeemachine.

        Parameters:
        -------
            self.main_res (list[int]): List of a decimal integers'.

        Returns:
        -------
            self.main_res (list[int]): List of a decimal integers'.
        """
        print(f"I gave you {self.main_res[4]}")
        self.main_res[4] = 0

        return self.main_res

    def remaining(self):
        """
        Prints all resuorces in the coffeemachine now.

        Parameters:
        -------
            self.main_res (list[int]): List of a decimal integers'.

        Returns:
        -------
            self.main_res (list[int]): List of a decimal integers'.
        """
        print(f"""\nThe coffee machine has:
        {self.main_res[0]} ml of water
        {self.main_res[1]} ml of milk
        {self.main_res[2]} g of coffee beans
        {self.main_res[3]} of disposable cups
        {self.main_res[4]} of money""")

        return self.main_res

    def input_control(self, user_com="_", user_cof="_") -> tuple[str, int]:
        """
        Checks input errors for different menus.

        If the argument 'user_com' is passed, then it is appended after the main info.
        If the argument 'user_cof' is passed, then it is appended after the main info.

        Parameters
        ----------
        user_com : str, optional
            More info to be displayed (default is "_")
        user_cof : str, optional
            More info to be displayed (default is "_")

        Returns
        -------
        Tuple:
             acts (str): String;
             act_number (int): A decimal integer.
        """
        self.main_res = self.main_res
        if not user_com == "_" and user_cof == "_":
            menu1, act_num1 = coffee_machine.action_control(user_com)

            while any([act_num1 == 0, act_num1 == 6, act_num1 == 7, act_num1 == 8, act_num1 == 9]):
                user_com = input("The input is unknown!!! Please try again.\nWrite action (buy, fill, take, remaining, "
                                 "exit):\n> ")
                menu1, act_num1 = coffee_machine.action_control(user_com)

        elif user_com == "_" and not user_cof == "_":
            menu1, act_num1 = coffee_machine.action_control(user_cof)

            while any([act_num1 == 0, act_num1 == 1, act_num1 == 2, act_num1 == 3, act_num1 == 4, act_num1 == 5]):
                user_cof = input(
                    "Inputed coffee is unknown!!! Please try again (type 1, 2, 3, or back).\nWhat do you "
                    "want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:\n> ")
                menu1, act_num1 = coffee_machine.action_control(user_cof)

        else:
            menu1 = "error"
            act_num1 = 0
            print("Menu error!!!")

        return menu1, act_num1

    def coffeemachine_do_something(self, act_num2=0):
        """
        Coffeemachine do some action in cycle.

        If the argument 'act_num2' is passed, then it is appended after the main info.

        Parameters:
        -------
            act_num2 (int): A decimal integer (default is 0).

        Returns:
        -------
            self.main_res (list[int]): List of a decimal integers'.
        """
        while not act_num2 == 5:
            if act_num2 == 1:
                user_command2 = "_"
                coffee_type2 = input(
                    "\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main "
                    "menu:\n> ")
                menu2, act_num2 = coffee_machine.input_control(user_command2, coffee_type2)

                if act_num2 == 6 or act_num2 == 7 or act_num2 == 8:
                    self.main_res = coffee_machine.buy(act_num2)

            elif act_num2 == 2:
                # User input and resources filling
                water_str = "\nWrite how many ml of water you want to add:\n> "
                water_add = input(water_str)
                self.main_res[0] = coffee_machine.fill(0, water_str, water_add)

                milk_str = "Write how many ml of milk you want to add:\n> "
                milk_add = input(milk_str)
                self.main_res[1] = coffee_machine.fill(1, milk_str, milk_add)

                beans_str = "Write how many grams of coffee beans you want to add:\n> "
                beans_add = input(beans_str)
                self.main_res[2] = coffee_machine.fill(2, beans_str, beans_add)

                cups_str = "Write how many disposable coffee cups you want to add:\n> "
                cups_add = input(cups_str)
                self.main_res[3] = coffee_machine.fill(3, cups_str, cups_add)

            elif act_num2 == 3:
                self.main_res = coffee_machine.take()

            elif act_num2 == 4:
                self.main_res = coffee_machine.remaining()

            user_command2 = input("\nWrite action (buy, fill, take, remaining, exit):\n> ")
            coffee_type2 = "_"
            menu2, act_num2 = coffee_machine.input_control(user_command2, coffee_type2)

        return self.main_res


# The body of the main script is shown below!!!!!
coffee_machine = CoffeeMachine(main_resources)

user_command = input("\nWrite action (buy, fill, take, remaining, exit):\n> ")
coffee_type = "_"
menu, act_num = coffee_machine.input_control(user_command, coffee_type)

main_resources = coffee_machine.coffeemachine_do_something(act_num)
