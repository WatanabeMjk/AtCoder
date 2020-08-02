A, B, M = map(int, input().split())
aryAPrice = list(map(int, input().strip().split()))
aryBPrice = list(map(int, input().strip().split()))
aryDiscount = [[0]*3]*M
for i in range(M):
    aryDiscount[i] = list(map(int, input().strip().split()))

intABest = aryAPrice[0]
intBBest = aryBPrice[0]
for i in aryAPrice:
    if intABest > i:
        intABest = i

for i in aryBPrice:
    if intBBest > i:
        intBBest = i

bestSum = intABest + intBBest

index = 0
for i in range(M):
    hikaku = aryAPrice[aryDiscount[index,0]] + aryBPrice[aryDiscount[index,1]] - aryDiscount[index,2]
    if bestSum > hikaku:
        bestSum = hikaku

    index += 1

print(bestSum)