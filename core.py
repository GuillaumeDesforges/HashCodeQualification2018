class Ride:
    def __init__(self, x0, y0, x1, y1, ti, tf):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.ti = ti
        self.tf = tf

    def __str__(self):
        return ' '.join([str(self.x0), str(self.y0), str(self.x1), str(self.y1), str(self.ti), str(self.tf)])

def read(file_path):
    with open(file_path) as f:
        lines = [line.replace("\n", "") for line in f.readlines()]
        R, C, F, N, B, T = tuple(map(int, lines[0].split(" ")))
        rides = []
        for line in lines[1:]:
            ride = Ride(*tuple(map(int, lines[0].split(" "))))
            rides.append(ride)
        return R, C, F, N, B, T, rides

if __name__ == "__main__":
    print(*read("a_example.in"))
