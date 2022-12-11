"""Function x_o_player_step(): It decides what player made a step and fills the field using the correct symbol"""


def x_o_player_step(table_vector_s, table_matrix, row_coord_n, col_coord_n):

    if (table_vector_s.count("X") - table_vector_s.count("O")) == 0:
        table_matrix[row_coord_n][col_coord_n] = "X"
    elif (table_vector_s.count("X") - table_vector_s.count("O")) == 1:
        table_matrix[row_coord_n][col_coord_n] = "O"

    return table_matrix
