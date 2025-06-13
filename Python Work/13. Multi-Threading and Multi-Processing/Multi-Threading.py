### Multithreading
## When to use Multi Threading
###I/O-bound tasks: Tasks that spend more time waiting for I/O operations (e.g., file operations, network requests).
###Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently.

import threading
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(2)

def print_alphabets():
    for char in "abcde":
        print(f"Alphabet: {char}")
        time.sleep(2)

# Declaring Threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_alphabets)

starttime=time.time()
# Starting Threads
t1.start()
t2.start()
# Waiting for Threads to complete
t1.join()
t2.join()

executiontime=time.time()-starttime
print(f"Execution time: {executiontime}")