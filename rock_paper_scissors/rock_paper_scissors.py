"""Rock_paper_scissors project: game"""

# Libraries
import random
import math

# 5-th stage
print("\nROCK_PAPER_SCISSORS\n")  # Program name


def ini_parameter_func() -> tuple[list[str], int, str]:
    """
    Implements initial data set.

    Returns:
    -------
        Tuple:
            opt (list[str]): List of Strings;
            sc (int): A decimal integer;
            us_n (str): String.
    """
    # Options alphabet (set)
    all_options = ["rock", "fire", "scissors", "snake", "human", "tree", "wolf",
                   "sponge", "paper", "air", "water", "dragon", "devil", "lightning",
                   "gun"]
    opt = ["rock", "scissors", "paper"]
    # Initial score
    sc = 0

    us_n = input("Enter your name: > ")  # Users intodusing
    print(f"Hello, {us_n}.")
    current_options = input("Please input game options in the format "
                            "\"symbol1,symbol2,symbol3,...\".\n> ").lower().split(",")
    current_options = list(set(current_options))  # To prevent duplicates
    # To prevent short input or unexpected game options
    if len(current_options) <= 2:
        print("Your input was too short!\nOptions will be: \"rock\", \"scissors\", \"paper\".")
    elif not any([current_options[i] in all_options for i in range(len(current_options))]):
        elements = str([current_options[i] in all_options for i in range(len(current_options))])
        print(f"Wrong some element ({elements})!\nOptions will be: \"rock\", \"scissors\", \"paper\".")
    else:
        opt_temp = []
        for j in range(len(all_options)):
            for i in range(len(current_options)):
                if all_options[j] == current_options[i]:
                    opt_temp.append(all_options[j])
        opt = opt_temp

    print("Okay, let's start!")

    return opt, sc, us_n


def program_answer_func(us_ch: str, sc: int) -> int:
    """
    Implements program choice in the game.

    Parameters:
    -------
        us_ch (str): String;
        sc (int): A decimal integer.

    Returns:
    -------
        sc (int): A decimal integer.
    """
    prog_ch = str(random.choice(options))  # Randomly choosen option by program

    # Determination of the options list when user wins program
    win_ind = range((options.index(prog_ch) - math.floor(len(options) / 2)), (options.index(prog_ch)))
    win_options = [options[i] for i in win_ind]

    # To choose the winner
    if prog_ch != us_ch and us_ch in win_options:  # Player wins
        print(f"Well done. The computer chose {prog_ch} and failed")
        sc += 100

    elif prog_ch != us_ch and us_ch not in win_options:  # Program wins
        print(f"Sorry, but the computer chose {prog_ch}")

    else:  # Draw
        print(f"There is a draw ({prog_ch})")
        sc += 50

    return sc


def raiting_file_func(sc: int, us_n: str) -> int:
    """
    Reads the results file, checks the names and set initial score.

    Parameters:
    -------
        sc (int): A decimal integer;
        us_n (str): String.

    Returns:
    -------
        sc_res (int): A decimal integer
    """
    # Reads the file with sessions results and forms the list using lines
    all_players_res_list = []
    try:
        open('rating.txt')
    except FileNotFoundError as e:
        print(f"File {e} was not found.")
    else:
        with open('rating.txt', 'r+t', encoding='utf-8') as my_file:
            all_players_res_list = my_file.readlines()

    # Saves score from file if it finds the name in the line (looping each line in file)
    sc_file = 0
    for s in all_players_res_list:
        if us_n in s:
            try:
                sc_file = int(s.split(" ")[-1])
            except TypeError:
                print("Score in your file rating.txt should be a number!")

    # Checks situation showing results after game session
    # The situation before game session
    if sc <= sc_file:
        sc_res = sc_file
    # The situation after game session
    else:
        sc_res = sc

    print(f"Your rating: {sc_res}")

    return sc_res


# The body of the main script is shown below!!!!!
if __name__ == '__main__':
    # Initial parameter set
    options, score, user_name = ini_parameter_func()

    while True:
        user_choice = input("> ")

        if user_choice in options:
            score = program_answer_func(user_choice, score)

        elif user_choice == "!rating":
            score = raiting_file_func(score, user_name)

        elif user_choice == "!exit":
            print("Bye!")
            exit()

        else:
            print("Invalid input. Please re-enter.")
