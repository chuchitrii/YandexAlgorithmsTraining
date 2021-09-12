def func():
    with open('input.txt', 'r') as f:
        N, M = list(map(int, f.readline().strip().split(' ')))
        heroes = [[h + 1] for h in range(N)]
        swaps = f.readlines()
    
    result = []
    
    def swap(i1, i2, log = True):
        heroes[i1 - 1][0], heroes[i2 - 1][0] = heroes[i2 - 1][0], heroes[i1 - 1][0]
        heroes[i1 - 1].append(i2)
        heroes[i2 - 1].append(i1)
        if log:
            result.append([i1, i2])

    def were_swapped(i1, i2):
        if i1 == i2:
            return True
        return i2 in heroes[i1 - 1][1:]

    def everybody_in_place():
        for i in range(1, N + 1, 1):
            if heroes[i - 1][0] != i:
                return False
        return True

    def exactly_swapped(i1, i2):
        return heroes[i1 - 1][0] == i2 and heroes[i2 - 1][0] == i1

    for s in swaps:
        ch = list(map(int, s.strip().split()))
        swap(ch[0], ch[1], False)

    while not everybody_in_place():
        for i1 in range(1, N + 1, 1):
            if (heroes[i1 - 1][0] != i1):
                [i2] = [i for i in range(1, N + 1, 1) if heroes[i - 1][0] == i1 and i != i1]
                if not were_swapped(i1, i2):
                    swap(i1, i2)
                elif exactly_swapped(i1, i2):
                    i3, i4 = [i for i in range(1, N + 1, 1) if not were_swapped(i, i1) and not were_swapped(i, i2)][:2]
                    swap(i1, i3)
                    swap(i2, i4)
                    swap(i3, i2)
                    swap(i4, i1)
                    if not were_swapped(i3, i4):
                        swap(i3, i4)
                else:
                    [i3] = [i for i in range(1, N + 1, 1) if not were_swapped(i, i1) and not were_swapped(i, i2)][:1]
                    swap(i2, i3)
                    swap(i1, i3)

    print(result)
    with open('output.txt', 'w') as f:
        f.write('\n'.join([f'{i[0]} {i[1]}' for i in result]))

if __name__ == '__main__':
    func()