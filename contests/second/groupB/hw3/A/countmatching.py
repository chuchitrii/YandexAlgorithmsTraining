def func():
    with open('input.txt', 'r') as f:
        ans = len(set(f.readline().strip().split()) & set(f.readline().strip().split()))
    
    with open('output.txt', 'w') as f:
        f.write(str(ans))

if __name__ == '__main__':
    func()