"""Function table_situation_check(): It creates current short version of table from full version and save booleans
for making dicision to continue or stoping players steps itterations"""


def table_situation_check(table):

    # Cases of win formulation
    cases_h_win_str = table.replace(" ", "")
    cases_h_win_str = cases_h_win_str.replace("|", "")
    cases_h_win = cases_h_win_str.split("\n")
    us_str2 = "".join(str(e) for e in cases_h_win)

    # Cases to win
    cases_v_win = [us_str2[0:9:3], us_str2[1:9:3], us_str2[2:9:3]]
    cases_d_win = [us_str2[0:9:4], us_str2[2:7:2]]
    cases_win = cases_h_win + cases_v_win + cases_d_win

    # X wins
    win_x = [True if val == "XXX" else False for i, val in enumerate(cases_win)]
    win1_x = any(win_x)  # X wins 1 and more times

    # O wins
    win_o = [True if val == "OOO" else False for i, val in enumerate(cases_win)]
    win1_o = any(win_o)  # O wins 1 and more times

    # X or O wins 1 and more times
    win1 = any([win1_x, win1_o])
    # X and O win 2 and more times
    win2 = all([win1_x, win1_o])

    # Check number of X minus number of O equal 1, or -1, or 0
    x_minus_o_num = abs(us_str2.count("X") - us_str2.count("O")) == 1 or abs(
        us_str2.count("X") - us_str2.count("O")) == 0

    # Check "_" containing in table
    table_cont = "_" in us_str2

    return cases_h_win, win1, table_cont, win2, x_minus_o_num, win1_x, win1_o
