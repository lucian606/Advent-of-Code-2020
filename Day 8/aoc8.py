input_file = open("input.txt", 'r')
lines = input_file.readlines()
visited = [False] * len(lines)
accumulator = 0
pc = 0

while pc < (len(lines)):
    if visited[pc]:
        break
    if pc == len(lines):
        break
    visited[pc] = True
    lines[pc] = lines[pc].replace('\n', '')
    line = lines[pc]
    instr, offsetStr = line.split(' ')
    offset = int(offsetStr)
    if instr == 'acc':
        accumulator += offset
        pc += 1
    elif instr == 'jmp':
        pc += offset
    else:
        pc += 1 

print(f"Part one: {accumulator}")

finish_accumulator = -1

for instruction_switched in range(len(lines)):
    current_accumulator = 0
    pc = 0
    finished = False
    visited = [False] * len(lines)
    while True:
        if pc >= len(lines):
            finished = True
            break
        if visited[pc]:
            break
        visited[pc] = True
        line = lines[pc]       
        instr, offsetStr = line.split(' ')
        offset = int(offsetStr)
        if pc == instruction_switched:
            if instr == 'nop':
                instr = 'jmp'
            elif instr == 'jmp':
                instr = 'nop'
        if instr == 'acc':
            current_accumulator += offset
            pc += 1
        elif instr == 'jmp':
            pc = pc + offset
        else:
            pc += 1
    if finished:
        finish_accumulator = current_accumulator
        break

print(f"Part Two: {finish_accumulator}")
input_file.close()