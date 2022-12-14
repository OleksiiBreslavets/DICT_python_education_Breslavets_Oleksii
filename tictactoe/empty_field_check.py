"""Function empty_field_check(): It checks current inputed by player 2 coordinates numbers between 1 and 3 for
occupining of current table field considering the possibility of repeated separator, nonumbers and out of range error"""

# Functionss:
from separator_check import separator_check
from numbers_check import numbers_check
from range_check import range_check


def empty_field_check(table_matrix, row_coord_n, col_coord_n):

    # To check field is empty or occupied
    while table_matrix[row_coord_n][col_coord_n] != "_":
        print("This cell is occupied! Choose another one!")
        pl_step = input("Enter the coordinates: ")
        pl_step_list = pl_step.split(" ", 1)

        # To check the separator
        row_coord, col_coord = separator_check(pl_step_list)

        # To check - coordinates is numbers
        row_coord_n, col_coord_n = numbers_check(row_coord, col_coord)

        # To check the range
        row_coord_n, col_coord_n = range_check(row_coord_n, col_coord_n)

    return row_coord_n, col_coord_n
