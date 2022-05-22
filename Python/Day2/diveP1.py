file = open("inputP1.txt", "r")

rows = [line.replace("\n", "") for line in file.readlines()]

direction_dict = {"forward": 0, "down": 0, "up": 0}
aim = 0;
depth = 0;

for direction in rows:
    if  "forward" in direction:
        direction_dict["forward"] += int(direction[-1])
        depth += aim * int(direction[-1])
    elif  "down" in direction:
        direction_dict["down"] += int(direction[-1])
        aim += int(direction[-1])
    elif  "up" in direction:
        direction_dict["up"] += int(direction[-1])
        aim -= int(direction[-1])
    else:
        continue

print(direction_dict["forward"] * depth)