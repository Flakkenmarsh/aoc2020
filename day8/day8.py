file = open('day8.csv', 'r')
lines = file.readlines()
lines = [line.strip('\n' ',') for line in lines]

instructions = lines

acc = 0
index = 0
used_indices = []
while not used_indices.__contains__(index):
    used_indices.append(index)
    instruction = instructions[index].split(" ")[0]
    value = int(instructions[index].split(" ")[1])
    if instruction == "acc":
        acc += value
        index += 1
    elif instruction == "jmp":
        index += value
    elif instruction == "nop":
        index += 1

print(acc)

#Part 1 only
