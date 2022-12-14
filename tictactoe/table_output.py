"""Function table_output(): It creates and displays current full version of table (with borders and spaces)"""


def table_output(table_vector_s):

    border = "---------"
    table = " ".join(str(e) for e in list(table_vector_s))
    table = "| " + table[:5] + " |\n| " + table[6:11] + " |\n| " + table[12:] + " |"
    print(border + "\n" + table + "\n" + border)

    return table
