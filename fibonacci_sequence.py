# generate sequence of fibonacii numbers to nth number
# we assume that F0 = 0

def fib_sequence(n):
    current = 0
    next = 1
    seq = [current]
    for _ in range(n):
        current, next = next, current + next
        seq.append(current)
    return seq


n = int(input("Type the index of last fibonnaci number:"))
fib_numbers = fib_sequence(n)
print(fib_numbers)
