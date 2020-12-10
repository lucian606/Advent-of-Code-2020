def numberOfArrangements(arr):
    DP = [0] * len(arr)
    DP[0] = 1
    for i in range(0, len(arr)):
        for k in range(i + 1, len(DP)):
            if arr[k] - arr[i] <= 3:
                DP[k] += DP[i]
    return DP[-1]

joltages = []
with open('input.txt') as input_file:
    for line in input_file:
        joltage = int(line)
        joltages.append(joltage)
joltages.sort()
joltages.insert(0, 0)
joltages.append(joltages[-1] + 3)
one_jolt_diff = 0
three_jolt_diff = 0
current_joltage = 0
for joltage in joltages:
    if joltage - current_joltage == 3:
        three_jolt_diff += 1
    elif joltage - current_joltage == 1:
        one_jolt_diff += 1
    current_joltage = joltage
print(f"Part one: {one_jolt_diff * three_jolt_diff}")
print(f"Part two: {numberOfArrangements(joltages)}")