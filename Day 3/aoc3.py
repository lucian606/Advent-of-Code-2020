input_file = open('input.txt','r')
lines = input_file.readlines()
line_count = len(lines)
start_col = 3
trees = 0
total_trees = 1

for i in range(1, line_count):
    line = lines[i]
    n = len(line)
    if line[-1] == '\n':
        line = line[:n - 1]
    while len(line) - 1 <= start_col:
       line *= 2;
    lines[i] = line
    if line[start_col] == '#':
        trees += 1
    start_col += 3

print(trees)

for k in range(1, 8, 2):
    start_col = k
    trees = 0
    for i in range(1, line_count):
        line = lines[i]
        n = len(line)
        while len(line) - 1 <= start_col:
            line *= 2;
        if line[start_col] == '#':
            trees += 1
        start_col += k
    total_trees *= trees

start_col = 1
trees = 0
for i in range(2, line_count, 2):
    line = lines[i]
    n = len(line)
    if line[start_col] == '#':
        trees += 1
    start_col += 1
total_trees *= trees

print(total_trees)
