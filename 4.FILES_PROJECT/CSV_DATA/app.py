import os  

script_dir = os.path.dirname((os.path.abspath(__file__)))
data_path = os.path.join(script_dir, 'csv_data.txt')

studies = open(data_path,'r')
lines = studies.readlines()

lines = [line.strip() for line in lines[1:]] # strip() elimina los espacios en blanco y saltos de línea al inicio y final de cada línea.

for line in lines:
    person_data = line.split(',')
    nombre = person_data[0]
    edad = person_data[1]
    universidad = person_data[2]
    carrera = person_data[3]

    print(f'la persona {nombre}, tiene {edad}, estudia {carrera} en {universidad}\n')

