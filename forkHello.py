import multiprocessing
import os

# for i in range(0, 5):
print('this is parent!')

for i in range(5):
    tid = os.fork()
    if tid:
        print('Hello from child: %d' % tid)
    else:
        print('closing')
        os.__exit__()


