"""Matrixprocessing project: driver program"""

# 6-th stage
print("\nMATRIXPROCESSING")  # Program name


def separator_check(pl_step_list: list[str], size_string: str) -> tuple[str, str]:
    """
    Checks current input of player step for correct separator.

    Parameters:
    -------
        pl_step_list (list[str]): List of a strings;
        size_string (str): String.

    Returns:
    -------
        Tuple:
            n_row (str): String;
            m_col (str): String.
    """
    while len(pl_step_list) == 1:
        print("Please use only \" \" (space) as separator. Try again.")
        pl_step = input(size_string)
        pl_step_list = pl_step.split(" ", 1)
    else:
        # To save the coordinates
        n_row = pl_step_list[0]
        m_col = pl_step_list[1]

    return n_row, m_col


def numbers_check(row: str, col: str, size_string: str) -> tuple[int, int]:
    """
    Checks current inputed 2 sizes for numbers or not numbers considering
    the possibility of repeated separator error.

    Parameters:
    -------
        row (str): String;
        col (str): String;
        size_string (str): String.

    Returns:
    -------
        Tuple:
            n_size (int): A decimal integer;
            m_size (int): A decimal integer.
    """
    while not row.isnumeric() or not col.isnumeric():
        print("You should enter numbers! Try again.")
        pl_step = input(size_string)
        pl_step_list = pl_step.split(" ", 1)

        # To check the separator
        row, col = separator_check(pl_step_list, size_string)

    # String to number
    n_size = int(row)
    m_size = int(col)

    return n_size, m_size


def range_check(row_num: int, col_num: int, size_string: str) -> tuple[int, int]:
    """
    Checks current inputed 2 sizes positivity considering the possibility
    of repeated separator and nonumbers error.

    Parameters:
    -------
        row_num (int): A decimal integer;
        col_num (int): A decimal integer;
        size_string (str): String.

    Returns:
    -------
        Tuple:
            row_num (int): A decimal integer;
            col_num (int): A decimal integer.
    """
    while not 0 < row_num or not 0 < col_num:
        print("Sizes of matrix should be 1 and more! Try again.")
        pl_step = input(size_string)
        pl_step_list = pl_step.split(" ", 1)

        # To check the separator
        row_sym, col_sym = separator_check(pl_step_list, size_string)

        # To check - coordinates is numbers
        row_num, col_num = numbers_check(row_sym, col_sym, size_string)

    return row_num, col_num


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


def matrix_input(n_rows: int, m_cols: int) -> list[list[int | float]]:
    """
    Implements user matrix input and checks it correctness.

    Parameters:
    -------
        n_rows (int): A decimal integer;
        m_cols (int): A decimal integer.

    Returns:
    -------
        matrix (list[list[int | float]]): List of a decimal integers' or floating-point decimal real numbers.
    """
    matrix = []
    flag_float = 0
    for y in range(n_rows):
        a = []
        flag_row_length = 0
        matrix_row = input("> ").split()
        if len(matrix_row) == m_cols:
            for x in range(m_cols):
                if is_integer(matrix_row[x]):
                    a.append(int(matrix_row[x]))
                elif is_float(matrix_row[x]):
                    a.append(float(matrix_row[x]))
                else:
                    print(f"Inputed elememt on {y + 1}-th row and {x + 1}-th column is not a number!")
                    flag_row_length = flag_row_length + 1
        else:
            print(f"Inputed matrix row has invalid length")
        while not len(matrix_row) == m_cols or not flag_row_length == 0:
            print("Try again.")
            a = []
            flag_row_length = 0
            matrix_row = input("> ").split()
            if len(matrix_row) == m_cols:
                for x in range(m_cols):
                    if is_integer(matrix_row[x]):
                        a.append(int(matrix_row[x]))
                    elif is_float(matrix_row[x]):
                        a.append(float(matrix_row[x]))
                    else:
                        print(f"Inputed elememt on {y + 1}-th row and {x + 1}-th column is not a number!")
                        flag_row_length = flag_row_length + 1
            else:
                print(f"Inputed matrix row has invalid length")
        else:
            matrix.append(a)

    for i in range(n_rows):
        for j in range(m_cols):
            if type(matrix[i][j]) == float:
                flag_float = flag_float + 1

    if flag_float > 0:
        matrix = [[float(matrix[i][j]) for j in range(m_cols)] for i in range(n_rows)]

    return matrix


