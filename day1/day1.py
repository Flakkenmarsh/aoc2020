file = open('day1.csv', 'r')
lines = file.readlines()
lines = [line.strip('\n' ',') for line in lines]
numbers = [int(s) for s in lines]

def test_method(val):
    return val

#a comment on society
sum = 0

for line in lines:
    pass #sum += int(line)

for i in range(1,len(numbers)):
    if numbers[i] > numbers[i-1]:
        sum += 1

print (sum)
quit()
