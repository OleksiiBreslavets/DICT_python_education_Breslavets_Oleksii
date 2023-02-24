"""Dominoes project: game"""

# Libraries
import random

# 5-th stage
print("\nDOMINOES\n")  # Program name


class Dominoes:
    """
        Class Dominoes: The class represents the Dominoes game; its method takes a string as input; whenever the
        user types a string into the console, the program calls this method with one argument: the string the user types
        into the console; the class will only process input that comes to it through this method and its string
        argument.

        ...

        Attributes
        ----------
        knuckles : list[list[int]]
            detected set of player domino knuckles.

        Methods
        -------
        prevent_duplicates(some_knucks: list[list[int]]):
            Removes all duplicates from the input domino knuckles set.
        take_seven_knuckles(dom_set: list[list[int]]):
            Takes 7 random knuckles from the first basic set and adds this knuckles to the players or computers set.
        output_res(dom_set: list[list[int]], comp_set: list[list[int]], pl_set: list[list[int]],
            dom_snake: list[int], st="error"):
            Displays the results.
        check_items(dom_set: list[list[int]], comp_set: list[list[int]], pl_set: list[list[int]], done=False):
            Checks [n, n] knuckles in the players and computers sets.
        put_knuckle_onto_snacke(dom_set: list[list[int]], ini_set1: list[list[int]], ini_set2: list[list[int]],
            num: int, com: int, dom_snake: list[list[int]] | list[int], stat: str):
            Puts 1 knuckle onto domino snacke.
        move(dom_set: list[list[int]], ini_set1: list[list[int]], ini_set2: list[list[int]],
             num: int, com: int, dom_snake: list[list[int]] | list[int], side: list[int] | int, stat: str):
             Makes 1 step and checks how it to do.
        registration(self, side1: list[int] | int, side2: list[int] | int,
            cp_com_vect: list[int], comp_set: list[list[int]]):
            Makes the registration of the checked possible choices.
        game_step(dom_set: list[list[int]], comp_set: list[list[int]], pl_set: list[list[int]],
            dom_snake: list[list[int]] | list[int], stat: str):
            Makes 1 step of computer or player.
    """

    def __init__(self, knuckles):
        """
        Constructs all the necessary attributes for the resources status object.

        Parameters:
        -------
            knuckles : list[list[int]]
                detected set of player domino knuckles.
        """
        self.knuckles = knuckles

    def prevent_duplicates(self, some_knucks: list[list[int]]) -> list[list[int]]:
        """
        Removes all duplicates from the input domino knuckles set.

        Parameters:
        -------
            some_knucks (list[list[int]]): List of a decimal integers'.

        Returns:
        -------
            self.knuckles (list[list[int]]): List of a decimal integers'.
        """
        knuckles_without_duplicates = []
        [knuckles_without_duplicates.append(x) for x in some_knucks if x not in knuckles_without_duplicates]
        self.knuckles = knuckles_without_duplicates

        return self.knuckles

    def take_seven_knuckles(self, dom_set: list[list[int]]) -> tuple[list[list[int]], list[list[int]]]:
        """
        Takes 7 random knuckles from the first basic set and adds this knuckles to the players or computers set.

        Parameters:
        -------
            dom_set (list[list[int]]): List of a decimal integers'.

        Returns:
        -------
            Tuple:
                self.knuckles (list[int]): List of a decimal integers';
                second_set  (list[int]): List of a decimal integers'.
        """
        second_set = random.sample(dom_set, 7)
        self.knuckles = [x for x in dom_set if x not in second_set]

        return self.knuckles, second_set

    def output_main(self, dom_set: list[list[int]], comp_set: list[list[int]], pl_set: list[list[int]],
                    dom_snake: list[int] | list[list[int]], st="error") -> list[list[int]]:
        """
        Displays the results.

        If the argument 'st' is passed, then it is appended after the main info.

        Parameters:
        -------
            dom_set (list[list[int]]): List of a decimal integers';
            comp_set (list[list[int]]): List of a decimal integers';
            pl_set (list[list[int]]): List of a decimal integers';
            dom_snake (list[int] | list[list[int]]): List of a decimal integers';
            st (str): String (default is "error").

        Returns:
        -------
            self.knuckles (list[list[int]]): List of a decimal integers'.
        """
        str_border = "=" * 70
        if st == "player":
            str_to_move = "It's your turn to make a move. Enter your command."
        else:
            str_to_move = "Computer is about to make a move. Press Enter to continue..."

        pl_str = "\n".join([f"[{str(i + 1)}]:{pl_set[i]}" for i in range(len(pl_set))])

        if len(dom_snake) > 6:
            d_snake = "".join(map(str, dom_snake[:3])) + "..." + "".join(map(str, dom_snake[-3:]))
        else:
            d_snake = dom_snake

        print(f"""{str_border}
Stock size: {len(dom_set)}
Computer pieces: {len(comp_set)}

{d_snake}

Player pieces:
{pl_str}
""")
        if not len(pl_set) == 0 and not len(comp_set) == 0:
            print(f"Status: {str_to_move}")

        return self.knuckles

    def check_items(self, dom_set: list[list[int]], comp_set: list[list[int]], pl_set: list[list[int]], done=False) -> \
            tuple[list[list[int]], list[list[int]], list[list[int]], list[int], str, bool]:
        """
        Checks [n, n] knuckles in the players and computers initial sets.

        If the argument 'done' is passed, then it is appended after the main info.

        Parameters:
        -------
            dom_set (list[list[int]]): List of a decimal integers';
            comp_set (list[list[int]]): List of a decimal integers';
            pl_set (list[list[int]]): List of a decimal integers';
            done (bool): Boolean (default is False).

        Returns:
        -------
            Tuple:
                dom_set (list[list[int]]): List of a decimal integers';
                comp_set (list[list[int]]): List of a decimal integers';
                pl_set (list[list[int]]): List of a decimal integers';
                dom_snake (list[int]): List of a decimal integers';
                stat (str): String;
                done (bool): Boolean.
        """
        stat = ""
        dom_snake = [int()]
        for j in range(6, -1, -1):
            for i in range(len(player_dominoes)):
                if [j, j] == player_dominoes[i]:
                    dom_snake = pl_set[i]
                    player_dominoes.pop(i)
                    stat = "computer"
                    self.knuckles = dominoes.output_main(dom_set, comp_set, pl_set, dom_snake, stat)
                    done = True
                    break

                elif [j, j] == comp_set[i]:
                    dom_snake = comp_set[i]
                    comp_set.pop(i)
                    stat = "player"
                    self.knuckles = dominoes.output_main(dom_set, comp_set, pl_set, dom_snake, stat)
                    done = True
                    break

                else:
                    done = False

            if done:
                break

        return dom_set, comp_set, pl_set, dom_snake, stat, done

    def put_knuckle_onto_snacke(self, dom_set: list[list[int]], ini_set1: list[list[int]], ini_set2: list[list[int]],
                                num: int, com: int, dom_snake: list[list[int]] | list[int], stat: str) -> \
            tuple[list[list[int]], list[list[int]], list[list[int]], list[list[int]]]:
        """
        Puts 1 knuckle onto domino snacke.

        Parameters:
        -------
            dom_set (list[list[int]]): List of a decimal integers';
            ini_set1 (list[list[int]]): List of a decimal integers';
            ini_set2 (list[list[int]]): List of a decimal integers';
            num (int): A decimal integer (left value order; rotate knuckle or not);
            com (int): A decimal integer;
            dom_snake (list[list[int]] | list[int]): List of a decimal integers';
            stat (str): String.

        Returns:
        -------
            Tuple:
                dom_set (list[list[int]]): List of a decimal integers';
                ini_set1 (list[list[int]]): List of a decimal integers';
                ini_set2 (list[list[int]]): List of a decimal integers';
                dom_snake (list[list[int]]): List of a decimal integers'.
        """
        if com < 0 and (len(dom_snake) <= 2 and type(dom_snake[0]) == int):
            dom_snake = [[ini_set1[(abs(com) - 1)][num], ini_set1[(abs(com) - 1)][(num * (-1) + 1)]], dom_snake]
        elif com < 0 and not (len(dom_snake) <= 2 and type(dom_snake[0]) == int):
            dom_snake = [[ini_set1[(abs(com) - 1)][num], ini_set1[(abs(com) - 1)][(num * (-1) + 1)]], *dom_snake]
        elif com > 0 and (len(dom_snake) <= 2 and type(dom_snake[0]) == int):
            dom_snake = [dom_snake, [ini_set1[(abs(com) - 1)][num], ini_set1[(abs(com) - 1)][(num * (-1) + 1)]]]
        elif com > 0 and not (len(dom_snake) <= 2 and type(dom_snake[0]) == int):
            dom_snake = [*dom_snake, [ini_set1[(abs(com) - 1)][num], ini_set1[(abs(com) - 1)][(num * (-1) + 1)]]]
        else:
            if len(dom_set) > 0:
                ini_set1.append(random.choice(dom_set))
                dom_set.remove(ini_set1[-1])

        if not com == 0:
            ini_set1.pop((abs(com) - 1))

        if stat == "player":
            self.knuckles = dominoes.output_main(dom_set, ini_set2, ini_set1, dom_snake, "computer")
            return dom_set, ini_set2, ini_set1, dom_snake
        else:
            self.knuckles = dominoes.output_main(dom_set, ini_set1, ini_set2, dom_snake, "player")
            return dom_set, ini_set1, ini_set2, dom_snake

    def move(self, dom_set: list[list[int]], ini_set1: list[list[int]], ini_set2: list[list[int]],
             num: int, com: int, dom_snake: list[list[int]] | list[int], side: list[int] | int, stat: str) -> \
            tuple[list[list[int]], list[list[int]], list[list[int]], list[list[int]], str]:
        """
        Makes 1 step and checks how it to do.

        Parameters:
        -------
            dom_set (list[list[int]]): List of a decimal integers';
            ini_set1 (list[list[int]]): List of a decimal integers';
            ini_set2 (list[list[int]]): List of a decimal integers';
            num (int): A decimal integer;
            com (int): A decimal integer;
            dom_snake (list[list[int]] | list[int]): List of a decimal integers';
            stat (str): String.

        Returns:
        -------
            Tuple:
                dom_set (list[list[int]]): List of a decimal integers';
                comp_set (list[list[int]]): List of a decimal integers';
                pl_set (list[list[int]]): List of a decimal integers';
                dom_snake (list[list[int]]): List of a decimal integers';
                stat (str): String.
        """
        self.knuckles = dom_set
        if side == ini_set1[(abs(com) - 1)][num]:
            if com < 0:
                dom_set, comp_set, pl_set, dom_snake = \
                    dominoes.put_knuckle_onto_snacke(dom_set, ini_set1, ini_set2,
                                                     (num * (-1) + 1), com, dom_snake, stat)
            elif com > 0:
                dom_set, comp_set, pl_set, dom_snake = \
                    dominoes.put_knuckle_onto_snacke(dom_set, ini_set1, ini_set2,
                                                     num, com, dom_snake, stat)
            else:
                dom_set, comp_set, pl_set, dom_snake = \
                    dominoes.put_knuckle_onto_snacke(dom_set, ini_set1, ini_set2,
                                                     num, com, dom_snake, stat)
        elif side == ini_set1[(abs(com) - 1)][(num * (-1) + 1)]:
            if com < 0:
                dom_set, comp_set, pl_set, dom_snake = \
                    dominoes.put_knuckle_onto_snacke(dom_set, ini_set1, ini_set2, num, com, dom_snake, stat)
            elif com > 0:
                dom_set, comp_set, pl_set, dom_snake = \
                    dominoes.put_knuckle_onto_snacke(dom_set, ini_set1, ini_set2,
                                                     (num * (-1) + 1), com, dom_snake, stat)
            else:
                dom_set, comp_set, pl_set, dom_snake = \
                    dominoes.put_knuckle_onto_snacke(dom_set, ini_set1, ini_set2,
                                                     (num * (-1) + 1), com, dom_snake, stat)
        else:
            if stat == "player":
                print("Illegal move. Please try again.")
                # Player makes his game step again
                dom_set, comp_set, pl_set, dom_snake, stat = \
                    dominoes.game_step(dom_set, ini_set2, ini_set1, dom_snake, "player")
            else:
                print("Illegal move. Please try again.")
                # Player makes his game step again
                dom_set, comp_set, pl_set, dom_snake, stat = \
                    dominoes.game_step(dom_set, ini_set1, ini_set2, dom_snake, "computer")

        return dom_set, comp_set, pl_set, dom_snake, stat

    def registration(self, side1: list[int] | int, side2: list[int] | int,
                     cp_com_vect: list[int], comp_set: list[list[int]]) -> tuple[int, list[int]]:
        """
        Makes the registration of the checked possible choices.

        Parameters:
        -------
            side1 (int): A decimal integer;
            side2 (int): A decimal integer;
            cp_com_vect (list[int]): List of a decimal integers';
            comp_set (list[list[int]]): List of a decimal integers'.

        Returns:
        -------
            Tuple:
                cp_com (int): A decimal integer;
                reg_choice (list[int]): List of a decimal integers'.
        """
        self.knuckles = self.knuckles
        cp_com = int(cp_com_vect[0]) + 1
        reg_choice = [cp_com]
        iteration_marks = 1

        while not side1 == comp_set[(abs(cp_com) - 1)][0] \
                and not side1 == comp_set[(abs(cp_com) - 1)][1] \
                and not side2 == comp_set[(abs(cp_com) - 1)][0] \
                and not side2 == comp_set[(abs(cp_com) - 1)][1] \
                and not iteration_marks == (len(cp_com_vect)):
            if cp_com not in reg_choice:
                reg_choice.append(cp_com)
                reg_choice.sort()
            cp_com = int(cp_com_vect[iteration_marks]) + 1
            iteration_marks += 1

        if side1 == comp_set[(abs(cp_com) - 1)][0] or side1 == comp_set[(abs(cp_com) - 1)][1]:
            cp_com = -abs(cp_com)
        elif side2 == comp_set[(abs(cp_com) - 1)][0] or side2 == comp_set[(abs(cp_com) - 1)][1]:
            cp_com = abs(cp_com)
        else:
            cp_com = 0

        return cp_com, reg_choice

    def game_step(self, dom_set: list[list[int]], comp_set: list[list[int]], pl_set: list[list[int]],
                  dom_snake: list[list[int]] | list[int], stat: str) -> \
            tuple[list[list[int]], list[list[int]], list[list[int]], list[list[int]], str]:
        """
        Makes 1 step of computer or player.

        Parameters:
        -------
            dom_set (list[list[int]]): List of a decimal integers';
            comp_set (list[list[int]]): List of a decimal integers';
            pl_set (list[list[int]]): List of a decimal integers';
            dom_snake (list[list[int]] | list[int]): List of a decimal integers';
            stat (str): String.

        Returns:
        -------
            Tuple:
                dom_set (list[list[int]]): List of a decimal integers';
                comp_set (list[list[int]]): List of a decimal integers';
                pl_set (list[list[int]]): List of a decimal integers';
                dom_snake (list[list[int]]): List of a decimal integers';
                stat (str): String.
        """
        self.knuckles = dom_set

        if stat == "player":
            while True:
                try:
                    us_com = int(input("> "))
                    while not abs(us_com) <= len(pl_set):
                        us_com = int(input("Invalid input.\nWrong input value range.\nPlease try again.\n> "))
                    break
                except ValueError:
                    print("Invalid input.\nEnter only numbers!\nPlease try again.")

            if us_com < 0:
                if len(dom_snake) <= 2 and type(dom_snake[0]) == int:

                    dom_set, comp_set, pl_set, dom_snake, stat = \
                        dominoes.move(dom_set, pl_set, comp_set, 0, us_com, dom_snake, dom_snake[0], stat)

                else:

                    dom_set, comp_set, pl_set, dom_snake, stat = \
                        dominoes.move(dom_set, pl_set, comp_set, 0, us_com, dom_snake, dom_snake[0][0], stat)

            elif us_com > 0:

                if len(dom_snake) <= 2 and type(dom_snake[0]) == int:

                    dom_set, comp_set, pl_set, dom_snake, stat = \
                        dominoes.move(dom_set, pl_set, comp_set, 0, us_com, dom_snake, dom_snake[-1], stat)

                else:

                    dom_set, comp_set, pl_set, dom_snake, stat = \
                        dominoes.move(dom_set, pl_set, comp_set, 0, us_com, dom_snake, dom_snake[-1][-1], stat)

            else:
                dom_set, comp_set, pl_set, dom_snake = \
                    dominoes.put_knuckle_onto_snacke(dom_set, pl_set, comp_set, 0, us_com, dom_snake, stat)

            stat = "computer"

        else:
            input("> ")

            # Marking system of the computer step
            comp_set_vector = [comp_set[i][j] for j in range(len(comp_set[0])) for i in range(len(comp_set))]
            if len(dom_snake) <= 2 and type(dom_snake[0]) == int:
                dom_snake_vector = [dom_snake[i] for i in range(len(dom_snake))]
            else:
                dom_snake_vector = [dom_snake[i][j] for j in range(len(dom_snake[0])) for i in range(len(dom_snake))]
            marking_field = [*comp_set_vector, *dom_snake_vector]
            value_marks = {i: marking_field.count(i) for i in range(7)}
            marks = {i: (value_marks[comp_set[i][0]] + value_marks[comp_set[i][1]]) for i in range(len(comp_set))}
            marks = {k: v for k, v in sorted(marks.items(), reverse=True, key=lambda item: item[1])}
            cp_com_vect = [*marks]

            # Registration of checked possible choices
            if len(dom_snake) <= 2 and type(dom_snake[0]) == int:
                cp_com, reg_choice = dominoes.registration(dom_snake[0], dom_snake[-1], cp_com_vect, comp_set)

            else:
                cp_com, reg_choice = dominoes.registration(dom_snake[0][0], dom_snake[-1][-1], cp_com_vect, comp_set)

            if cp_com < 0:
                if len(dom_snake) <= 2 and type(dom_snake[0]) == int:

                    dom_set, comp_set, pl_set, dom_snake, stat = \
                        dominoes.move(dom_set, comp_set, pl_set, 0, cp_com, dom_snake, dom_snake[0], stat)

                else:

                    dom_set, comp_set, pl_set, dom_snake, stat = \
                        dominoes.move(dom_set, comp_set, pl_set, 0, cp_com, dom_snake, dom_snake[0][0], stat)

            elif cp_com > 0:
                if len(dom_snake) <= 2 and type(dom_snake[0]) == int:

                    dom_set, comp_set, pl_set, dom_snake, stat = \
                        dominoes.move(dom_set, comp_set, pl_set, 0, cp_com, dom_snake, dom_snake[-1], stat)

                else:

                    dom_set, comp_set, pl_set, dom_snake, stat = \
                        dominoes.move(dom_set, comp_set, pl_set, 0, cp_com, dom_snake, dom_snake[-1][-1], stat)

            else:
                dom_set, comp_set, pl_set, dom_snake = \
                    dominoes.put_knuckle_onto_snacke(dom_set, comp_set, pl_set, 0, cp_com, dom_snake, stat)

            stat = "player"

        return dom_set, comp_set, pl_set, dom_snake, stat


