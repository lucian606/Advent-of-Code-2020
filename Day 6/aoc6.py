input_file = open('input.txt', 'r')
lines = input_file.readlines()
total_answers = 0
unanimous_answers = 0
groups = []
current_group = ""

for line in lines:
    if line != '\n':
        current_group += line
    else:
        groups.append(current_group)
        current_group = ""
        
groups.append(current_group)

for group in groups:
    answered = [False] * 27
    for answer in group:
        if answer != '\n':
            answered[ord(answer) - ord('a')] = True
    total_answers += len(list(filter(lambda x: x, answered)))

print(f"First part: {total_answers}")

for group in groups:
    answered = [False] * 27
    members = group.count('\n')
    if group == groups[-1]:
        members += 1
    for answer in group:
        if answer != '\n':
            if group.count(answer) == members:
                answered[ord(answer) - ord('a')] = True
            else:
                answered[ord(answer) - ord('a')] = False
    unanimous_answers += len(list(filter(lambda x: x, answered)))

print(f"Second part: {unanimous_answers}")
input_file.close()