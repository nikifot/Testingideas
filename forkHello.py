import multiprocessing
import os

# for i in range(0, 5):
tid = os.fork()
if tid == 0:
    print('Hello from child')
else:
    print('this is parent!')
