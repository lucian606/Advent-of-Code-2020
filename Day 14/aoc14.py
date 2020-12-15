import re

def setBit(num, pos, value):
    if value == '1':
        bit = 1 << pos
        num = num | bit
    elif value == '0':
        bit = 1 << pos
        bit = ~bit
        num = num & bit
    return num
with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

def generatePosibleNumbers(num, positions, index, numbers):
    if (index == len(positions)):
        numbers.append(num)
        if len(numbers) == 2**len(positions):
            return
    else:
        curr_pos = positions[index]
        num = setBit(num, curr_pos, '0')
        generatePosibleNumbers(num, positions, index + 1, numbers)
        num = setBit(num, curr_pos, '1')
        generatePosibleNumbers(num, positions, index + 1, numbers)



if __name__=='__main__':
    current_mask = ""
    mem = {}
    for line in lines:
        if "mask" in line:
            line_list = line.split(' ')
            current_mask = line_list[2]
        else:
            line_list = line.split(' ')
            initial_number = int(line_list[2])
            result = re.search('\[[0-9]*\]', line_list[0])
            index_str = str(result.group(0))
            n = len(index_str)
            index_str = index_str[1:n - 1]
            for i in range(len(current_mask)):
                bit = current_mask[i]
                initial_number = setBit(initial_number, 35 - i, bit)
            mem[index_str] = initial_number

    values = mem.values()
    print(f"Part One: {sum(values)}")

    current_mask = ""
    mem = {}
    numbers = []
    for line in lines:
        floating_bits = []
        if "mask" in line:
            line_list = line.split(' ')
            current_mask = line_list[2]
        else:
            line_list = line.split(' ')
            initial_number = int(line_list[2])
            result = re.search('\[[0-9]*\]', line_list[0])
            index_str = str(result.group(0))
            n = len(index_str)
            index_str = index_str[1:n - 1]
            initial_address = int(index_str)
            for i in range(len(current_mask)):
                bit = current_mask[i]
                if bit == '1':
                    initial_address = setBit(initial_address, 35 - i, bit)
                elif bit == 'X':
                    floating_bits.append(35 - i)
            if len(floating_bits) == 0:
                numbers.append(initial_address)
            else:
                possible_numbers = []
                generatePosibleNumbers(initial_address, floating_bits, 0, possible_numbers)
                numbers = numbers + possible_numbers
                for number in possible_numbers:
                    mem[number] = initial_number
   
    print(f"Part Two: {sum(mem.values())}")