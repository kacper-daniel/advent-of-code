data = open('inputs/day10_input.txt', 'r').read().split('\n')

position = [0,0]
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "S":
            position = [i,j]

whole_loop = [[position[0], position[1]], [position[0]-1, position[1]]]
position = [position[0]-1, position[1]]
last_move = [-1, 0]
steps = 1
while data[position[0]][position[1]] != "S":
    if data[position[0]][position[1]] == "|":
        if last_move == [1, 0]:
            position = [position[0] + 1, position[1]]
        else:
            position = [position[0] - 1, position[1]]
            last_move = [-1, 0]
    elif data[position[0]][position[1]] == "-":
        if last_move == [0, 1]:
            position = [position[0], position[1] + 1]
        else:
            position = [position[0], position[1] - 1]
            last_move = [0, -1]
    elif data[position[0]][position[1]] == "L":
        if last_move == [1, 0]:
            position = [position[0], position[1] + 1]
            last_move = [0, 1]
        else:
            position = [position[0] - 1, position[1]]
            last_move = [-1, 0]
    elif data[position[0]][position[1]] == "J":
        if last_move == [1, 0]:
            position = [position[0], position[1] - 1]
            last_move = [0, -1]
        else:
            position = [position[0] - 1, position[1]]
            last_move = [-1, 0]
    elif data[position[0]][position[1]] == "7":
        if last_move == [-1, 0]:
            position = [position[0], position[1] - 1]
            last_move = [0, -1]
        else:
            position = [position[0] + 1, position[1]]
            last_move = [1, 0]
    elif data[position[0]][position[1]] == "F":
        if last_move == [-1, 0]:
            position = [position[0], position[1] + 1]
            last_move = [0, 1]
        else:
            position = [position[0] + 1, position[1]]
            last_move = [1, 0]
    steps += 1
    whole_loop.append([position[0], position[1]])
print(steps // 2)

# part two

map = [[c for c in line.strip()] for line in data]
for i in range(len(map)):
    norths = 0
    for j in range(len(map[i])):
        place = map[i][j]
        if [i,j] in whole_loop:
            if place in ["|", "L", "J", "S"]:
                norths += 1
            continue
        if norths % 2 == 0:
            map[i][j] = "O"
        else:
            map[i][j] = "I"
enclosed = "\n".join(["".join(line) for line in map]).count("I")
print(enclosed)
            
