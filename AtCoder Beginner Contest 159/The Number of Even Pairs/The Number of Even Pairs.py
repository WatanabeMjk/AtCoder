import math


def inputlist():
    return [int(i) for i in input().split()]


def kumiawase(num):
    r = 2
    if num != 1 and num != 0:
        return math.factorial(num) // (math.factorial(num - r) * math.factorial(r))
    else:
        return 0


def main():
    N, M = inputlist()
    print(kumiawase(N) + kumiawase(M))


if __name__ == '__main__':
    main()
