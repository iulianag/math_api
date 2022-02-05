
def calculate_factorial(n: int):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


def calculate_fibonacci_number(n: int):
    t1 = 0
    t2 = 1
    s = 0
    for i in range(n+1):
        s = t1 + t2
        t1 = t2
        t2 = s
    return s
