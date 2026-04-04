import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor #creamos un bunch de threads para ejecutar nuestras funciones
import threading

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
print(f'Single Thread total time {time.time() - start}')

thread1 = Thread(target = complex_calculation)
thread2 = Thread(target= ask_user)


start = time.time()
thread1.start()
thread2.start()

#DONT KILL THREADS BEACAUSE IT COULD CAUSE A DEADLOCK WHERE GIL IS NOT REASSIGNED

thread1.join() #para bloquear el main thread hasta que thread1 termine
thread2.join() #para bloquear el main thread hasta que el thread2 termine
print(f'Two thread total time: {time.time() - start}')
#print(threading.active_count())