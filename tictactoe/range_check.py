"""Function range_check(): It checks current inputed by player 2 coordinates numbers for a range between 1 and 3
considering the possibility of repeated separator and nonumbers error"""

# Functionss:
from separator_check import separator_check
from numbers_check import numbers_check


def range_check(row_coord_n, col_coord_n):

    # To check the range
    while not 0 <= row_coord_n <= 2 or not 0 <= col_coord_n <= 2:
        print("Coordinates should be from 1 to 3!")
        pl_step = input("Enter the coordinates: ")
        pl_step_list = pl_step.split(" ", 1)

        # To check the separator
        row_coord, col_coord = separator_check(pl_step_list)

        # To check - coordinates is numbers
        row_coord_n, col_coord_n = numbers_check(row_coord, col_coord)

    return row_coord_n, col_coord_n
