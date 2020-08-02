def main():
    N = int(input()) + 1
    intSum = 0
    for num in range(N):
        if (num % 3 != 0) and (num % 5 != 0):
            intSum += int(num)

    print(intSum)


if __name__ == '__main__':
    main()
