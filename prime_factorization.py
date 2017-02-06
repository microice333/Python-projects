# finding all prime factors for entered value

def generate_primes(n):
    no_primes = [j for i in range(2, int(n ** 0.5) + 1) for j in range(i ** 2, n + 1, i)]
    primes = [i for i in range(2, n + 1) if i not in no_primes]
    return primes


def factorization(n):
    if n < 2:
        return []
    prime_factors = []
    for p in generate_primes(n):
        if n % p == 0:
            prime_factors.append(p)
    return prime_factors


n = int(input("Enter the number you want to factor"))
print(factorization(n))
