import multiprocessing
import time

def square(num):
    """calculates square of a number """
    # print("Working in: ", multiprocessing.current_process().name)
    return num ** 2

def start_process():
    print("Starting ", multiprocessing.current_process().name)

if __name__ == '__main__':
    pool_size = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(processes=pool_size, initializer=start_process)
    numbers = list(range(20))
    outputs = pool.map(square, numbers)
    print("Output :", outputs)
    pool.close()  # no more tasks
    pool.join()  # wait for the worker processes to exit
    