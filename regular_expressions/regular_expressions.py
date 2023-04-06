"""Regular-expressions project: editor program"""

# Libraries
import re

# 6-th stage
print("\nREGULAR_EXPRESSIONS\n")  # Program name


class RegularExpressions:
    """
    Class RegularExpressions: The class represents the Regular-expressions program; its method takes a string as
    input; whenever the user types a string into the console, the program calls this method with one argument: the
    string the user types into the console; the class will only process input that comes to it through this method
    and its string argument.

        ...

        Attributes
        ----------
        user_string : str
            user inputed string.

        Methods
        -------
        input_check(us_sring: str):
            Checks the separator | in the inputed string.
        match_expr(us_str: str):
            Matches regular expression and string.
        match_each_pair_symbols(self, us_str: str):
            Calls the function from the first step for each character in the regular expression-string pair and returns
            True only if there is a match for each character.
        match_increment(self, us_str: str):
            Calls the function from the second step and matches pair with incremented (different start position) inputed
            row if the function from the second step return False.
    """

    def __init__(self, user_string):
        """
        Constructs all the necessary attributes for the resources status object.
        """
        self.user_string = user_string

    def input_check(self, us_sring: str) -> str:
        """
        Checks the separator | in the inputed string.
        """
        if us_sring == "!exit":
            exit()

        while not us_sring.count("|") == 1:
            us_sring = input("You must input string with 1 \"|\" separator. Please try again.\nInput: ")

        self.user_string = us_sring

        return us_sring

    def match_expr(self, us_str: str) -> bool:
        """
        Matches regular expression and string.
        """
        self.user_string = self.user_string
        regexpr = us_str.split("|")[0]
        string = us_str.split("|")[1]
        res = re.match(regexpr, string)
        return res is not None

    def match_each_pair_symbols(self, us_str: str) -> bool:
        """
        Calls the function from the first step for each character in the regular expression-string pair and returns
        True only if there is a match for each character.
        """
        self.user_string = self.user_string
        check_all: list[bool] = []

        if len(us_str.split("|")[0]) > len(us_str.split("|")[1]):
            res = False

        elif not regular.match_expr(us_str.split("|")[0][0] + "|" + us_str.split("|")[1][0]):
            res = False

        else:
            for i in range(len(us_str.split("|")[0])):
                pair = us_str.split("|")[0][i] + "|" + us_str.split("|")[1][i]
                check_all.append(regular.match_expr(pair))
            res = all(check_all)

        return res

    def match_increment(self, us_str: str) -> bool:
        """
        Calls the function from the second step and matches pair with incremented (different start position) inputed
        row if the function from the second step return False.
        """
        self.user_string = self.user_string
        index = us_str.find("|") + 1
        while len(us_str.split("|")[1]) > 0:
            res = regular.match_each_pair_symbols(us_str)
            if res:
                return res

            us_str = us_str[:index] + us_str[(index + 1):]

        return False


# The body of the main script is shown below!!!!!
if __name__ == '__main__':
    mystring = ""
    regular = RegularExpressions(mystring)

    while True:
        mystring = input("Input: ")
        mystring = regular.input_check(mystring)
        if "^" in mystring.split("|")[0] or "$" in mystring.split("|")[0] or "?" in mystring.split("|")[0] \
                or "*" in mystring.split("|")[0] or "+" in mystring.split("|")[0] \
                or "\\" in mystring.split("|")[0]:
            if "\\" == mystring.split("|")[0][0]:
                mystring = mystring.split("|")[0].replace("\\", "\\\\") + "|" + mystring.split("|")[1]
                if "\\\\.$" in mystring.split("|")[0]:
                    mystring = mystring.split("|")[0].replace("\\\\.$", ".*\\.") + "|" + mystring.split("|")[1]
                if "\\\\\\\\" == mystring.split("|")[0]:
                    mystring = mystring.split("|")[0].replace("\\\\", "\\") + "|" + mystring.split("|")[1]
            result = regular.match_expr(mystring)
        else:
            result = regular.match_increment(mystring)

        print(f"Output: {result}")
