file = open('input.csv', 'r')
lines = file.readlines()
lines = [line.strip('\n' ',') for line in lines]

buses = lines[0].split(',')


def example():
    t = 100000000000000
    while True:
        # if t%7 + (t+1)%13 + (t+4)%59 + (t+6)%31 + (t+7)%19 == 0:
        if t%13 + (t+3)%41 + (t+7)%37 + (t+13)%659 + (t+32)%19 + (t+36)%23 + (t+42)%29 + (t+44)%409 + (t+61)%17 == 0:
            break
        t += 1
    print(t)


def setup():
    t = 0
    found = False
    while True:
        bus_index = 0
        for i in range(len(buses)):
            if buses[i] == 'x':
                bus_index += 1
                continue
            if (t+i) % int(buses[i]) != 0:
                break
            if i == len(buses)-1:
                found = True
            bus_index += 1

        if found:
            break
        
        t += 1
    print(t)


def main():
    pass


if __name__ == "__main__":
    example()
    # setup()
    # main()