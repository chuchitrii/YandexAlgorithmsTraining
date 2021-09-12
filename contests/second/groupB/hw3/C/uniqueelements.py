def func():
    with open('input.txt', 'r') as f:
        elements = {}
        for i in f.readline().strip().split():
            if i not in elements:
                elements[i] = 0
            elements[i] += 1
    
    ans = []
    for i in elements:
        if elements[i] == 1:
            ans.append(i)

    with open('output.txt', 'w') as f:
        f.write(' '.join(ans))

if __name__ == '__main__':
    func()