# The body of the main script is shown below!!!!!
if __name__ == '__main__':
    done_first_step = False
    dominoes_set = [[int()]]
    dominoes = Dominoes(dominoes_set)
    computer_dominoes = [[int()]]
    player_dominoes = [[int()]]
    dominoes_snake = [[int()]]
    status = ""
    while not done_first_step:
        # Initializes start set of all domino knuckles in the game.
        dominoes_set = [sorted([a, b]) for a in range(7) for b in range(7)]

        dominoes_set = dominoes.prevent_duplicates(dominoes_set)  # To prevent duplicates in the inputed set of knuckles

        dominoes_set, player_dominoes = dominoes.take_seven_knuckles(dominoes_set)  # To define players knuckles

        dominoes_set, computer_dominoes = dominoes.take_seven_knuckles(dominoes_set)  # To define computers knuckles

        # Returns the result of the 1st step with [n, n] knuckle
        dominoes_set, computer_dominoes, player_dominoes, dominoes_snake, status, done_first_step = \
            dominoes.check_items(dominoes_set, computer_dominoes, player_dominoes, done_first_step)

    while (len(computer_dominoes) > 0 and len(player_dominoes) > 0) or \
            (len(dominoes_snake) > 8 and dominoes_snake[0][0] == dominoes_snake[-1][-1]
             and str(dominoes_snake).find(str(dominoes_snake[0][0])) == 8):
        # Some gamer makes his game step
        dominoes_set, computer_dominoes, player_dominoes, dominoes_snake, status = \
            dominoes.game_step(dominoes_set, computer_dominoes, player_dominoes, dominoes_snake, status)

    if len(player_dominoes) == 0:
        print("Status: The game is over. You won!")
    elif len(computer_dominoes) == 0:
        print("Status: The game is over. The computer won!")
    else:
        print("Status: The game is over. It's a draw!")
