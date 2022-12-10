def name_input(fr_num, friends):
    print("\nEnter the name of every friend (including you), each on a new line:")
    while len(friends) < fr_num:
        name = input("> ")

        while not name.isalpha() or not name.isascii() or not name.istitle() or len(name) <= 1:
            name = input("Your input is not a name. Please try again.\n> ")  # inputing correct names of friends
        else:
            if name not in friends:  # don't repeat the names
                friends[name] = 0

    return friends
