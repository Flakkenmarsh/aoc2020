file = open('day5.csv', 'r')
lines = file.readlines()
#line = 'FBFBBFFRLR'
ids = [0]

for line in lines:
    bin1 = int(line[0:7].replace('F', '0').replace('B', '1'), 2)
    bin2 = int(line[7:10].replace('R', '1').replace('L', '0'), 2)
    ids.append(int(bin1)*8 + int(bin2))

print(max(ids))
