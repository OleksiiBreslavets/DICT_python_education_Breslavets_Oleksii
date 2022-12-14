"""Function vector(): It creates current short-vector version of table (without borders and spaces) using matrix of
table (list of lsts)"""


def vector(table_matrix):

    table_vector = [item for sublist in table_matrix for item in sublist]
    table_vector_s = "".join(str(e) for e in table_vector)

    return table_vector_s
