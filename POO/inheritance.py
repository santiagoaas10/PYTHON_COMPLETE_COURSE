#Herencia y property decorator: 
class Student:
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/ len(self.marks)

class WorkingStudent(Student):
    def __init__(self,name,school,salary):
        super().__init__(name,school)
        self.salary = salary
    
    @property
    def weekly_salary(self):
        return self.salary * 37.5




rolf = WorkingStudent('Rolf', 'MIT', 100)
print(rolf.salary)

rolf.marks.append(100)
rolf.marks.append(87)
rolf.marks.append(90)
print(rolf.average())
print(rolf.weekly_salary)

'''
el property decorator
Permite que un método se use como si fuera un atributo.
Es decir:
En vez de hacer esto:
persona.get_nombre()
Puedes hacer esto:
persona.nombre
Pero por debajo sigue siendo una función.
🔥 ¿Por qué es poderoso?
Porque te permite:
✅ Agregar lógica cuando alguien accede a un atributo
✅ Validar datos
✅ Calcular valores dinámicos
✅ Encapsular correctamente (POO real)
✅ Cambiar implementación sin romper código externo

'''