def matrix_save(num: int) -> tuple[int, int, list[list[int | float]]]:
    """
    Implements user sizes and its matrix input.

    Parameters:
    -------
        num (int): A decimal integer (key).

    Returns:
    -------
        Tuple:
            rows (int): A decimal integer;
            cols (int): A decimal integer;
            matrix (list[list[int | float]]): List of a decimal integers' or floating-point decimal real numbers.
    """
    if num == 1:
        inp_str = " first "
    elif num == 2:
        inp_str = " second "
    elif num == 0:
        inp_str = " "
    else:
        print("ERROR!!!")
        exit()
    size_str = "Enter size of" + inp_str + "matrix: > "
    n_m_sizes = input(size_str).split(" ", 1)  # User input
    n_sym, m_sym = separator_check(n_m_sizes, size_str)  # To check the separator
    n_num, m_num = numbers_check(n_sym, m_sym, size_str)  # To check - sizes is numbers
    rows, cols = range_check(n_num, m_num, size_str)  # To check the range
    print("Enter" + inp_str + "matrix:")
    matrix = matrix_input(rows, cols)  # Implements user matrix input and checks it correctness.

    return rows, cols, matrix


def constant_input() -> int | float:
    """
    Implements user constant input.

    Parameters:
    -------
        None

    Returns:
    -------
        constant (int | float): A decimal integer or floating-point decimal real number.
    """
    constant = input("Enter constant: > ")
    while not is_float(constant):
        constant = input("Your constant is not number. Try again.\nEnter constant: > ")

    if is_integer(constant):
        constant = int(constant)
    else:
        constant = float(constant)

    return constant


def add_m_func() -> tuple[int, int, list[list[int | float]]]:
    """
    Makes 2 matrixes and sums them.

    Parameters:
    -------
        None

    Returns:
    -------
        Tuple:
            n_add (int): A decimal integer;
            m_add (int): A decimal integer;
            matrix_add (list[list[int | float]]): List of a decimal integers' or floating-point decimal real numbers.
    """
    # Matrix #1
    n1, m1, matrix1 = matrix_save(1)

    # Matrix #2
    n2, m2, matrix2 = matrix_save(2)  # Matrix #2

    # To add them
    if n1 == n2 and m1 == m2:
        matrix_add = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
        n_add = n1
        m_add = m1
    else:
        print("The operation cannot be performed.")
        matrix_add = []
        n_add = 0
        m_add = 0

    return n_add, m_add, matrix_add


