import time

from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor

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

    start = time.time()
    with ProcessPoolExecutor(max_workers=2) as pool:
        pool.submit(complex_calculation)
        pool.submit(complex_calculation)
    print(f'Two Processes total time {time.time() - start}')
