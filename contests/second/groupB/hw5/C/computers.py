def func():
    with open('input.txt', encoding="utf8", mode='r') as f:
        N, M = list(map(int, f.readline().strip().split()))
        groups = {i + 1: int(value) for i, value in enumerate(f.readline().strip().split())}
        rooms = {i + 1: int(value) for i, value in enumerate(f.readline().strip().split())}
    
    sortedGroups = sorted(groups.items(), key=lambda x:x[1], reverse=True)
    sortedRooms = sorted(rooms.items(), key=lambda x:x[1], reverse=True)

    i = 0
    ansCount = 0
    for group in sortedGroups:
        if i > M:
            groups[group[0]] = 0
        elif sortedRooms[i][1] - group[1] >= 1:
            groups[group[0]] = sortedRooms[i][0]
            i += 1
            ansCount += 1
        else:
            groups[group[0]] = 0

    with open('output.txt', encoding="utf8", mode='w') as f:
        f.write(f'{str(ansCount)}\n' + '\n'.join([str(room) for room in groups.values()]))

if __name__ == '__main__':
    func()