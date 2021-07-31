import math

def compute(N):
    factorial = math.factorial(N)
    sum_of_digits = sum([int(digit) for digit in str(factorial)])
    return sum_of_digits

if __name__ == "__main__":
    N = 100
    print(compute(N))
