file = open('day5.csv', 'r')
lines = file.readlines()
lines = [line.strip('\n' ',') for line in lines]


seat_IDs = []

for line in lines:
    FB = line[0:7]
    FB = FB.replace("F", "0")
    FB = FB.replace("B", "1")
    FB_2 = int(FB, 2)

    RL = line[7:]
    RL = RL.replace("L", "0")
    RL = RL.replace("R", "1")
    RL_2 = int(RL, 2)

    seat_IDs.append(FB_2*8 + RL_2)

print(max(seat_IDs))

seat_IDs = sorted(seat_IDs)

for i in range(1, len(seat_IDs)):
    if seat_IDs[i] - seat_IDs[i-1] > 1:
        print(str(seat_IDs[i]) + ", " + str(seat_IDs[i-1]))
        break
