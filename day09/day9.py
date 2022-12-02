import copy

def is_valid(start, end, target):
	for i in range(start, end+1):
		for j in range(start, end+1):
			if i == j:
				continue
			if lines[i] + lines[j] == target:
				return True

	return False

file = open('day9.csv', 'r')
lines = file.readlines()
lines = [int(line) for line in lines]
preamble = 25

"""
end_index = preamble

while end_index < len(lines):
	if not is_valid(end_index - preamble, end_index-1, lines[end_index]):
		print(lines[end_index])
		break
	end_index += 1
"""
#PART 2
find_val = 90433990
#not 32745643
#not 43471562 43471562

search_start = 0
found = False
while True:
	sum_total = 0
	for i in range(search_start, len(lines)):
		sum_total += lines[i]
		if sum_total == find_val:
			found = True
			print(f'{lines[search_start]} + {lines[i]}')
			for j in range(search_start, i+1):
				print(lines[j])
			print('=====')
			print(min(lines[search_start:i+1]))
			print(max(lines[search_start:i+1]))
			print('=====')
			print(min(lines[search_start:i+1]) + max(lines[search_start:i+1]))
		if sum_total > find_val:
			break

	if found:
		break

	search_start += 1

