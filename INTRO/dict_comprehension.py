friends = ["Santi", "Carlos", "David", "Daniel"]
time_no_see = [3,10,2,7]

longest_time_no_see = {
    friends[i]:time_no_see[i]
    for i in range(len(friends))
    if time_no_see[i] > 4
}

print(longest_time_no_see)


#o tambien
comprehension_easier = dict(zip(friends,time_no_see))
print(comprehension_easier)