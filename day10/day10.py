def count_substring(input, sub):
	count = 0
	for j in range(0, len(input)):
		if input[j:j+len(sub)] == sub:
			count += 1

	return count

file = open('day10.csv', 'r')
lines = file.readlines()
lines = [int(line) for line in lines]

lines.sort()

lines = [0] + lines + [max(lines) + 3]

string = "3"

for i in range(1, len(lines)):
	string += str(lines[i] - lines[i-1])

five = count_substring(string, "311113")
four = count_substring(string, "31113")
three = count_substring(string, "3113")

print(f'{pow(7,five)} * {pow(4, four)} * {pow(2, three)}')
print(f'7^{five} * 4^{four} * 2^{three}')
print(pow(7,five) * pow(4, four) * pow(2, three))
