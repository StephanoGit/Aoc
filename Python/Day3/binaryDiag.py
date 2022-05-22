def binaryToDecimal(b):
    power = len(b) - 1
    result = 0
    for number in b:
        result += int(number) * 2 ** power
        power -= 1

    return result

file = open("inputP1.txt", "r")

rows = [list(map(int, line[:-1])) for line in file.readlines()]

counter = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
           [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

for sublist in rows:
    for index, number in enumerate(sublist):
        if number == 0:
            counter[index][0] += 1
        if number == 1:
            counter[index][1] += 1

gamma = ""
epsilon = ""

for list in counter:
    if list[0] > list[1]:
        gamma = gamma + "0"
        epsilon = epsilon + "1"
    else:
        gamma = gamma + "1"
        epsilon = epsilon + "0"

print("Gamma bin: " + gamma)
print("Gamma dec: " + str(binaryToDecimal(gamma)))
print("Epsilon bin: " + epsilon)
print("Epsilon dec: " + str(binaryToDecimal(epsilon)))
print("Power consumption: " + str(binaryToDecimal(gamma) * binaryToDecimal(epsilon)))