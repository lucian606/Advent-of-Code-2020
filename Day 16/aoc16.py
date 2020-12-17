from collections import defaultdict

with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

parse_ticket_info = True
parse_my_ticket = False
parse_other_tickets = False
my_ticket = []
tickets = []
valid_tickets = []
keys = []
field_limits = {}

for line in lines:
    if line == '\n':
        parse_ticket_info = False
        parse_my_ticket = False
        continue
    line = line.replace('\n', '')
    if line == 'your ticket:':
        parse_my_ticket = True
        continue
    if line == 'nearby tickets:':
        parse_other_tickets = True
        continue
    if parse_ticket_info:
        dict_entry = line.split(': ')[0]
        keys.append(dict_entry)
        components = line.split(': ')[1]
        components = components.split(' ')
        first_limit_str = components[0]
        first_limit = first_limit_str.split('-')
        first_limit = tuple(list(map(int, first_limit)))
        second_limit_str = components[2]
        second_limit = second_limit_str.split('-')
        second_limit = tuple(list(map(int, second_limit)))
        touples = [first_limit, second_limit]
        field_limits[dict_entry] = touples
    if parse_my_ticket:
        numbers = list(map(int, line.split(',')))
        my_ticket = numbers
    if parse_other_tickets:
        ticket = list(map(int, line.split(',')))
        tickets.append(ticket)

limits = list(field_limits.values())
completed = [False] * len(keys)
completed_fields = []
error_rate = 0
indexes = []
result = 1

for ticket in tickets:
    valid_ticket = True
    for field in ticket:
        is_Valid = False
        for first_limit, second_limit in limits:
            if field >= first_limit[0] and field <= first_limit[1]:
                is_Valid = True
                break
            if field >= second_limit[0] and field <= second_limit[1]:
                is_Valid = True
                break
        if not is_Valid:
            error_rate += field
            valid_ticket = False
    if valid_ticket:
        valid_tickets.append(ticket)        

print(f'Part One: {error_rate}')
possible_fields = defaultdict(list)

for field in range(len(valid_tickets[0])):
    field_list = []
    for ticket in range(len(valid_tickets)):
        valid_fields = []
        current_field = valid_tickets[ticket][field]
        for i in range(len(limits)):
            limit_lst = limits[i]
            for j in range(2):
                limit = limit_lst[j]
                if current_field >= limit[0] and current_field <= limit[1]:
                    valid_fields.append(i)
        field_list.append(valid_fields)
    field_list = list(map(set, field_list))
    common_elements = list(field_list[0].intersection(*field_list))
    for element in common_elements:
        field_str = keys[element]
        possible_fields[field].append(field_str)

for i in range(len(keys)):
    for position, fields in possible_fields.items():
        if len(fields) == 1 and completed[position] == False:
            completed[position] = True
            completed_field = fields[0]
            if "departure" in completed_field:
                indexes.append(position)
            for key in possible_fields.keys():
                if key == position:
                    continue
                if fields[0] in possible_fields[key]:
                    possible_fields[key].remove(completed_field)

for index in indexes:
    result *= my_ticket[index]

print(f'Part Two: {result}')