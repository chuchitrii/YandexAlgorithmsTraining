def func():
    colorSum = {}
    with open('input.txt', 'r') as f:
        N = int(f.readline().strip())
        for i in range(N):
            [color, number] = list(map(int, f.readline().strip().strip().split()))
            if color not in colorSum: 
                colorSum[color] = 0
            colorSum[color] += number
    
    with open('output.txt', 'w') as f:
        f.write('\n'.join([f'{c} {n}' for c, n in sorted(colorSum.items())]))

if __name__ == '__main__':
    func()