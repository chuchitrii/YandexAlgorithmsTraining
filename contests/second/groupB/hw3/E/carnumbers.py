def func():
    with open('input.txt', 'r') as f:
        M = int(f.readline().strip())
        witnesses = [f.readline().strip() for _ in range(M)]
        N = int(f.readline().strip())
        carnumbers = [[f.readline().strip(), 0] for _ in range(N)]
    
    for witness in witnesses:
        for i in range(len(carnumbers)):
            if set(witness).issubset(set(carnumbers[i][0])):
                carnumbers[i][1] += 1
    max = 0
    maxKeys = []
    for i in range(len(carnumbers)):
        if carnumbers[i][1] > max:
            max = carnumbers[i][1]
            maxKeys = [carnumbers[i][0]]
        elif carnumbers[i][1] == max:
            maxKeys.append(carnumbers[i][0])

    with open('output.txt', 'w') as f:
        f.write('\n'.join(maxKeys))

if __name__ == '__main__':
    func()