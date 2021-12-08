file = open('day3.csv', 'r')
lines = file.readlines()
lines = [line.strip('\n' ',') for line in lines]
#numbers = [int(s) for s in lines]
#characters = [list(line) for line in lines]

def test_method(val):
    return val

trees = 0

row = 0
col = 0
right = 1
down = 2

while row < len(lines):
    if col >= len(lines[0]):
        col -= len(lines[0])
    if lines[row][col] == '#':
        trees += 1

    row += down
    col += right

print(trees)


