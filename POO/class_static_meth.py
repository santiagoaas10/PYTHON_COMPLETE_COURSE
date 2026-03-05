class Student:
    def __init__(self,name, school):
        self.name = name
        self.school = school
        self.marks = []
    
    def average(self):
        return sum(self.marks) / len(self.marks)

rolf = Student('rolf', 'MIT')

rolf.marks.append(90)
rolf.marks.append(100)


print(rolf.average()) # = es lo mismo que: Student.average(rolf)


#un class method toma como argumento a la CLASE, no a la instancia (que es self)
class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)

my_object = Foo()
my_object.hi()


#los metodos estaticos NO TOMAN PARAMETROS ni de instancia ni de clase
class Bar:
    @staticmethod
    def hi():
        print('Hi I dont take params')

class FixedFloat:
    def __init__ (self,amount):
        self.amount = amount
    
    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'
        
    #solucion al problema sin usar la instancia de forma inutil
    @staticmethod
    def from_sum_static(valuea, valueb):
        return FixedFloat(valuea + valueb)
    
    @classmethod
    def from_sum_classmethod(cls,valuea, valueb):
        return cls(valuea+valueb)

"""    def from_sum(self, value1, value2):
        return FixedFloat(value1 + value2)"""

#number = FixedFloat(16.3850) #mira que creamos esta instancia pa nada, porqie el new number solo se calcula con los dos valores que damos de argumento al metodo
#new_number = number.from_sum(19.577, 0.4567)
#print(new_number)

#para ello seria util definir un static method que no necesite la instancia en sí misma ni la clase, NO NECESITAMOS CREAR EL OBJETO PA LLAMAR EL METODO
static = FixedFloat.from_sum_static(19.577, 0.4567)
print(static)

class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = 'E'

    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:.2f}>'

#class method
money = Euro.from_sum_classmethod(18.786, 9.999)
print(money)
