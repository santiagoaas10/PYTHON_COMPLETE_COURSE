friends = ["Santi", "Carlos", "David", "Daniel"]
guests = ["Santi", "Carlos", "David"]

friends_lower_set = {friend.lower() for friend in friends}
guests_lower_set = {guest.lower() for guest in guests}


present_friends=friends_lower_set.intersection(guests_lower_set)

presented_friends_end = {name.title() for name in present_friends}

print(presented_friends_end)



 