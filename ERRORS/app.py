class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def __repr__(self):
        return f'<Car {self.make} {self.model}>'



class Garage:
    def __init__(self):
        self.cars = []
    
    def __len__(self):
        return len(self.cars)
    
    def add_car(self, car):
        #print('Working to get ready the method')
        if not isinstance(car, Car):
            raise TypeError(f'Tried to add a {car.__class__.__name__} to the garage, but you can only add Car objects')
        #raise NotImplementedError("We can't add cars to the garage yeet.")
        self.cars.append(car)


ford = Garage()
#ford.add_car('Fiesta') esto levanta el error
fiesta = Car('Fiesta', 1995)
ford.add_car(fiesta)
print(len(ford))

raptor = Car('raptor', 2016)

try:
    ford.add_car(raptor)
except TypeError: #si otro tipo de error diferente del de Type error pasa, esto no será llamado y no se agarrará el error y como no se agarra se dispara y para el programa
    print('Your Car was not a Car')

print(len(ford))


try:
    ford.add_car('F150')
except TypeError: #ACA LO VA A ATRAPAR, PERO SI TUVIERAMOS POR EJEMPLO UN ERROR DE TIPO VALUE ERROR QUE SE RAISEA, NO ES CAPAZ DE ATRAPARLO Y POR ENDE NO EJECUTA EL PRINT DE ABAJO, SINO QUE DISPARA EL ERROR RAISEADO Y PARA EL PROGRAMA, INTENTAR CAMBIAR EN LA LINEA 2 POR UN ERROR TIPO EXCEPTION O VALUEERROR U OTRO  Y VERAS 
    print('Your car was not a CAR!!!!')
except SyntaxError:
    print('probando si se agarra un error de sintaxis')
finally: #y este finally se ejecuta SIEMPRE, 'excepts may or not run but finally will always run ', puede haber tambn un else que si ejecuta solo si los anteriores 2 no se ejecutaron
    print(f'The garage now has {len(ford)} cars.')