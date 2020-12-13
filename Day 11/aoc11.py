def getNeighbours(mat, x, y):
    count = 0
    if x - 1 >= 0:
        if y - 1 >= 0 and mat[x - 1][y - 1] == '#':
            count += 1
        if mat[x - 1][y] == '#':
            count += 1
        if y + 1 < len(mat[x - 1]) and mat[x - 1][y + 1] == '#':
            count += 1
    if x + 1 < len(mat):
        if y - 1 >= 0 and mat[x + 1][y - 1] == '#':
            count += 1
        if mat[x + 1][y] == '#':
            count += 1
        if y + 1 < len(mat[x + 1]) and mat[x + 1][y + 1] == '#':
            count += 1
    if y - 1 >= 0 and mat[x][y - 1] == '#':
        count += 1
    if y + 1 < len(mat[x]) and mat[x][y + 1] == '#':
        count += 1
    return count


def checkUpAux(mat, x, y):
    if x < 0 or mat[x][y] == 'L':
        return 0
    elif mat[x][y] == '#':
        return 1
    else:
        return checkUpAux(mat, x - 1, y)

def checkUp(mat, x, y):
    return checkUpAux(mat, x - 1, y)


def checkDownAux(mat, x, y):
    if x >= len(mat) or mat[x][y] == 'L':
        return 0
    elif mat[x][y] == '#':
        return 1
    else:
        return checkDownAux(mat, x + 1, y)

def checkDown(mat, x, y):
    return checkDownAux(mat, x + 1, y)

def checkLeftAux(mat, x, y):
    if y < 0 or mat[x][y] == 'L':
        return 0
    elif mat[x][y] == '#':
        return 1
    else:
        return checkLeftAux(mat, x, y - 1)

def checkLeft(mat, x, y):
    return checkLeftAux(mat, x, y - 1)

def checkRightAux(mat, x, y):
    if y >= len(mat[0]) or mat[x][y] == 'L':
        return 0
    elif mat[x][y] == '#':
        return 1
    else:
        return checkRightAux(mat, x, y + 1)

def checkRight(mat, x, y):
    return checkRightAux(mat, x, y + 1)

def checkUpLeftAux(mat, x, y):
    if x < 0 or y < 0 or mat[x][y] == 'L':
        return 0
    elif mat[x][y] == '#':
        return 1
    else:
        return checkUpLeftAux(mat, x - 1, y - 1)

def checkUpLeft(mat, x, y):
    return checkUpLeftAux(mat, x - 1, y - 1)

def checkUpRightAux(mat, x, y):
    if x < 0 or y >= len(mat[0]) or mat[x][y] == 'L':
        return 0
    elif mat[x][y] == '#':
        return 1
    else:
        return checkUpRightAux(mat, x - 1, y +1)

def checkUpRight(mat, x, y):
    return checkUpRightAux(mat, x - 1, y + 1)

def checkDownLeftAux(mat, x, y):
    if x >= len(mat) or y < 0 or mat[x][y] == 'L':
        return 0
    elif mat[x][y] == '#':
        return 1
    else:
        return checkDownLeftAux(mat, x + 1, y - 1)

def checkDownLeft(mat, x, y):
    return checkDownLeftAux(mat, x + 1, y - 1)

def checkDownRightAux(mat, x, y):
    if x >= len(mat) or y >= len(mat[0]) or mat[x][y] == 'L':
        return 0
    elif mat[x][y] == '#':
        return 1
    else:
        return checkDownRightAux(mat, x + 1, y + 1)

def checkDownRight(mat, x, y):
    return checkDownRightAux(mat, x + 1, y + 1)

def checkSeatLines(mat, x, y):
    count = checkUp(mat, x, y) + checkDown(mat, x, y) + checkLeft(mat, x, y) + checkRight(mat, x, y)
    count += checkUpLeft(mat, x, y) + checkUpRight(mat, x, y) + checkDownLeft(mat, x, y) + checkDownRight(mat, x, y)
    return count

with open('input.txt', 'r') as input_file:
    matrix = input_file.readlines()

for i in range(len(matrix)):
    matrix[i] = matrix[i].replace('\n','')

old_matrix = list(matrix)
new_matrix = list(matrix)
steps = 0

while True:
    changed = False
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'L' and getNeighbours(matrix, i, j) == 0:
                changed = True
                lst = list(new_matrix[i])
                lst[j] = '#'
                new_matrix[i] = "".join(lst)
            elif matrix[i][j] == '#' and getNeighbours(matrix, i, j) >= 4:
                changed = True
                lst = list(new_matrix[i])
                lst[j] = 'L'
                new_matrix[i] = "".join(lst)
    if not changed:
        break
    matrix = list(new_matrix)

occupied = 0
for line in new_matrix:
    occupied += line.count('#')
print(f"Part One: {occupied}")

matrix = list(old_matrix)
new_matrix = list(matrix)

while True:
    changed = False
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'L' and checkSeatLines(matrix, i, j) == 0:
                changed = True
                lst = list(new_matrix[i])
                lst[j] = '#'
                new_matrix[i] = "".join(lst)
            elif matrix[i][j] == '#' and checkSeatLines(matrix, i, j) >= 5:
                changed = True
                lst = list(new_matrix[i])
                lst[j] = 'L'
                new_matrix[i] = "".join(lst)
    if not changed:
        break
    matrix = list(new_matrix)

occupied = 0
for line in new_matrix:
    occupied += line.count('#')
print(f"Part Two: {occupied}")