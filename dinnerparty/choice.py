def choice(friends):
    # Libraries
    import random

    # Name of friend who will not pay and New dictionary of unlucky friends
    lucky_fr = str(random.choice(tuple(friends.keys())))
    unlucky_fr = friends.copy()
    unlucky_fr.pop(lucky_fr)
    return lucky_fr, unlucky_fr
