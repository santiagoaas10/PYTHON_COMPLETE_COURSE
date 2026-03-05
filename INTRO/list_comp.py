friend_ages = [3,6,7,8]

names = {
    "santi":3, 
    "jose":4, 
    "david":5,
    "camilo":8
    }

string_ages = [f"my friend {name} tiene {age}" for name,age in names.items() ]
print(string_ages)


nuevas_edades = [22,45,36,75,28]
edades_pares = [edades_pares for edades_pares in nuevas_edades if edades_pares%2==0]
print(edades_pares)