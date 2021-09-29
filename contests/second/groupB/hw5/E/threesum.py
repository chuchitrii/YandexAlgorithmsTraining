def func():
    with open('input.txt', encoding="utf8", mode='r') as f:
        s = int(f.readline().strip())
        a = list(map(int, f.readline().strip().split()[1::]))
        b = list(map(int, f.readline().strip().split()[1::]))
        c = list(map(int, f.readline().strip().split()[1::]))

    ab_complement = {}
    for i in range(len(c)):
        complement = s - c[i]
        if complement not in ab_complement:
            ab_complement[s - c[i]] = i
    
    def doubleLoop():
        for j in range(len(a)):
            for k in range(len(b)):
                sum = a[j] + b[k]
                if sum in ab_complement:
                    return f'{j} {k} {ab_complement[a[j] + b[k]]}'
        return '-1'

    ans = doubleLoop()

    with open('output.txt', encoding="utf8", mode='w') as f:
        f.write(ans)

if __name__ == '__main__':
    func()