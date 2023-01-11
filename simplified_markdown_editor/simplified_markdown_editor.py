"""Simplified_markdown_editor project: text editor program"""

# 4-th stages
print("\nSIMPLIFIED_MARKDOWN_EDITOR")  # Program name


def input_func(prelim_str="") -> str:
    """
    Implements input of the formatting type or special command and checks it.

    Parameters:
    -------
        prelim_str (str): String.

    Returns:
    -------
        us_inp (str): String.
    """
    # User input
    us_inp = input(prelim_str + "Choose a formatter: > ")
    while not us_inp == "!help" and not us_inp == "!done" and not us_inp == "plain" and not us_inp == "bold" \
            and not us_inp == "italic" and not us_inp == "header" and not us_inp == "link" \
            and not us_inp == "inline-code" and not us_inp == "ordered-list" and not us_inp == "unordered-list" \
            and not us_inp == "new-line":
        print("Unknown formatting type or command")
        us_inp = input("Choose a formatter: > ")

    return us_inp


def help_func():
    """
    Displays help-message.

    Parameters:
    -------
        None

    Returns:
    -------
        None
    """
    print("""Available formatters: plain bold italic header link inline-code ordered-
list unordered-list new-line
Special commands: !help !done""")


def plain_text_func(all_text: str) -> str:
    """
    Saves user inputed text to the added earlier.

    Parameters:
    -------
        all_text (str): String.

    Returns:
    -------
        res_text (str): String.
    """
    add_plain_text = input("Text: > ")
    if not len(all_text) == 0:
        res_text = all_text + "\n" + add_plain_text
    else:
        res_text = add_plain_text

    return res_text


def bold_func(all_text: str) -> str:
    """
    Saves user inputed text, transfer it to bold, adds it to the text earlier.

    Parameters:
    -------
        all_text (str): String.

    Returns:
    -------
        res_text (str): String.
    """
    add_plain_text = input("Text: > ")
    bolded_text = "**" + add_plain_text + "**"
    if not len(all_text) == 0:
        res_text = all_text + "\n" + bolded_text
    else:
        res_text = bolded_text

    return res_text


def italic_func(all_text: str) -> str:
    """
    Saves user inputed text, transfer it to italic, adds it to the text earlier.

    Parameters:
    -------
        all_text (str): String.

    Returns:
    -------
        res_text (str): String.
    """
    add_plain_text = input("Text: > ")
    italiced_text = "*" + add_plain_text + "*"
    if not len(all_text) == 0:
        res_text = all_text + "\n" + italiced_text
    else:
        res_text = italiced_text

    return res_text


def header_func(all_text: str) -> str:
    """
    Saves user inputed header with spec-symbols, adds it to the text earlier.

    Parameters:
    -------
        all_text (str): String.

    Returns:
    -------
        res_text (str): String.
    """
    level = input("Level: > ")
    while not level.isnumeric():
        print("Inputed level should be numeric. Try again.")
        level = input("Level: > ")
    level = int(level)
    while not 1 <= level <= 6:
        print("The level should be within the range of 1 to 6. Try again.")
        level = input("Level: > ")

    add_plain_text = input("Text: > ")

    header_text = level * "#" + " " + add_plain_text
    if not len(all_text) == 0:
        res_text = all_text + "\n" + header_text
    else:
        res_text = header_text

    return res_text


def link_func(all_text: str) -> str:
    """
    Saves user inputed web-link, adds it to the text earlier.

    Parameters:
    -------
        all_text (str): String.

    Returns:
    -------
        res_text (str): String.
    """
    libel_text = input("Label: > ")
    url_text = input("URL: > ")
    link_text = "[" + libel_text + "](" + url_text + ")"
    if not len(all_text) == 0:
        res_text = all_text + "\n" + link_text
    else:
        res_text = link_text

    return res_text


def inline_code_func(all_text: str) -> str:
    """
    Saves user inputed inline-code, adds it to the text earlier.

    Parameters:
    -------
        all_text (str): String.

    Returns:
    -------
        res_text (str): String.
    """
    inp_text = input("Text: > ")

    if "`" in inp_text:
        text_with_code = "``" + inp_text + "``"
    else:
        text_with_code = "`" + inp_text + "`"

    if not len(all_text) == 0:
        res_text = all_text + "\n" + text_with_code
    else:
        res_text = text_with_code

    return res_text


