import time
import random
import queue

from threading import Thread

counter=0
job_queue = queue.Queue() #things to be printed out
counter_queue = queue.Queue() #amounts by which to increase queue, when we increment the counter we add the amount to this queue

def increment_manager():
    global counter
    while True:
        increment = counter_queue.get() #wait until sn item is available and the
        old_counter = counter
        counter = old_counter + increment
        job_queue.put((f'New counter value is {counter}'), '--------')
        counter_queue.task_done()

Thread(target=increment_manager, daemon=True).start()

def printer_manager():
    while True:
        for line in job_queue.get():
            print(line)
        job_queue.task_done()

Thread(target=printer_manager, daemon=True).start()

def increment_counter():
    counter_queue.put(1)


workers = [Thread(target=increment_counter) for thread in range(10)]

for thread in workers:
    thread.join()

counter_queue.join()
job_queue.join()




