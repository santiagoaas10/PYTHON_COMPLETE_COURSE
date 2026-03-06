div = lambda x,y : x/y
print(div(15,1))


####################### EJM ###########################
students = [
    {"name":"santi", "grades":(60,40,23)},
    {"name":"jose", "grades":(60,40,89)}
]

average = lambda sequence : sum(sequence)/len(sequence)

for student in students:
    print(average(student["grades"]))
