def func():
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        coords = list(map(int, f.readline().strip().split()))

    if n > 0:
        i = n // 2
        if n % 2 == 0:
            ans = (int(coords[i - 1]) + int(coords[i])) // 2
        else:
            ans = coords[i]
    else:
        ans = 0

    with open('output.txt', 'w') as f:
        f.write(str(ans))

if __name__ == '__main__':
    func()