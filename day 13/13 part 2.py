file = open('input.csv', 'r')
# bus_ids = "7,13,x,x,59,x,31,19"  # 1068781
# bus_ids = "17,x,13,19"  # is 3417.
# bus_ids = "67,7,59,61"  # first occurs at timestamp 754018.
# bus_ids = "67,x,7,59,61"  # first occurs at timestamp 779210.
# bus_ids = "67,7,x,59,61"  # first occurs at timestamp 1261476.
# bus_ids = "1789,37,47,1889"  # first occurs at timestamp 1202161486.
bus_ids = "13,x,x,41,x,x,x,37,x,x,x,x,x,659,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,23,x,x,x,x,x,29,x,409,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17"


class Bus:
    def __init__(self, offset, mod):
        self.offset = offset
        self.bi = (mod - (offset % mod)) % mod
        self.mod = mod
        self.Ni = 0
        self.xi = 0

    def biNixi(self):
        return self.bi * self.Ni * self.xi


def setup():
    buses0 = bus_ids.split(",")
    buses = []
    N = 1
    for i in range(len(buses0)):
        if buses0[i] == 'x':
            continue
        N *= int(buses0[i])
        buses.append(Bus(i, int(buses0[i])))

    for bus in buses:
        bus.Ni = N // bus.mod
        x = bus.Ni % bus.mod
        i = 1
        while (x*i) % bus.mod != 1:
            i += 1
        bus.xi = i

    binixi = 0
    for bus in buses:
        binixi += bus.biNixi()
    print(int(binixi % N))


if __name__ == "__main__":
    setup()