def mult_c_func() -> tuple[int, int, list[list[int | float]]]:
    """
    Makes constant and multiplies it with first matrix.

    Parameters:
    -------
        None

    Returns:
    -------
        Tuple:
            n1 (int): A decimal integer;
            m1 (int): A decimal integer;
            matrix_mult_c (list[list[int | float]]): List of a decimal integers' or floating-point decimal real numbers.
    """
    # Matrix #1
    n1, m1, matrix1 = matrix_save(0)

    # User inputs constant
    const = constant_input()

    # Calculates multiplication
    matrix_mult_c = [[matrix1[i][j] * const for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

    return n1, m1, matrix_mult_c


"""Function mult_m_func(): It makes matrix2 and multiplies it with matrix1."""


def mult_m_func() -> tuple[int, int, list[list[int | float]]]:
    """
    Makes 2 matrixes and multiplies them.

    Parameters:
    -------
        None

    Returns:
    -------
        Tuple:
            n_mult (int): A decimal integer;
            m_mult (int): A decimal integer;
            matrix_mult_m (list[list[int | float]]): List of a decimal integers' or floating-point decimal real numbers.
    """
    # Matrix #1
    n1, m1, matrix1 = matrix_save(1)

    # Matrix #2
    n2, m2, matrix2 = matrix_save(2)  # Matrix #2

    # Multiplies Matrix #1 and Matrix #2
    if m1 == n2:
        n_mult = n1
        m_mult = m2
        a = m1
        matrix_mult_m = []

        for i in range(n_mult):
            row_mult_m = []

            for j in range(m_mult):
                vec_mult_m = [(matrix1[i][k] * matrix2[k][j]) for k in range(a)]
                sum_mult_m = sum(vec_mult_m)
                row_mult_m.append(sum_mult_m)

            matrix_mult_m.append(row_mult_m)

    else:
        print("The operation cannot be performed.")
        n_mult = 0
        m_mult = 0
        matrix_mult_m = []

    return n_mult, m_mult, matrix_mult_m


def transp_func() -> tuple[int, int, list[list[int | float]]]:
    """
    Transposes matrix1 in 4 ways.

    Parameters:
    -------
        None

    Returns:
    -------
        Tuple:
            n_t (int): A decimal integer;
            m_t (int): A decimal integer;
            matrix_t (list[list[int | float]]): List of a decimal integers' or floating-point decimal real numbers.
    """
    # Input way of transponation
    user_c_t = input("""
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
Your choice: > """)

    # Check correctnes of inputed command
    while not user_c_t == "1" and not user_c_t == "2" and not user_c_t == "3" \
            and not user_c_t == "4":
        print("Your choice is not correct!!! Try again.")
        user_c_t = input("""
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
Your choice: > """)

    # Matrix #1
    n1, m1, matrix1 = matrix_save(0)

    if user_c_t == "1":
        n_t = m1
        m_t = n1
        matrix_t = [[matrix1[j][i] for j in range(len(matrix1))] for i in range(len(matrix1[0]))]
    elif user_c_t == "2":
        n_t = m1
        m_t = n1
        matrix_t = [[matrix1[j][i] for j in range((len(matrix1) - 1), -1, -1)]
                    for i in range((len(matrix1[0]) - 1), -1, -1)]
    elif user_c_t == "3":
        n_t = n1
        m_t = m1
        matrix_t = [[matrix1[i][j] for j in range((len(matrix1[0]) - 1), -1, -1)] for i in range(len(matrix1))]
    else:
        n_t = n1
        m_t = m1
        matrix_t = [[matrix1[i][j] for j in range(len(matrix1[0]))] for i in range((len(matrix1) - 1), -1, -1)]

    return n_t, m_t, matrix_t


def determinant_func() -> bool | int:
    """
    Inputs determinant calculation of square n*n matrix with errors check.

    Parameters:
    -------
        None

    Returns:
    -------
        det (bool | int): A boolean or a decimal integer.
    """
    # Matrix #1
    n1, m1, matrix_1 = matrix_save(0)

    if not n1 == m1 or (n1 < 2 or m1 < 2):
        print("The operation cannot be performed.")
        det = False  # Bool does not print
    else:
        det = det_calc_func(matrix_1)
        if det == 0:
            print("Singular Matrix!")

    return det


def det_calc_func(matrix1: list[list[int | float]], res_det=0) -> int:
    """
    Calculates determinant.

    If the argument 'res_det' is passed, then it is appended after the main info.

    Parameters:
    -------
        matrix1 (list[list[int | float]]): List of a decimal integers' or floating-point decimal real numbers (the
        matrix to find the determinant for);
        res_det (int): A decimal integer (safely establish at each level; default is "0").

    Returns:
    -------
        res_det (int): A decimal integer (running res_det for the levels of recursion).
    """
    # Store indices in list for using later
    indices = list(range(len(matrix1)))

    # When at 2x2 submatrices recursive calls end
    if len(matrix1) == 2 and len(matrix1[0]) == 2:
        res_2x2 = matrix1[0][0] * matrix1[1][1] - matrix1[1][0] * matrix1[0][1]
        return res_2x2

    # Define submatrix for 0-column
    for fc in indices:  # For each 0-column find the submatrix
        matrix1_c = [[matrix1[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]  # Make a copy
        matrix1_c = matrix1_c[1:]  # Remove 1-st row
        height = len(matrix1_c)  # Find new max of index

        for i in range(height):  # For each remaining row of submatrix
            matrix1_c[i] = matrix1_c[i][0:fc] + matrix1_c[i][fc + 1:]  # 0-column elements

        sign = (-1) ** (fc % 2)  # To change signs for submatrix
        sub_det = det_calc_func(matrix1_c)  # Pass submatrix
        res_det += sign * matrix1[0][fc] * sub_det  # Total all returns

    return res_det


def inverse_matrix_func() -> tuple[int, int, list[list[int | float]]]:
    """
    Finds inverse matrix of input.

    Parameters:
    -------
        None

    Returns:
    -------
        Tuple:
            n_inv (int): A decimal integer;
            m_inv (int): A decimal integer;
            matrix_inv (list[list[int | float]]): List of a decimal integers' or floating-point decimal real numbers.
    """
    # Matrix #1
    n1, m1, matrix1 = matrix_save(0)
    if not n1 == m1 or (n1 < 2 or m1 < 2):
        print("The operation cannot be performed.")
        n_inv = 0
        m_inv = 0
        matrix_inv = False  # Bool is not printable
    else:
        det = det_calc_func(matrix1)
        n_inv = n1
        m_inv = m1
        if det == 0:
            print("The operation cannot be performed.")
            matrix_inv = False
        else:
            if n1 == 2 and m1 == 2:
                matrix_inv = [[matrix1[1][1] / det, -1 * matrix1[0][1] / det],
                              [-1 * matrix1[1][0] / det, matrix1[0][0] / det]]
            else:
                # Replaces each element of the original matrix with its algebraic complement
                matrix_inv = []
                for i_row in range(n1):
                    matrix_inv_row = []
                    for j_col in range(m1):
                        # Itteration of rows and cols removings
                        minor = [row[:j_col] + row[j_col + 1:] for row in (matrix1[:i_row] + matrix1[i_row + 1:])]
                        matrix_inv_row.append(((-1) ** (i_row + j_col)) * det_calc_func(minor))
                    matrix_inv.append(matrix_inv_row)

                # Transposes the resulting matrix - as a result, the union matrix will be obtained,
                matrix_inv = [[matrix_inv[j][i] for j in range(n_inv)] for i in range(m_inv)]

                # Divides each element of the union matrix by the determinant of the original matrix.
                matrix_inv = [[(matrix_inv[i_row][j_col] / det) for j_col in range(m_inv)] for i_row in range(n_inv)]

    return n_inv, m_inv, matrix_inv


def output_func(matrix_res: list[list[int | float]]):
    """
    Displays result matrix or single ineger or None.

    Parameters:
    -------
        matrix_res (list[list[int | float]]): List of a decimal integers' or floating-point decimal real numbers.

    Returns:
    -------
        None
    """
    if type(matrix_res) == list and not len(matrix_res) == 0:
        print("The result is:")
        list_str = [[str(matrix_res[i][j]) for j in range(len(matrix_res[0]))] for i in range(len(matrix_res))]
        flag_int = [[True if ((list_str[i][j][len(list_str[i][j]) - 1] == "0")
                              and (list_str[i][j][len(list_str[i][j]) - 2] == ".")) else False
                     for j in range(len(matrix_res[0]))] for i in range(len(matrix_res))]

        # If output matrix can be integer but visualise like float
        if all(flag_int):
            list_str = [[list_str[i][j].replace(".0", "")
                         for j in range(len(matrix_res[0]))] for i in range(len(matrix_res))]
            temp_res = list_str
        else:
            temp_res = matrix_res

        list_res = "\n".join(str(e) for e in temp_res)
        str_res = list_res.replace("[", "").replace("]", "").replace(",", "").replace("\'", "")
        print(str_res)
    elif (type(matrix_res) == int or type(matrix_res) == float) and not type(matrix_res) == list:
        print("The result is:")
        print(matrix_res)


def main_menu_func() -> str:
    """
    Implements input of the main menu command and checks it.

    Parameters:
    -------
        None

    Returns:
    -------
        us_command (str): String.
    """
    # User inpu initial command
    us_command = input("""
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
Your choice: > """)

    # Check correctnes of inputed command
    while not us_command == "1" and not us_command == "2" and not us_command == "3" \
            and not us_command == "4" and not us_command == "5" and not us_command == "6" and not us_command == "0":
        print("Your choice is not correct!!! Try again.")
        us_command = input("""
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
Your choice: > """)

    return us_command


# The body of the main script is shown below!!!!!
# Initial command of user
us_com = main_menu_func()

# Loop of main menu
while not us_com == "0":

    if us_com == "1":
        n, m, matrix_out = add_m_func()
    elif us_com == "2":
        n, m, matrix_out = mult_c_func()
    elif us_com == "3":
        n, m, matrix_out = mult_m_func()
    elif us_com == "4":
        n, m, matrix_out = transp_func()
    elif us_com == "5":
        matrix_out = determinant_func()
    else:
        n, m, matrix_out = inverse_matrix_func()

        # Output
    output_func(matrix_out)

    # Input new command while not "Exit"
    us_com = main_menu_func()
