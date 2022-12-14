"""Function res_cases_over(): It decides what is the result of the game over"""


def res_cases_over(win1, win2, win1_x, win1_o, table_cont, x_minus_o_num):

    # Results cases if game is over
    if not win1 and not table_cont and not win2 and x_minus_o_num:
        res = "Draw"
    elif win1_x and x_minus_o_num and not win2 and x_minus_o_num:
        res = "X wins"
    elif win1_o and x_minus_o_num and not win2 and x_minus_o_num:
        res = "O wins"
    else:
        res = "Impossible"

    return res
