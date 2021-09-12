def func():
    with open('input.txt', 'r') as f:
        buildings = list(f.readline().strip().split())

    def getHomesAndShops(buildings):
        homes = []
        shops = []
        for i in range(len(buildings)):
            if buildings[i] == '1':
                homes.append(i)
            if buildings[i] == '2':
                shops.append(i)
        return findMax(homes, shops)

    def findMax(homes, shops):
        maxr = 0
        for home in homes:
            max = min([abs(home - shop) for shop in shops])
            if max > maxr:
                maxr = max
        return maxr

    ans = getHomesAndShops(buildings)

    with open('output.txt', 'w') as f:
        f.write(str(ans))

if __name__ == '__main__':
    func()