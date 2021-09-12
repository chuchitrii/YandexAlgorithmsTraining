def func():
    with open('input.txt', 'r') as f:
        l, k = list(map(int, f.readline().strip().split()))
        coords = list(map(int, f.readline().strip().split()))    
    median = l // 2

    if k == 1:
        ans = f'{coords[0]}'
    elif l % 2 == 0:
        if k == 2:
            ans = f'{coords[0]}'
        else:
            for i in range(len(coords)):
                if (coords[i] <= median - 1) and (coords[i + 1] >= median):
                    ans = f'{coords[i]} {coords[i + 1]}'
                    break
    else:
        try:
            if coords.index(median):
                ans = f'{median}'
        except ValueError:
            for i in range(len(coords)):
                if coords[i] < median and coords[i + 1] > median:
                    ans = f'{coords[i]} {coords[i + 1]}'
                    break
                
    with open('output.txt', 'w') as f:
        f.write(ans)

if __name__ == '__main__':
    func()