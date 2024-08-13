test = ['a', 'b', 'c', 'd', 'e']

katz_deli = []

def line(deli_line):
    if len(deli_line) == 0:
        print("The line is currently empty.")
    else:
        ret_str = "The line is currently:"
        for i in range(len(deli_line)):
            person_position = i + 1
            current_person = deli_line[i]
            ret_str += f' {person_position}. {current_person}'
        print(ret_str)

def take_a_number(deli_line, person):
    deli_line.append(person)
    print(f'Welcome, {person}. You are number {len(deli_line)} in line.')

def now_serving(deli_line):
    if len(deli_line) == 0:
        print('There is nobody waiting to be served!')
    else:
        print(f'Currently serving {deli_line.pop(0)}.')