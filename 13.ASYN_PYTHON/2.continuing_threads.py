import time
from concurrent.futures import ThreadPoolExecutor #creamos un bunch de threads para ejecutar nuestras funciones

def ask_user():
    start = time.time()
    user_input = input('Enter your input') #blocking operation
    greet = f'Hello, {user_input}'
    print(greet)
    print(f'ask_user, {time.time() - start}')

def complex_calculation():
    start = time.time()
    print('started calculation')
    [x**2 for x in range(20000000)]
    print(f'complex_calculation {time.time() - start}')

start = time.time()
ask_user()
complex_calculation()
print(f'Single Thread totl time {time.time() - start}')


with ThreadPoolExecutor(max_workers=2) as pool: #creamos una pool de threads a las cuales les podemos mandar tareas
    pool.submit(complex_calculation) #y como lo hacemos con with no tnemos que esperar que termine
    pool.submit(ask_user)









"""
with es un context manager. Básicamente garantiza que algo se limpie correctamente al terminar, aunque haya un error.

# Con with:
with open('archivo.txt') as f:
    data = f.read()
# El archivo se cierra automáticamente aquí, pase lo que pase

# Sin with (equivalente manual):
f = open('archivo.txt')
try:
    data = f.read()
finally:
    f.close()  # Tienes que hacerlo tú
Con ThreadPoolExecutor hace lo mismo:

# Con with:
with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(ask_user)
# Aquí automáticamente hace .shutdown() que espera todos los threads (como join)

# Sin with (equivalente manual):
pool = ThreadPoolExecutor(max_workers=2)
try:
    pool.submit(complex_calculation)
    pool.submit(ask_user)
finally:
    pool.shutdown(wait=True)  # Tienes que hacerlo tú
¿Es obligatorio? No, pero es muy recomendable porque:

Evita memory leaks
Evita archivos que quedan abiertos
Evita threads que quedan colgados
El código queda más limpio
"""