f = open("input1.txt", "r")

list = list(map(int, f.readlines()))
countList  = []

count = 0
for i, level in enumerate(list):
    if (i + 2) >= len(list):
        break
    countList.append(list[i] + list[i + 1] + list[i + 2])

count = 0
for i, level in enumerate(countList):
    if (i + 1) >= len(countList):
        break
    if (countList[i + 1] > countList[i]):
        count += 1

print(count)