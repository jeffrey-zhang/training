import time
from threading import Thread


def count_down(n):
    while n > 0:
        n -= 1


n = 100000000

t1 = Thread(target=count_down, args=[n // 2])
t2 = Thread(target=count_down, args=[n // 2])
start_time = time.perf_counter()
t1.start()
t2.start()
t1.join()
t2.join()
end_time = time.perf_counter()
print(f'time takes {end_time - start_time} seconds')


def apply_discount(price, discount):
    updated_price = price * (1 - discount)
    assert 0 <= updated_price <= price, 'price should be greater or equal to 0'
    return updated_price


print(apply_discount(100, 0.2))
print(apply_discount(100, 2))
