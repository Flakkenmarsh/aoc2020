file = open('input.csv', 'r')
lines = file.readlines()
lines = [line.strip('\n' ',') for line in lines]


def setup():
    line = lines[0].split(",")
    line = [int(c) for c in line]
    turn = 1
    numbers = {}
    for i in line:
        print(i, end=",")
        numbers[i] = []
        numbers[i].append(turn)
        turn += 1
    last = line[-1]
    spoken = 0
    while turn <= 2020:
        if numbers.__contains__(last) and len(numbers[last]) > 1:
            spoken = turn - 1 - numbers[last][-1]
            numbers[spoken].append(turn)
        else:
            spoken = 0
            if not numbers.__contains__(spoken):
                numbers[spoken] = []
            numbers[spoken].append(turn)
            last = 0
        turn += 1
        line.append(spoken)
        print(spoken, end=",")
    print("")
    print(line)
    print(numbers)


if __name__ == "__main__":
    setup()
