file = open('day6.csv', 'r')
lines = file.readlines()
lines = [line.strip('\n' ',') for line in lines]
#characters = [list(line) for line in lines]
#Dict = list(dict.fromkeys(characters))

