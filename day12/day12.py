def move_direction(dir):
    global EW, NS
    if dir == 'E':
        EW += distance
    elif dir == 'W':
        EW -= distance
    elif dir == 'N':
        NS -= distance
    elif dir == 'S':
        NS += distance

file = open('day12.csv', 'r')
lines = file.readlines()
grid = [[char for char in line.strip()] for line in lines]

counter = 0
NS = 0
EW = 0
direction = 'E'

compass = ['N', 'E', 'S', 'W', 'N', 'E', 'S', 'W']

for line in lines:
    distance = int(line[1:])
    #print(line.strip())
    if line[0] == 'L':
        direction = compass[compass.index(direction) - int(distance/90)]
    elif line[0] == 'R':
        direction = compass[compass.index(direction) + int(distance/90)]
    elif line[0] == 'F':
        move_direction(direction)
    else:
        move_direction(line[0])
    #print(f'NS: {NS}, EW: {EW}\n')

print(f'NS: {NS}, EW: {EW}')
print(abs(NS) + abs(EW))
