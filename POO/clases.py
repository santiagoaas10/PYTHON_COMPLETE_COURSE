class Student:
    def __init__(self,new_name,new_grades): #self is a blank object that was created before we call the dunder init function
        self.name = new_name
        self.grades = new_grades
    

    def average(self):
        return sum(self.grades) / len(self.grades)

student_one = Student("santi", [4, 5, 4.5, 3]) 


print(student_one.__class__)
#when we create a class it creates a self object (empty) that is passed to the dunder method inmediatly

#student one se pasa como self
print(student_one.average()) #average recibe el argumento self (que es el objeto en si mismo), vease linea 7, peeero python es muy inteligente y sabe que con esta sintaxis " student_one.average() " el objeto con el que lo llamamos es student_one()
#es equivalente a hacer esto, python nos salva de tipear todo esto
print(Student.average(student_one))
