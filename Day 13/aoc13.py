with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

lines[0] = lines[0].replace('\n', '')
departure_time = int(lines[0])
busses = lines[1].split(',')
busses_task2 = busses
busses = list(filter(lambda s: s != 'x', busses))
busses = list(map(lambda s: int(s), busses))
reachable_times = list(busses)
min_idx = 0
for i in range(0, len(reachable_times)):
    id = reachable_times[i]
    while id < departure_time:
        id += busses[i]
    reachable_times[i] = id
    if id < reachable_times[min_idx]:
        min_idx = i

waiting_time = reachable_times[min_idx] - departure_time
print(f"Part One: {waiting_time * busses[min_idx]}")

busses = busses_task2
busses = list(map(lambda s: int(s) if s != 'x' else s, busses))

rems_divs = []
for i in range(len(busses)):
    if busses[i] != 'x':
        pair = (-i % busses[i],busses[i])
        rems_divs.append(pair)
        
x = 0
step = 1
for r, d in rems_divs:
    while x % d != r:
        x += step
    step *= d

print(f"Part Two: {x}")