file = open('day9.csv', 'r')
lines = file.readlines()
lines = [line.strip('\n' ',') for line in lines]
numbers = [int(s) for s in lines] #convert to numbers

def has_solution(preamble, target):
    print(preamble)
    print("Target: " + str(target))
    for i in range(0, len(preamble)):
        for j in range(i+1, len(preamble)):
            if preamble[i] + preamble[j] == target:
                print("Found")
                return True

    return False

preamble_size = 25
preamble = numbers[0:preamble_size]
index = 0

while index+preamble_size < len(numbers):
    preamble = numbers[index:index+preamble_size]
    if not has_solution(preamble, numbers[index+preamble_size]):
        break
    index += 1

print(numbers[index+preamble_size])