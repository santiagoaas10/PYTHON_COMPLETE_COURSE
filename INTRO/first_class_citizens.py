###Functions are first class citizens, it means that we can add them to variables, and put themo into dictionaries, lists, etc

def greet():
    print("hello friends")

hello = greet

hello()

### example of first_class_citizens

students = [
    {"name":"santi", "grades":(60,40,23)},
    {"name":"jose", "grades":(60,40,89)},
    {"name":"carlos", "grades":(80,10,500)}
]

operations = {
    "average" : lambda seq: sum(seq)/len(seq),
    "sum" : sum,
    "top" : max 
}

for student in students:
    name = student["name"]
    grades = student ["grades"]

    opc = input("average, sum or max")

    funcion_a_realizar = operations[opc]

    print(f"el estudiante {name}, la operacion realizada fue {opc} y el resultado fue", funcion_a_realizar(grades))