def ordered_list_func(all_text: str) -> str:
    """
    Saves user inputed ordered-list, adds it to the text earlier.

    Parameters:
    -------
        all_text (str): String.

    Returns:
    -------
        res_text (str): String.
    """
    num_rows = input("Number of rows: > ")
    while not num_rows.isnumeric():
        print("Inputed number of rows should be numeric. Try again.")
        num_rows = input("Number of rows: > ")
    num_rows = int(num_rows)
    while not 1 <= num_rows:
        print("The number of rows should be greater than zero. Try again.")
        num_rows = input("Number of rows: > ")

    list_text = ""
    for i in range(1, (num_rows + 1), 1):
        row = input("Row #" + str(i) + ": > ")
        row_text = str(i) + ". " + row
        if i == 1:
            list_text = list_text + row_text
        else:
            list_text = list_text + "\n" + row_text
    if not len(all_text) == 0:
        res_text = all_text + "\n" + list_text
    else:
        res_text = list_text

    return res_text


def unordered_list_func(all_text: str) -> str:
    """
    Saves user inputed unordered-list, adds it to the text earlier.

    Parameters:
    -------
        all_text (str): String.

    Returns:
    -------
        res_text (str): String.
    """
    num_rows = input("Number of rows: > ")
    while not num_rows.isnumeric():
        print("Inputed number of rows should be numeric. Try again.")
        num_rows = input("Number of rows: > ")
    num_rows = int(num_rows)
    while not 1 <= num_rows:
        print("The number of rows should be greater than zero. Try again.")
        num_rows = input("Number of rows: > ")

    list_text = ""
    for i in range(1, (num_rows + 1), 1):
        row = input("Row #" + str(i) + ": > ")
        row_text = "* " + row
        if i == 1:
            list_text = list_text + row_text
        else:
            list_text = list_text + "\n" + row_text
    if not len(all_text) == 0:
        res_text = all_text + "\n" + list_text
    else:
        res_text = list_text

    return res_text


def new_line_func(all_text: str) -> str:
    """
    Saves two spaces, adds it to the text earlier.

    Parameters:
    -------
        all_text (str): String.

    Returns:
    -------
        res_text (str): String.
    """
    if not len(all_text) == 0:
        res_text = all_text + "  "
    else:
        res_text = "  \n"

    return res_text


def save_file_func(all_text: str) -> None:
    """
    Saves the result to a file. When using the !done command, the program, in addition to exiting the program,
    saves the final result to the output.md file. If the file exists, overwrite the file. The file includes the
    result of the user's last session.

    Parameters:
    -------
        all_text (str): String.

    Returns:
    -------
        None
    """
    with open('output.md', 'w+t', encoding='utf-8') as my_file:
        my_file.write(all_text)


# The body of the main script is shown below!!!!!
# The bank of formated text
text = ""

# Initial formater input
user_input = input_func("\n")

while not user_input == "!done":

    # Help function
    if user_input == "!help":
        help_func()
        func_flag = 0

    elif user_input == "plain":
        text = plain_text_func(text)
        func_flag = 1

    elif user_input == "bold":
        text = bold_func(text)
        func_flag = 0

    elif user_input == "italic":
        text = italic_func(text)
        func_flag = 0

    elif user_input == "header":
        text = header_func(text)
        func_flag = 0

    elif user_input == "link":
        text = link_func(text)
        func_flag = 0

    elif user_input == "inline-code":
        text = inline_code_func(text)
        func_flag = 0

    elif user_input == "ordered-list":
        text = ordered_list_func(text)
        func_flag = 0

    elif user_input == "unordered-list":
        text = unordered_list_func(text)
        func_flag = 0

    else:
        text = new_line_func(text)
        func_flag = 0

    print(text)  # Displays the result

    # The loop of formater input
    if func_flag == 1:
        user_input = input_func()
    else:
        user_input = input_func("\n")

else:
    save_file_func(text)
    exit()
