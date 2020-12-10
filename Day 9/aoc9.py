numbers = []
width = 25
with open('input.txt') as input_file:
    for line in input_file:
        num = int(line)
        numbers.append(num)

for i in range(width, len(numbers)):
    valid = False
    weakness_list = []
    for k in range(i - width, i):
        for j in range (i - width, i):
            if numbers[k] + numbers[j] == numbers[i]:
                valid = True
    if not valid:
        print(f"Part One: {numbers[i]}")
        temp_list = numbers[0:i]
        weakness_list = []
        for start in range(0, len(temp_list)):
            current_list = []
            for k in range(start, len(temp_list)):
                current_list.append(temp_list[k])
                if sum(current_list) > numbers[i]:
                    break
                elif sum(current_list) == numbers[i] and len(current_list) >= 2:
                    weakness_list = current_list
                    break
        weakness_list.sort()
        print(f"Part Two: {weakness_list[0] + weakness_list[-1]}")