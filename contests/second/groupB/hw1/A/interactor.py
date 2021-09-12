def func():
    with open('input.txt', 'r') as f:
        r = int(f.readline().strip())
        i = int(f.readline().strip())
        c = int(f.readline().strip())
    ans = i
    if i == 0:
        if r != 0:
            ans = 3
        else:
            ans = c
    elif i == 1:
        ans = c
    elif i == 4:
        if r != 0:
            ans = 3
        else:
            ans = 4
    elif i == 6:
        ans = 0
    elif i == 7:
        ans = 1
    with open('output.txt', 'w') as f:
        f.write(str(ans))

if __name__ == '__main__':
    func()