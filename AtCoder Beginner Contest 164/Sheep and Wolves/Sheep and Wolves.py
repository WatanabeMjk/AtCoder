def inputlist():
    return [int(i) for i in input().split()]


def main():
    S, W = inputlist()
    if S > W:
        print("safe")
    else:
        print("unsafe")


if __name__ == '__main__':
    main()
