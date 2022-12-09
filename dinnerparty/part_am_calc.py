def part_am_calc(friends, unlucky_fr, tot_am):
    # To calculate part of amount and update friends dict
    if len(friends) > len(unlucky_fr) > 0:
        part_am = round(tot_am / (len(friends) - (len(friends) - len(unlucky_fr))), 2)
        friends.update({k: part_am for k in unlucky_fr})
    else:
        part_am = round(tot_am / len(friends), 2)
        friends.update({k: part_am for k in friends})

    return friends
