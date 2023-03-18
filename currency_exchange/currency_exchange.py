"""Currency exchange project: calculation program"""

# Libraries
import json
from json import JSONDecodeError
import requests

# 4-th stage
print("\nCURRENCY_EXCHANGE\n")  # Program name


class CurrencyExchange:
    """
        Class CurrencyExchange: The class represents the Currency exchange program; its method takes a string as input;
        whenever the user types a string into the console, the program calls this method with one argument:
        the string the user types into the console; the class will only process input that comes to it through this
        method and its string argument.

        ...

        Attributes
        ----------
        money : list[float, float, float]
            detected money of user coin.

        Methods
        -------
        calc_money_to_receive():
            Calculates transaction user money to other types money.
        is_float(element: any):
            Checks if the inputed string can be converted to float. If you expect None to be passed.
        str_to_float(sys_str):
            Converts string to floating-point decimal real number.
        check_input(sys_str: str):
            Checks user input about float number and range more 0.
        users_money(self, sys_str: str):
            Defines users money code and cache data for transfering.
        rate_and_money_to_receive(self, sys_str: str, inp_money_cach: dict) -> tuple[str, float]:
            Defines money code for transfering and exchange rate.
    """

    def __init__(self, money):
        """
        Constructs all the necessary attributes for the resources status object.

        Parameters:
        -------
            money : list[float, float, float]
                detected money of user coin.
        """
        self.money = money

    def calc_money_to_receive(self) -> tuple[float, float, float]:
        """
        Calculates transaction user money to other types money.

        Parameters:
        -------
            self.money (list[float, float, float]): Tuple of a floating-point decimal real numbers.

        Returns:
        -------
            Tuple:
                mycoin (float): A floating-point decimal real number.
                exrait (float): A floating-point decimal real number.
                dollars (float): A floating-point decimal real number.
        """
        mycoin: float = self.money[0]
        exrait: float = self.money[1]
        self.money[2] = 0
        dollars: float = round(mycoin * exrait, 2)
        self.money = [mycoin, exrait, dollars]

        return mycoin, exrait, dollars

    def is_float(self, element: any) -> bool:
        """
        Checks if the inputed string can be converted to float. If you expect None to be passed.

        Parameters:
        -------
            element (any): Any.

        Returns:
        -------
            (bool)
        """
        self.money = self.money
        if element is None:
            return False
        try:
            float(element)
            return True
        except ValueError:
            return False

    def str_to_float(self, sys_str: str) -> float:
        """
        Converts string to floating-point decimal real number.

        Parameters:
        -------
            sys_str (str): String.

        Returns:
        -------
            num_float (float): A floating-point decimal real number more than 0.
        """
        self.money = self.money
        us_str = input(sys_str)
        if us_str == "!exit":
            exit()
        while not bank.is_float(us_str):
            print('Wrong input. Enter a number!')
            us_str = input(sys_str)

        num_float = float(us_str)

        return num_float

    def check_input(self, sys_str: str) -> float:
        """
        Checks user input about float number and range more 0.

        Parameters:
        -------
            sys_str (str): String.

        Returns:
        -------
            num_float (float): A floating-point decimal real number more than 0.
        """
        num_float = bank.str_to_float(sys_str)

        while num_float <= 0:
            print("Inputed number should be grater 0!")
            num_float = bank.str_to_float(sys_str)

        self.money[0] = num_float

        return num_float

    def users_money(self, sys_str: str) -> tuple[str, dict]:
        """
        Defines users money code and cache data for transfering.

        Parameters:
        -------
            sys_str (str): String.

        Returns:
        -------
            Tuple:
                inp_money_code (str): String;
                inp_money_cach (dict): Dictionary.
        """
        self.money = self.money
        inp_money_cach = {}
        inp_money_code = ""
        while True:
            try:
                inp_money_code = input(sys_str).lower()
                if inp_money_code == "!exit":
                    exit()
                print(f"Checking {inp_money_code.upper()} in the cache...")
                response = requests.get(f"http://www.floatrates.com/daily/{inp_money_code}.json")
                inp_money_cach = json.loads(response.text)
                if not len(inp_money_cach) == 0:
                    print(f"{inp_money_code.upper()} is in the cache!")
                    break
            except JSONDecodeError:
                print("Sorry, but it is not in the cache!")
                continue

        return inp_money_code, inp_money_cach

    def rate_and_money_to_receive(self, sys_str: str, inp_money_cach: dict) -> tuple[str, float]:
        """
        Defines money code for transfering and exchange rate.

        Parameters:
        -------
            sys_str (str): String.

        Returns:
        -------
            Tuple:
                out_money_code (str): String;
                exrate (float): A floating-point decimal real number.
        """
        out_money_code = ""
        exrate: float = 0
        while True:
            try:
                out_money_code = input(sys_str).lower()
                if out_money_code == "!exit":
                    exit()
                print(f"Checking {out_money_code.upper()} in the cache...")
                exrate = float(inp_money_cach[out_money_code]["rate"])
                if not exrate == 0:
                    print(f"{out_money_code.upper()} is in the cache!")
                    break
            except KeyError:
                print("Sorry, but it is not in the cache!")
                continue

        self.money[1] = exrate

        return out_money_code, exrate


# The body of the main script is shown below!!!!!
if __name__ == '__main__':
    mymoney = [0.0, 0.0, 0.0]
    bank = CurrencyExchange(mymoney)

    sys_string = "Please input the code of your money:\n> "
    input_money_code, input_money_cach = bank.users_money(sys_string)

    while True:
        print("You can input the comand \"!exit\" to stop the calculation cycle.")
        sys_string = "Please enter the code of the money you want to receive:\n> "
        output_money_code, exchange_rate = bank.rate_and_money_to_receive(sys_string, input_money_cach)

        sys_string = "Please input the amount of your money:\n> "
        mycoins = bank.check_input(sys_string)

        output_money = bank.calc_money_to_receive()[2]
        print(f"You received {output_money} {output_money_code.upper()} from {mycoins} {input_money_code.upper()}.")
