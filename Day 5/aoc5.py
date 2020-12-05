input_file = open('input.txt', 'r')
lines = input_file.readlines()
highestId = 0
lowestId = 0
seats = []

for line in lines:
    row = 0
    column = 0
    for i in range(0, 7):
        chr = line[i]
        offset = 6 - i
        bit = -1
        if chr == "F":
            bit = 0
        else:
            bit = 1
        row += (bit << offset)
    for i in range(7, 10):
        chr = line[i]
        offset = 2 - (i % 7)
        bit = 0
        if chr == "L":
            bit = 0
        else:
            bit = 1
        column += (bit << offset)
    currentId = row * 8 + column
    if currentId > highestId:
        highestId = currentId
    seats.append(currentId)

print(highestId)
seats.sort()
lowestId = seats[0]
for num in range(lowestId, highestId):
    if not num in seats:
        print(num)