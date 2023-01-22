"""Credit_calculator project: economic calculator program"""

# Libraries
import math
# import sys
import argparse

# 4-th stage
print("\nCREDIT_CALCULATOR\n")  # Program name


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


def par_check_func(inp_str1: str) -> int | float:
    """
    Checks if the inputed string can be converted to integer or floating-point decimal real number and more than 0,
    and implements reinput.

    Parameters:
    -------
        inp_str1 (str): String.

    Returns:
    -------
        par1 (int | float): A decimal integer or floating-point decimal real number.
    """
    if inp_str1 == "Enter the loan principal:\n> ":
        par1 = args["principal"]
        flag = True
    elif inp_str1 == "Enter the number of periods:\n> ":
        par1 = args["periods"]
        flag = True
    elif inp_str1 == "Enter the monthly payment:\n> ":
        par1 = args["payment"]
        flag = False
    elif inp_str1 == "Enter the loan interest:\n> ":
        par1 = args["interest"]
        flag = False
    else:
        print("Error!")
        exit()

    if flag:
        while not is_integer(par1):
            print("Please input the integer number. Try again.")
            par1 = input(inp_str1)
        par1 = int(par1)
        while not par1 > 0:
            print("Please input the positive number. Try again.")
            par1 = int(input(inp_str1))
    else:
        while not is_float(par1):
            print("Please input the floating-point number. Try again.")
            par1 = input(inp_str1)
        par1 = float(par1)
        while not par1 > 0:
            print("Please input the positive number. Try again.")
            par1 = float(input(inp_str1))

    return par1


def terminal_run_func() -> tuple[dict[str, any], str]:
    """
    Controls parameters configuration when the script is activating from the terminal and mode of calculation.

    Parameters:
    -------
        None.

    Returns:
    -------
        Tuple:
            args1 (dict[str, any]): Dictionary of string keys and anys;
            mode_calc1 (str): String.
    """
    # print('Number of arguments: {}'.format(len(sys.argv)))
    # print('Argument(s) passed: {}'.format(str(sys.argv)))

    # Construct the argument parser
    ap = argparse.ArgumentParser()

    # Add the arguments to the parser
    ap.add_argument("-a", "--type", type=str, required=False, help="first operand")  # required=True
    ap.add_argument("-b", "--principal", type=int, required=False, help="second operand")
    ap.add_argument("-c", "--periods", type=int, required=False, help="third operand")
    ap.add_argument("-d", "--interest", type=float, required=False, help="fourth operand")  # required=True
    ap.add_argument("-e", "--payment", type=float, required=False, help="fifth operand")
    args1 = vars(ap.parse_args())

    if str(args1["type"]) == "annuity":
        if args1["periods"] is None and args1["payment"] is not None and args1["principal"] is not None \
                and args1["interest"] is not None:
            mode_calc1 = "n"
        elif args1["payment"] is None and args1["periods"] is not None and args1["principal"] is not None \
                and args1["interest"] is not None:
            mode_calc1 = "a"
        elif args1["principal"] is None and args1["periods"] is not None and args1["payment"] is not None \
                and args1["interest"] is not None:
            mode_calc1 = "p"
        else:
            print("Incorrect parameters.")
            exit()

    elif str(args1["type"]) == "diff":
        if args1["payment"] is None and args1["periods"] is not None and args1["principal"] is not None \
                and args1["interest"] is not None:
            mode_calc1 = "a"
        else:
            print("Incorrect parameters.")
            exit()

    else:
        print("Incorrect parameters.")
        exit()

    return args1, mode_calc1


