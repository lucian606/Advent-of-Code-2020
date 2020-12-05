import json

def isYearValid(yearStr):
    try:
        year = int(yearStr)
        return True
    except:
        return False

def checkYear(yearStr, lowerBound, upperBound):
    if isYearValid(yearStr):
        year = int(yearStr)
        return year >= lowerBound and year <= upperBound
    return False

def checkHgt(heightStr):
    tokens = []
    if 'cm' in heightStr:
        tokens = heightStr.split('c')
        if len(tokens) != 2:
            return False
        tokens[1] = 'c' + tokens[1]
        if tokens[1] != 'cm':
            return False
        try:
            height = int(tokens[0])
            if height >= 150 and height <= 193:
                return True
        except:
            return False
    elif 'in' in heightStr:
        tokens = heightStr.split('i')
        if len(tokens) != 2:
            return False
        tokens[1] = 'i' + tokens[1]
        if tokens[1] != 'in':
            return False
        try:
            height = int(tokens[0])
            if height >= 59 and height <= 76:
                    return True
        except:
            return False
    return False

def checkHcl(color):
    if color[0] != '#':
        return False
    for i in range(1, len(color)):
        chr = color[i]
        if not (chr.isalpha() or chr.isdigit()):
            return False
    return True

def checkEcl(color):
    return color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def checkPid(pid):
    return len(list(filter(lambda chr: chr in "0123456789", pid))) == 9

input_file = open('input.txt','r')
lines = []
passports = []
curr_line = ""
valid_passports = 0
corrert_passports = 0

while True:
    line = input_file.readline()
    if not line:
        break
    if line == "\n":
        lines.append(curr_line)
        curr_line = ""
    else:
        curr_line += line

for line in lines:
    sub_lines = line.split('\n')
    passport = {}
    for sub_line in sub_lines:
        if sub_line == "":
            continue
        pairs = sub_line.split(' ')
        for pair in pairs:
            words = pair.split(':')
            passport[words[0]] = words[1]
    passport['cid'] = 'Temp'
    if len(passport.keys()) == 8:
        valid_passports += 1
        passports.append(passport)

print(valid_passports)

for passport in passports:
    if checkYear(passport['byr'], 1920, 2002) and checkYear(passport['iyr'], 2010, 2020) and checkYear(passport['eyr'], 2020, 2030) and checkHgt(passport['hgt']) and checkHcl(passport['hcl']) and checkEcl(passport['ecl']) and checkPid(passport['pid']):
        corrert_passports += 1

print(corrert_passports)
