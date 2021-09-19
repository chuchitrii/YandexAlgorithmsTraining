def func():
    with open('input.txt', encoding="utf8", mode='r') as f:
        n, q = list(map(int, f.readline().strip().split()))
        a = list(map(int, f.readline().strip().split()))
        p = [0] * (n + 1)
        for i in range(1, n + 1):
            p[i] = p[i - 1] + a[i - 1]

        ans = []
        for _ in range(q):
            start, end = list(map(int, f.readline().strip().split()))
            ans.append(p[end] - p[start - 1])
    
    with open('output.txt', encoding="utf8", mode='w') as f:
        f.write('\n'.join([str(answer) for answer in ans]))

if __name__ == '__main__':
    func()