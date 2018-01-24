import multiprocessing
import os

def factorial(number):
    for i in range(number-1, 0, -1):
        number = number * i
    return number

# for i in range(0, 5):
print('this is parent!')

for i in range(1, 10):
    tid = os.fork()
    if tid:
        print('Hello from child: %d' % tid)
        print('the factorial of {} is {}'.format(i, factorial(i)))
    else:
        print('closing')
        os._exit(0)


