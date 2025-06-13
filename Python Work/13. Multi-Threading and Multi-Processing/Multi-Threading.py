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

t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_alphabets)

starttime=time.time()
t1.start()
t2.start()

t1.join()
t2.join()

executiontime=time.time()-starttime
print(f"Execution time: {executiontime}")