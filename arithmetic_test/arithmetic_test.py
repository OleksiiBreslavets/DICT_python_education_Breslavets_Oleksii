"""Arithmetic_test project: test program"""

# Libraries
import random
import operator
from os.path import exists as file_exists

# 3-rd stage
print("\nARITHMETIC_TEST\n")  # Program name


def test_1st_func():
    """
    Implements question of 1st level random aritmetic operation.

    Parameters:
    -------
        None

    Returns:
    -------
        answer (int | float): A decimal integer or floating-point decimal real number.
    """
    parameter1 = random.randint(2, 9)
    parameter2 = random.randint(2, 9)
    operation_key = {"+": operator.add, "-": operator.sub, "*": operator.mul}
    op = random.choice(list(operation_key.keys()))
    answer = operation_key.get(op)(parameter1, parameter2)
    print(f"{parameter1} {op} {parameter2}")

    return answer


def test_2nd_func():
    """
    Implements question of 2nd level random squaring.

    Parameters:
    -------
        None

    Returns:
    -------
        answer (int | float): A decimal integer or floating-point decimal real number.
    """
    parameter1 = random.randint(11, 29)
    operation_key = {"**": operator.pow}
    op = list(operation_key.keys())[0]
    answer = operation_key.get(op)(parameter1, 2)
    print(f"{parameter1}")

    return answer


def test_3rd_func():
    """
    Implements question of 3rd level random exponentiation.

    Parameters:
    -------
        None

    Returns:
    -------
        answer (int | float): A decimal integer or floating-point decimal real number.
    """
    parameter1 = random.randint(11, 29)
    parameter2 = random.randint(2, 9)
    operation_key = {"**": operator.pow}
    op = list(operation_key.keys())[0]
    answer = operation_key.get(op)(parameter1, parameter2)
    print(f"Raise {parameter1} to the power of {parameter2}")

    return answer


def is_float(element: any) -> bool:
    """
    Checks if the inputed string can be converted to float. If you expect None to be passed:

    Parameters:
    -------
        element (any): Any.

    Returns:
    -------
        (bool)
    """
    if element is None:
        return False
    try:
        float(element)
        return True
    except ValueError:
        return False


def is_integer(element: any) -> bool:
    """
    Checks if the inputed string can be converted to integer. If you expect None to be passed:

    Parameters:
    -------
        element (any): Any.

    Returns:
    -------
        (bool)
    """
    if element is None:
        return False
    try:
        int(element)
        return True
    except ValueError:
        return False


def test_1_compare_func(lev: str) -> bool:
    """
    Implements comparation of true question answer and user input.

    Parameters:
    -------
        lev (str): String.

    Returns:
    -------
        Boolean.
    """
    if lev == "1":
        answer = test_1st_func()
    elif lev == "2":
        answer = test_2nd_func()
    else:
        answer = test_3rd_func()
    guess = input("> ")
    while not is_float(guess):
        print("Wrong format! Try again.")
        guess = input("> ")
    guess = float(guess)

    return guess == answer


def test_series_func(lev: str) -> int:
    """
    Implements 5 question and marks.

    Parameters:
    -------
        lev (str): String.

    Returns:
    -------
        score (int): A decimal integer.
    """
    score = 0
    for i in range(5):
        checking = test_1_compare_func(lev)
        if checking:
            score += 1
            print("Right!")
        else:
            print("Wrong!")

    return score


def level_inp_func():
    """
    Implements user level input and return levels key.

    Parameters:
    -------
        None

    Returns:
    -------
        lev (str): String.
    """
    lev = input("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
3 - raise to the power\n> """)
    while not lev == "1" and not lev == "2" and not lev == "3":
        print("Incorrect format.")
        lev = input("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
3 - raise to the power\n> """)

    return lev


def file_ex_save_func(name: str, mark2: int, lev: str, des: str) -> None:
    """
    Checks and saves the file.

    Parameters:
    -------
        name (str): String;
        mark2 (int): A decimal integer;
        lev (str): String;
        des (str): String.

    Returns:
    -------
        None
    """
    if file_exists("results.txt"):
        with open('results.txt', 'a+t', encoding='utf-8') as my_file:
            my_file.write(f"\n{name}: {mark2}/5 in level {lev}{des}")
    else:
        with open('results.txt', 'w+t', encoding='utf-8') as my_file:
            my_file.write(f"{name}: {mark2}/5 in level {lev}{des}")


def high_level_func(mark2: int, lev: str) -> tuple[int, str]:
    """
    Checks and saves the file.

    Parameters:
    -------
        mark2 (int): A decimal integer;
        lev (str): String.

    Returns:
    -------
        mark2 (int): A decimal integer;
        lev (str): String.
    """
    if mark2 == 5:
        if lev == "1":
            us_ch = input("Your score for passing the first level is perfect. Would you like to try the "
                          "second level? Enter yes or no.\n> ")
            if us_ch == "yes" or us_ch == "YES" or us_ch == "y" or us_ch == "Yes":
                mark2 = test_series_func("2")
                save_file_func(mark2, "2")
        elif lev == "2":
            us_ch = input("Your score for passing the second level is perfect. Would you like to try the "
                          "therd level? Enter yes or no.\n> ")
            if us_ch == "yes" or us_ch == "YES" or us_ch == "y" or us_ch == "Yes":
                mark2 = test_series_func("3")
                save_file_func(mark2, "3")

    return mark2, lev


def save_file_func(mark2: int, lev: str) -> None:
    """
    Saves the result to a file.

    Parameters:
    -------
        mark2 (int): A decimal integer;
        lev (str): String.

    Returns:
    -------
        None
    """
    choice = input(f"Your mark is {mark2}/5. Would you like to save the result? Enter yes or no.\n> ")
    if choice == "yes" or choice == "YES" or choice == "y" or choice == "Yes":
        name = input(f"What is your name?\n> ")
        while not name.isalpha() or not name.istitle() or len(name) <= 1:
            print("Please input your name in a titled alphabetic string.")
            name = input(f"What is your name?\n> ")

        print("The results are saved in \"results.txt\".")

        if lev == "1":
            des = " (simple aritmetic operation)"

            file_ex_save_func(name, mark2, lev, des)

            high_level_func(mark2, lev)

        elif lev == "2":
            des = " (squaring)"

            file_ex_save_func(name, mark2, lev, des)

            high_level_func(mark2, lev)

        else:
            des = " (pow)"

            file_ex_save_func(name, mark2, lev, des)

    else:
        exit()


# The body of the main script is shown below!!!!!
level = level_inp_func()
mark = test_series_func(level)
save_file_func(mark, level)
