friend_ages = {"santi":4, "jose":3, "carlos":8 }

#iterating over dictionary keys
for name in friend_ages:
    print(name)

#iterating over dictionary keys
for ages in friend_ages.values():
    print(ages)

#iterating completely
for name,age in friend_ages.items():
    print(name,age)



#destructuring: 
amigos = [("Rolf",25), ("Caro",24), ("Ana",30)]
for name,age in amigos:
    print(f'el amigo {name}, tiene {age} de edad')