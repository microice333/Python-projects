# find e to nth digit by brothers' formulae: http://www.intmath.com/exponential-logarithmic-functions/calculating-e.php
import decimal


def factorial(n):
    factorials = [1]
    for i in range(1, n + 1):
        factorials.append(factorials[i - 1] * i)
    return factorials


def compute_e(n):
    decimal.getcontext().prec = n + 1
    e = 2
    factorials = factorial(2 * n + 1)
    for i in range(1, n + 1):
        counter = 2 * i + 2
        denominator = factorials[2 * i + 1]
        e += decimal.Decimal(counter / denominator)
    return e


while True:
    n = int(input("Please type number between 0-1000"))
    if n >= 0 and n <= 1000:
        break

print(str(compute_e(n))[:n + 1])
