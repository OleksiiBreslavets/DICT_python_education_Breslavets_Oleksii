def error_check(word_guess, word_puzzled, other_symbols, errors_num, word_user):
    check = False
    # Check of low English letter
    if not word_user.isascii() or not word_user.isalpha() or not word_user.islower():
        print("Please enter a lowercase English letter.")

    # Check of 1 symbol input
    elif len(word_user) != 1:
        print("You should input a single letter.")

    # Check of repeating not appeared the input letter
    elif word_user not in word_guess and word_user not in other_symbols:
        print("That letter doesn't appear in the word")
        errors_num = errors_num + 1
        other_symbols = other_symbols + word_user
    elif word_user not in word_guess and word_user in other_symbols:
        print("You've already guessed this letter.")
        other_symbols = other_symbols + word_user

    # Check of appearing and repeating appeared the input letter
    elif word_user in word_guess and word_user in word_puzzled:
        print("You've already guessed this letter.")
    else:
        check = True

    return check, other_symbols, errors_num
