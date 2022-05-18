f = open("input1.txt", "r")

list = list(map(int, f.readlines()))


count = 0
for i, level in enumerate(list):
    if (i + 1) >= len(list):
        break
    if list[i + 1] > list[i]:
        count += 1

print(count)