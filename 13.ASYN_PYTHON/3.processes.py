import time

from multiprocessing import Process

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

if __name__ == '__main__':

    start = time.time()
    ask_user()
    complex_calculation()
    print(f'Single Thread total time {time.time() - start}')

    #processes
    process  = Process(target=complex_calculation)
    process2  = Process(target=ask_user) #sale con error porque no tiene acceso a la consola, algo dificil del multiprocessing es que no se pueden compartir recursos entre procesos, como la consola. Ojo si se podrian hacer 2 complex calculations facil 
    process.start()
    process2.start()
    start = time.time()
    process.join()
    process2.join()
    print(f'two Processes total time {time.time() - start}')
'''
mutiprocessing vs multithreading.
multiprocessing es cuando queremos correr dos cosas en paralerlo en CPU.
multhithreading es cuando queremos correr de forma concurrente cosas con operaciones bloqueantes
'''




'''
no entendi, como asi que el proceso principal
Cuando corres un script de Python, ese script es un proceso — el proceso principal.

Cuando haces process.start(), creas un proceso hijo que corre aparte.

Ahora tienes dos procesos corriendo al mismo tiempo:


Proceso principal (tu script)  →  sigue ejecutando líneas
Proceso hijo                   →  corriendo complex_calculation()
process.join() le dice al proceso principal "para, espérate aquí hasta que el hijo termine".

Sin join() el proceso principal podría terminar y cerrar el programa antes de que el hijo acabara su tarea.

que hace el proceso principal?
En tu código, el proceso principal es el que corre todo el script:


if __name__ == '__main__':
    ask_user()               # proceso principal hace esto
    complex_calculation()    # proceso principal hace esto
    
    process = Process(...)   # proceso principal CREA el hijo
    process.start()          # proceso principal LANZA el hijo
    process.join()           # proceso principal ESPERA al hijo
    print(...)               # proceso principal hace esto al final
El proceso principal es básicamente tu programa. El proceso hijo es un ayudante que el principal crea para delegar una tarea.
'''