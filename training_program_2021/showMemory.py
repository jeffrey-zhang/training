import os
from time import time

import psutil

# show message usage of current python program
def show_memory_inf(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024.
    print('[%s] memory usage: %.2f MB' % (hint, memory))

def test_iterator():
    show_memory_inf('initing iterator')
    list_l = [i for i in range(100000000)]
    show_memory_inf('after interator initiated')
    print(sum(list_l))
    show_memory_inf('after sum called')

def test_generator():
    show_memory_inf('initing generator')
    list_l2 = (i for i in range(100000000))
    show_memory_inf('after generator initiated')
    print(sum(list_l2))
    show_memory_inf('after sum called')

test_iterator()
test_generator()