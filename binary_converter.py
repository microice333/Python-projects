def main():
    option = input("Type 'decimal' for decimal number or 'binary' for binary ")
    number = input("Type number ")
    if option == 'decimal':
        number = int(number)
    if isinstance(number, int):
        print(bin(number)[2:])
    else:
        print(int(number, 2))


if __name__ == '__main__':
    main()
