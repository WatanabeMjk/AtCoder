def inputlist():
    return [int(i) for i in input().split()]


def main():
    N, K = inputlist()
    aryNum = [0] * N

    aryInput = []
    for i in range(K):
        intNumType = int(input())
        aryInput = inputlist()
        for j in range(len(aryInput)):
            aryNum[aryInput[j] - 1] += 1

    sum = 0
    for i in range(N):
        if aryNum[i] == 0:
            sum += 1

    print(sum)


if __name__ == '__main__':
    main()
