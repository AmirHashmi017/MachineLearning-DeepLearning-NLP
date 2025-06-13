## PRocesses that run in parallel
### CPU-Bound Tasks-Tasks that are heavy on CPU usage (e.g., mathematical computations, data processing).
## Parallel execution- Multiple cores of the CPU

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        print(f"Square of {i}: {i**2}")
        time.sleep(2)

def cube_numbers():
    for i in range(5):
        print(f"Cube of {i}: {i**3}")
        time.sleep(1.5)

if __name__=="__main__":
    # Declaring Processes
    p1=multiprocessing.Process(target=square_numbers)
    p2=multiprocessing.Process(target=cube_numbers)
    starttime=time.time()

    # Starting Processes
    p1.start()
    p2.start()

    # Waiting for processes to complete
    p1.join()
    p2.join()

    execution_time=time.time()-starttime
    print(f"Execution Time: {execution_time}")