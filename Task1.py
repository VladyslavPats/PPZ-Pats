def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def fibonacci_seq_generator():
    a, b = 0, 1
    while True:
        if is_prime(b):
            yield b
        a, b = b, a + b

fib_gen = fibonacci_seq_generator()
for _ in range(10):
    print(next(fib_gen))