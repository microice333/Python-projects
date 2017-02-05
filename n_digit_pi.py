#generate pi to nth digit
# Chudnovsky algorihtm from https://en.wikipedia.org/wiki/Chudnovsky_algorithm
import decimal

def compute_pi(n):
    decimal.getcontext().prec = n
    C = 426880 * decimal.Decimal(10005).sqrt()
    K = 6.
    M = 1.
    X = 1
    L = 13591409
    S = L
    for i in range(1, n):
        M = M * (K ** 3 - 16 * K) / ((i + 1) ** 3)
        L += 545140134
        X *= -262537412640768000
        S += decimal.Decimal(M * L) / X
    pi = C / S
    return pi

n = int(input())
print (compute_pi(n))