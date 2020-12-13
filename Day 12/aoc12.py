def RotateLeft(initial, angle):
    directionOffset = int(angle / 90)
    new = initial
    new -= (directionOffset % 4)
    if new < 0:
        new = -new % 4
        new = 4 - new
    return new

def RotateRight(initial, angle):
    directionOffset = int(angle / 90)
    new = initial
    new += (directionOffset % 4)
    if new > 3:
        new = new % 4
    return new

with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

directions = {'E':0, 'S':1, 'W':2, 'N':3}
direction_values = [0, 0, 0, 0] 
directionString = 'ESWN'
curr_dir = 0

for line in lines:
    direction = line[0]
    value = int(line[1:])
    if direction in directionString:
        direction_values[directions[direction]] += value
    elif direction == 'F':
        direction_values[curr_dir] += value
    elif direction == 'L':
        curr_dir = RotateLeft(curr_dir, value)
    elif direction == 'R':
        curr_dir = RotateRight(curr_dir, value)

distance = abs(direction_values[0] - direction_values[2]) + abs(direction_values[1] - direction_values[3])
print(f"Part One: {distance}")

directionString = 'ESWN'
waypoint = [1, 10]
position = [0, 0]

for line in lines:
    direction = line[0]
    value = int(line[1:])
    value = value % 360
    
    if direction in directionString:
        if direction == 'N':
            waypoint[0] += value
        if direction == 'S':
            waypoint[0] -= value
        if direction == 'E':
            waypoint[1] += value
        if direction == 'W':
            waypoint[1] -= value

    elif direction == 'F':
        a = waypoint[0]
        b = waypoint[1]
        position[0] += (value * a)
        position[1] += (value * b)
    
    elif direction == 'L' and value == 90 or direction == 'R' and value == 270:
        a = waypoint[1]
        b = waypoint[0] * -1
        waypoint[0] = a
        waypoint[1] = b

    elif direction == 'R' and value == 90 or direction == 'L' and value == 270:
        a = waypoint[1] * -1
        b = waypoint[0]
        waypoint[0] = a
        waypoint[1] = b

    elif (direction == 'L' or direction == 'R') and value == 180:
        waypoint[0] *= -1
        waypoint[1] *= -1

distance = abs(position[0]) + abs(position[1])
print(f"Part Two: {distance}")