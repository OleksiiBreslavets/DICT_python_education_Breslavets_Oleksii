"""Function separator_check(): It checks current input of player step for correct separator between 2 coordinates"""


def separator_check(pl_step_list):

    # To check the separator
    while len(pl_step_list) == 1:
        print("Please use only \" \" (space) as separator between 2 coorinates. Try again.")
        pl_step = input("Enter the coordinates: ")
        pl_step_list = pl_step.split(" ", 1)
    else:
        # To save the coordinates
        row_coord = pl_step_list[0]
        col_coord = pl_step_list[1]

    return row_coord, col_coord
