file = open('day6.csv', 'r')
lines = file.readlines()
lines = [line.strip('\n' ',') for line in lines]

#PART 1: Remove \n from input file
answers = 0
for line in lines:
    characters = list(line)
    Dict = list(dict.fromkeys(characters))
    answers += len(Dict)

#print(answers)

#PART 2
line_no = 0
answers = 0
while line_no < len(lines):
    group_size = 0
    group_answers = ""
    if lines[line_no] == "":
        line_no += 1
        continue

    while line_no < len(lines) and lines[line_no] != "":
        group_answers += lines[line_no]
        group_size += 1
        line_no += 1

    options = list(dict.fromkeys(list(group_answers)))
    for option in options:
        if group_answers.count(option) == group_size:
            answers += 1

print(answers)
