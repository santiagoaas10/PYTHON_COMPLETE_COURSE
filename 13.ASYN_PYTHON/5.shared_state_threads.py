# SHARED STATE EN THREADS
# Todos los threads comparten la misma memoria (el mismo counter).
# El problema: un thread puede incrementar el counter, luego hacer un sleep,
# y mientras duerme OTRO thread también incrementa el counter.
# Cuando el primer thread imprime, el valor ya no es el que él puso — fue modificado por otro.
# Esto se llama RACE CONDITION: los threads "compiten" por modificar la misma variable.
# Por eso los valores se repiten o aparecen fuera de orden en el output.

from threading import Thread
import time
import random


counter=0

def increment_counter():
    global counter
    counter+=1
    time.sleep(random.random())  # simula trabajo — otro thread puede modificar counter aquí
    print(f'New Counter value: {counter}')  # el valor puede haber cambiado ya
    time.sleep(random.random())
    print('--------------------------------')

for x in range(10):
    t = Thread(target=increment_counter)
    time.sleep(random.random())
    t.start()

