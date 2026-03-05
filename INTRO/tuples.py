friends = ("1","2")
friends = friends + ("5",6)
print(friends)


sets={1,3,3,3,5}
print(sets)

friend_ages = {"rolf": 30, "santi":40}
friend_ages["jose"]=45
print(friend_ages)


nums=[[1,2,3],[4,5,6],[6,7,8]]
for i in range(len(nums)):
    for j in range(len(nums[i])):
        print(nums[i][j])
