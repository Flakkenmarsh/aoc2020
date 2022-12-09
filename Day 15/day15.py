# file = open('15input.csv', 'r')
# lines = file.readlines()
lines = ["10,16,6,0,1,17"]  # [line.strip('\n' ',') for line in lines]
# lines = ["0,3,6"]  # [line.strip('\n' ',') for line in lines]


def part1():
    line = lines[0].split(",")
    line = [int(c) for c in line]
    turn = 1
    numbers = {}
    for i in line:
        numbers[i] = []
        numbers[i].append(turn)
        turn += 1
    last = line[-1]
    spoken = 0
    while turn <= 2020:
        if numbers.__contains__(last) and len(numbers[last]) > 1:
            spoken = turn - 1 - numbers[last][-2]
            if not numbers.__contains__(spoken):
                numbers[spoken] = []
            numbers[spoken].append(turn)
        else:
            spoken = 0
            if not numbers.__contains__(spoken):
                numbers[spoken] = []
            numbers[spoken].append(turn)
        turn += 1
        line.append(spoken)
        last = spoken

    print(line[-1])


def add_to_dict(dict, key, val):
    if not dict.__contains__(key):
        dict[key] = []
    dict[key].append(val)


def puzzle(turns):
    line = lines[0].split(",")
    line = [int(c) for c in line]
    turn = 1
    numbers = {}
    for i in line:
        numbers[i] = []
        numbers[i].append(turn)
        turn += 1
    last = line[-1]
    spoken = 0
    while turn <= turns:
        if turn % 500000 == 0:
            print(int(turn/500000), "/", int(turns/500000))
        if numbers.__contains__(last) and len(numbers[last]) > 1:
            spoken = turn - 1 - numbers[last][-2]
        else:
            spoken = 0

        add_to_dict(numbers, spoken, turn)
        turn += 1
        line.append(spoken)
        last = spoken

    print(line[-1])


if __name__ == "__main__":
    # puzzle(2020)
    puzzle(30000000)
