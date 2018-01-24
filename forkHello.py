import multiprocessing
import os
import time

def factorial(number):
    time.sleep(5)
    for i in range(number-1, 0, -1):
        number = number * i
    return number

# for i in range(0, 5):
print('this is parent!')

t0 = time.time()
for i in range(100, 110):
    tid = os.fork()
    if tid:
        print('Hello from child: %d' % tid)

    else:
        print('the factorial of {} is {}'.format(i, factorial(i)))
        print('closing')
        os._exit(0)

t1 = time.time()
print('multithreading: {}'.format(t1-t0))

t0 = time.time()
for i in range(1, 10):

    print('Hello from child:')
    print('the factorial of {} is {}'.format(i, factorial(i)))

t1 = time.time()
print('serial: {}'.format(t1-t0))