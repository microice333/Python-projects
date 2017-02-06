# program to getting prime numbers while user choose to stop
def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_next_prime(n):
    find = False
    while not find:
        n += 1
        find = is_prime(n)
    return n


def main():
    n = 2
    stop = False
    print(n)
    while not stop:
        decision = int(input("Type 1 if u want next prime number otherwise type 0"))
        if decision == 0:
            stop = True
        else:
            n = get_next_prime(n)
            print(n)


if __name__ == '__main__':
    main()
