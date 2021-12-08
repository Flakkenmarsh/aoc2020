file = open('day2.csv', 'r')
lines = file.readlines()
lines = [line.strip('\n' ',') for line in lines]
#numbers = [int(s) for s in lines]

def test_method(val):
    return val

isum = 0

newarray = []

for line in lines:
    params = line.split(' ')
    numbers = params[0].split('-')
    min = int(numbers[0]) - 1
    max = int(numbers[1]) - 1
    character = params[1]
    string = params[2]

    if string[min] == character or string[max] == character:
        isum += 1

    if string[min] == character and string[max] == character:
        isum -= 1
    #count = string.count(character)

    #if (count >= min) and (count <= max):
     #   isum += 1


print(isum)