def period_mode_calc_func() -> tuple[int, float, float, int]:
    """
    Calculates number of periods.

    Parameters:
    -------
        None.

    Returns:
    -------
        Tuple:
            loan1 (int): A decimal integer;
            mon_pay1 (float): A floating-point decimal real number;
            loan_int1 (float): A floating-point decimal real number;
            months1 (int): A decimal integer.
    """
    loan1 = par_check_func("Enter the loan principal:\n> ")

    mon_pay1 = par_check_func("Enter the monthly payment:\n> ")

    loan_int1 = par_check_func("Enter the loan interest:\n> ")

    i = loan_int1 / (12 * 100)
    months1 = math.ceil(math.log((mon_pay1 / (mon_pay1 - i * loan1)), (1 + i)))

    years = math.floor(months1 / 12)
    months_part = months1 - years * 12

    if months1 == 0:
        print(f"It will take {years} years to repay this loan!")
    elif years == 0:
        print(f"It will take {months1} months to repay this loan!")
    elif months1 == 0 and years == 0:
        print(f"It will take nothing to repay this loan!")
    else:
        print(f"It will take {years} years and {months_part} months to repay this loan!")

    return loan1, mon_pay1, loan_int1, months1


def mon_pay_mode_calc_func() -> tuple[int, int | list[int], float, int]:
    """
    Calculates monthly payment.

    Parameters:
    -------
        None.

    Returns:
    -------
        Tuple:
            loan1 (int): A decimal integer;
            mon_pay1 (int | list[int]): A decimal integer or a list of a decimal integer's numbers;
            loan_int1 (float): A floating-point decimal real number;
            months1 (int): A decimal integer.
    """
    loan1 = par_check_func("Enter the loan principal:\n> ")

    months1 = par_check_func("Enter the number of periods:\n> ")

    loan_int1 = par_check_func("Enter the loan interest:\n> ")

    if str(args["type"]) == "annuity":
        i = loan_int1 / (12 * 100)
        mon_pay1 = math.ceil(loan1 * (i * ((1 + i) ** months1)) / (((1 + i) ** months1) - 1))

        print(f"Your monthly payment = {mon_pay1}")

    else:
        i = loan_int1 / (12 * 100)
        mon_pay1 = []
        for m in range(months1):
            mon_pay1.append(math.ceil(loan1 / months1 + i * (loan1 - (loan1 * ((m + 1) - 1)) / months1)))
            print(f"Month {(m + 1)}: payment is {mon_pay1[m]}")

    return loan1, mon_pay1, loan_int1, months1


def loan_mode_calc_func() -> tuple[int, float, float, int]:
    """
    Calculates loan.

    Parameters:
    -------
        None.

    Returns:
    -------
        Tuple:
            loan1 (int): A decimal integer;
            mon_pay1 (float): A floating-point decimal real number;
            loan_int1 (float): A floating-point decimal real number;
            months1 (int): A decimal integer.
    """
    mon_pay1 = par_check_func("Enter the monthly payment:\n> ")

    months1 = par_check_func("Enter the number of periods:\n> ")

    loan_int1 = par_check_func("Enter the loan interest:\n> ")

    i = loan_int1 / (12 * 100)
    loan1 = math.floor(mon_pay1 / ((i * ((1 + i) ** months1)) / (((1 + i) ** months1) - 1)))

    print(f"Your loan principal = {loan1}!")

    return loan1, mon_pay1, loan_int1, months1


def overpayment_func(loan1: int, mon_pay1: float | int | list[int], months1: int) -> int:
    """
    Calculates overpayment.

    Parameters:
    -------
        loan1 (int): A decimal integer;
        mon_pay1 (float | int | list[int]): A floating-point decimal real number or a decimal integer
            or a list of a decimal integer's numbers;
        months1 (int): A decimal integer.

    Returns:
    -------
        over_pay1 (int): A decimal integer.
    """
    if str(args["type"]) == "annuity":
        over_pay1 = round(mon_pay1 * months1 - loan1)
    else:
        over_pay1 = sum(mon_pay1) - loan1

    print(f"Overpayment = {over_pay1}")

    return over_pay1


# The body of the main script is shown below!!!!!
args, mode_calc = terminal_run_func()

if mode_calc == "n":
    loan, mon_pay, loan_int, months = period_mode_calc_func()

elif mode_calc == "a":
    loan, mon_pay, loan_int, months = mon_pay_mode_calc_func()

else:
    loan, mon_pay, loan_int, months = loan_mode_calc_func()

over_pay = overpayment_func(loan, mon_pay, months)
