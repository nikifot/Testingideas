import multiprocessing
import os

# for i in range(0, 5):
print('this is parent!')
tid = os.fork()
for i in range(5):
    if tid == 0:
        print('Hello from child: %d' % os.getpgid(tid))


