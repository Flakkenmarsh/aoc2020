import pprint
import copy

def count_adjacent(row, col):
    count = 0

    for i in range(row - 1, row + 2):
        if i < 0 or i >= len(grid):
            continue
        for j in range(col - 1, col + 2):
            if j < 0 or j >= len(grid[0]) or (i == row and j == col):
                continue
            if grid[i][j] == '#':
                count += 1

    return count

def count_visible_adjacent(row, col):
    count = 0
    direction = [-1, 0, 1]

    for i in range(0, 3):
        for j in range(0, 3):
            test_row = row
            test_column = col
            while True:
                test_row += direction[i]
                test_column += direction[j]
                if test_column < 0 or test_column >= len(grid[0]):
                    break
                if test_row < 0 or test_row >= len(grid):
                    break
                if direction[i] == 0 and direction[j] == 0:
                    break
                #print(f'{row + direction[i]}, {col + direction[j]}')
                if grid[test_row][test_column] == '#':
                    count += 1
                    break
                if grid[test_row][test_column] == 'L':
                    break

    return count

file = open('day11.csv', 'r')
lines = file.readlines()
grid = [[char for char in line.strip()] for line in lines]

counter = 0

grid_copy = copy.deepcopy(grid)

"""
while True:
    grid = copy.deepcopy(grid_copy)
    for k in range(0, len(grid)):
        for l in range(0, len(grid[0])):
            if grid[k][l] == 'L' and count_adjacent(k, l) == 0:
                grid_copy[k][l] = '#'
            elif grid[k][l] == '#' and count_adjacent(k, l) >= 4:
                grid_copy[k][l] = 'L'

    if grid == grid_copy:
        break
    #pprint.pprint(grid_copy)
    counter += 1

print(sum([row.count('#') for row in grid]))
print(counter)
"""

#print_grid = ["".join(line) for line in grid]
#pprint.pprint(grid)

#part 2
while True:
    grid = copy.deepcopy(grid_copy)

    #print_grid = ["".join(line) for line in grid]
    #pprint.pprint(print_grid)
    for k in range(0, len(grid)):
        for l in range(0, len(grid[0])):
            adjacent = count_visible_adjacent(k, l)
            if grid[k][l] == 'L' and adjacent == 0:
                grid_copy[k][l] = '#'
            elif grid[k][l] == '#' and adjacent >= 5:
                grid_copy[k][l] = 'L'

    if grid == grid_copy:
        break

    counter += 1

print(sum([row.count('#') for row in grid]))
