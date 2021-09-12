def func():
    with open('input.txt', 'r') as f:
        seen_before = set()
        ans = []
        for i in f.readline().strip().split():
            if i in seen_before:
                ans.append('YES')
            else:
                seen_before.add(i)
                ans.append('NO')
    
    with open('output.txt', 'w') as f:
        f.write('\n'.join(ans))

if __name__ == '__main__':
    func()