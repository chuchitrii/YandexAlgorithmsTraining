def func():
    with open('input.txt', 'r') as f:
        n, i, j = list(map(int, f.read().strip().split()))
    diff = abs(i-j)
    if (diff < n//2):
        ans = diff - 1
    else:
        ans = n-diff-1
    with open('output.txt', 'w') as f:
        f.write(str(ans))

if __name__ == '__main__':
    func()