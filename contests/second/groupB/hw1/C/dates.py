def func():
    with open('input.txt', 'r') as f:
        x, y, z = list(map(int, f.read().strip().split()))
        
    if (x > 12 or y > 12):
        ans = 1
    elif (x == y):
        ans = 1
    else:
        ans = 0

    with open('output.txt', 'w') as f:
        f.write(str(ans))

if __name__ == '__main__':
    func()