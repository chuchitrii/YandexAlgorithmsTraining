def func():
    import math

    with open('input.txt', 'r') as f:
        d = int(f.readline())
        x, y = list(map(int, f.readline().strip().split()))

    def getIndexOfPointWithMinDistance(d, x, y):
        for index, p in enumerate([{'x': 0, 'y': 0}, {'x': d, 'y': 0}, {'x': 0, 'y': d}]) :
            dMin = getDistance(x, y, p['x'], p['y'])
            if index == 0:
                dMinResult = dMin
                dMinIndex = index
            elif dMin < dMinResult:
                dMinResult = dMin
                dMinIndex = index
        return dMinIndex + 1

    def getDistance(x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    if x <= d - y and x >= 0 and y <= d - x and y >= 0:
        ans = 0
    else:
        ans = getIndexOfPointWithMinDistance(d, x, y)    

    with open('output.txt', 'w') as f:
        f.write(str(ans))

if __name__ == '__main__':
    func()