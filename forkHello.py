import multiprocessing
import os

# for i in range(0, 5):
print('this is parent!')

for i in range(5):
    tid = os.fork()
    if tid == 0:
        print('Hello from child: %d' % os.getpgid(tid))


