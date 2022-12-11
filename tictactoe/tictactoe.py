"""Tictactoe project: simple game"""

# Functions
from table_output import table_output
from table_situation_check import table_situation_check
from separator_check import separator_check
from numbers_check import numbers_check
from range_check import range_check
from empty_field_check import empty_field_check
from vector import vector
from x_o_player_step import x_o_player_step
from res_cases_over import res_cases_over

# 5-th stage
print("\nTICTACTOE")  # Program name

start_table_vector_s = "_________"  # Empty table

# Output new table with separators
start_table = table_output(start_table_vector_s)

# Cases of win formulation
cases_h_win, win1, table_cont, win2, x_minus_o_num, win1_x, win1_o = table_situation_check(start_table)

while not win1 and table_cont and not win2 and x_minus_o_num:

    # Coordinatisation of table
    table_matrix = [list(val) for i, val in enumerate(cases_h_win)]
    table_vector_s = vector(table_matrix)

    # User step iputing the coordinates
    pl_step = input("Enter the coordinates: ")
    pl_step_list = pl_step.split(" ", 1)

    # To check the separator
    row_coord, col_coord = separator_check(pl_step_list)

    # To check - coordinates is numbers
    row_coord_n, col_coord_n = numbers_check(row_coord, col_coord)

    # To check the range
    row_coord_n, col_coord_n = range_check(row_coord_n, col_coord_n)

    # To check field is empty or occupied
    row_coord_n, col_coord_n = empty_field_check(table_matrix, row_coord_n, col_coord_n)

    table_matrix = x_o_player_step(table_vector_s, table_matrix, row_coord_n, col_coord_n)
    table_vector_s = vector(table_matrix)

    # Output new table with separators
    table = table_output(table_vector_s)

    # Cases of win formulation
    cases_h_win, win1, table_cont, win2, x_minus_o_num, win1_x, win1_o = table_situation_check(table)
else:
    # Results cases if game is over
    print(res_cases_over(win1, win2, win1_x, win1_o, table_cont, x_minus_o_num))
