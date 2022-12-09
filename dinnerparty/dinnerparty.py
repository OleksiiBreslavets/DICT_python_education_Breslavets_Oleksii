"""Dinnerparty project: simple game"""

# Functions
from part_am_calc import part_am_calc
from choice import choice
from name_input import name_input

# 3-rd and 4-th stages
print("\nDINNERPARTY")  # Program name

# Make a dictionary
friends = {}
unlucky_fr = {}

# The input of the number
fr_num = input("Enter the number of friends joining (including you):\n> ")

# Check for not numbers and not normal numbers
if not fr_num.isnumeric() or (fr_num.isnumeric() and int(fr_num) <= 0):
    print("No one is joining for the party")
else:
    # String to number
    fr_num = int(fr_num)

    # inputing names of friends
    friends = name_input(fr_num, friends)

    tot_am = input("\nEnter the total amount:\n> ")

    # Check for not numbers and not normal numbers
    while not tot_am.isnumeric() or (tot_am.isnumeric() and int(tot_am) <= 0):
        print("Inputed amount is not correct. Please try again.")
        tot_am = input("\nEnter the total amount:\n> ")
    else:
        # String to number
        tot_am = int(tot_am)

        # To choose friend who will not pay
        lucky_choice = input("\nDo you want to use the \"Who is lucky?\" feature? Write Yes/No:\n> ")
        if lucky_choice == "Yes" or lucky_choice == "yes":
            # Name of friend who will not pay and New dictionary of unlucky friends
            lucky_fr, unlucky_fr = choice(friends)
            print("\n" + lucky_fr + " is the lucky one!")
        else:
            print("\nNo one is going to be lucky.")

        # To calculate part of amount and update friends dict and output
        friends = part_am_calc(friends, unlucky_fr, tot_am)
        print("\n" + str(friends))  # Output dictionaries
