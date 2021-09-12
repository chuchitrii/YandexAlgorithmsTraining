def func():
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())
        diplomas = list(map(int, f.readline().strip().split()))
    
    if n == 0:
        ans = 0
    else:
        diplomas.remove(max(diplomas))
        ans = sum(diplomas)

    with open('output.txt', 'w') as f:
        f.write(str(ans))

if __name__ == '__main__':
    func()