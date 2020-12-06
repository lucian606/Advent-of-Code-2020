def xor(a, b):
    return a ^ b

input_file = open('input.txt','r')
lines = input_file.readlines()
valid_passwords = 0
new_valid_passwords = 0

for line in lines:
    args = line.split(" ")
    args[0] = args[0].split("-")
    lower_bound = int(args[0][0])
    upper_bound = int(args[0][1])
    chr = args[1][0]
    password = args[2]
    occurences = password.count(chr)
    if occurences >= lower_bound and occurences <= upper_bound:
        valid_passwords += 1

print(f"First part: {valid_passwords}")

for line in lines:
    args = line.split(" ")
    args[0] = args[0].split("-")
    first_index = int(args[0][0])
    second_index = int(args[0][1])
    chr = args[1][0]
    password = args[2]
    password = " " + password
    if xor(password[first_index] == chr, password[second_index] == chr):
        new_valid_passwords += 1

print(f"Second part: {new_valid_passwords}")
