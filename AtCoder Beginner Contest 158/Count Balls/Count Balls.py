initInput = input()
tmpList = initInput.split()
inputN = int(tmpList[0])
inputA = int(tmpList[1])
inputB = int(tmpList[2])
arrayList = []
num = 0
arrayNum = 0
blueballNum = 0
while len(arrayList)  < inputN:
    if num % 2 == 0:
        for a in range(inputA):
            arrayList = arrayList + ['a']
            arrayNum = arrayNum + 1
            blueballNum = blueballNum + 1
    else:
        for b in range(inputB):
            arrayList = arrayList + ['b']
            arrayNum = arrayNum + 1
            
    num += 1

blueballNum = blueballNum - (len(arrayList) - inputN)
    
print(blueballNum)