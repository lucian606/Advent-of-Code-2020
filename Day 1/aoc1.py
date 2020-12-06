input_file = open('input.txt','r')
lines = input_file.readlines()
numbers = list(map(lambda str: int(str), lines))
n = len(numbers)
found_pair = False
found_triplet = False

for i in range (n - 1):
    if found_pair:
        break
    for j in range (i + 1, n - 1):
        if (numbers[i] + numbers[j] == 2020):
            print(f"First part: {numbers[i] * numbers[j]}")
            found_pair = True
            
for i in range (n - 2):
    if found_triplet:
        break
    for j in range (i + 1, n - 1):
        for k in range (j + 1, n):
            if (numbers[i] + numbers[j] + numbers[k] == 2020):
                print(f"Second part: {numbers[i] * numbers[j] * numbers[k]}")
                found_triplet = False
