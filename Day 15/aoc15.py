from collections import defaultdict

with open('input.txt', 'r') as input_file:
    line = input_file.readline()

nums = list(line.split(','))
nums = list(map(lambda s: int(s), nums))
turns_dict = defaultdict(list)

for i in range(len(nums)):
    last_number = nums[i]
    turns_dict[last_number] = [i + 1]

part_one_answer = 0
part_two_answer = 0
for i in range(len(nums) + 1, 30000001):
    result = turns_dict.get(last_number)
    if len(result) < 2:
        last_number = 0
        updated_list = turns_dict[0]
        updated_list.append(i)
        turns_dict[0] = updated_list
    else:
        n = len(result)
        new_number = result[n - 1] - result[n - 2]
        last_number = new_number
        new_list = turns_dict[new_number]
        new_list.append(i)
        turns_dict[new_number] = new_list
    if i == 2020:
        part_one_answer = last_number
    if i == 30000000:
        part_two_answer = last_number

print(f"Part One: {part_one_answer}")
print(f"Part Two: {part_two_answer}")