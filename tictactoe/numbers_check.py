"""Function numbers_check(): It checks current inputed by player 2 coordinates for numbers or not numbers considering
the possibility of repeated separator error"""

# Functionss:
from separator_check import separator_check


def numbers_check(row_coord, col_coord):

    # To check - coordinates is numbers
    while not row_coord.isnumeric() or not col_coord.isnumeric():
        print("You should enter numbers!")
        pl_step = input("Enter the coordinates: ")
        pl_step_list = pl_step.split(" ", 1)

        # To check the separator
        row_coord, col_coord = separator_check(pl_step_list)

    # String to number
    row_coord_n = int(row_coord) - 1
    col_coord_n = int(col_coord) - 1

    return row_coord_n, col_coord_n
