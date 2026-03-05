class Student:
    def __init__(self,name):
        self.name = name

movies = ['Matrix', 'finding Nemo']
print(movies.__class__) #de la clase lista
#TODO EN PYTHON ES UN OBJETO

#los dunder methods son metodos especiales que las clases que nosotros creamos se manejen como objetos nativos de python,
#es decir, que podamos comparrarlos con ==, que podemos ver algun mensaje cuando los imprimimos o debugueamos
#que podamos iterarlos como si fueran listas y asi ...
#abajo vemos algunos de ellos

class Garage:
    #a
    def __init__(self):
        self.cars = []
    
    #b
    def __len__(self):
        return len(self.cars)
    
    #c
    def __getitem__(self,i):
        return self.cars[i]
    
    #d
    def __repr__(self):
        return f'<Garage {self.cars}>'

    #e
    def __str__(self):
        return f'Garage with {len(self)} cars'




ford = Garage()
ford.cars.append('Fiseta')
ford.cars.append('Focus')

print(ford.cars)

#b
print(len(ford))

#c
print(ford[0]) #Garage.__getitem__(ford,0)


#cuando tenemos los metodos len y getitem definidos debloqueamos el poder de iterar sobre los valores de una clase:
for car in ford:
    print(car)

#e
print(ford)