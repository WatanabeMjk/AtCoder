def inputlist():
    return [int(i) for i in input().split()]


def main():
    A, B, C, D = inputlist()
    boolTurnTaka = True
    while A > 0 and C > 0:
        if boolTurnTaka:
            C -= B
            boolTurnTaka = False
        else:
            A -= D
            boolTurnTaka = True

    if A <= 0:
        print("No")
    else:
        print("Yes")


if __name__ == '__main__':
    main()
