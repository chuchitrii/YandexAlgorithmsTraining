def func():
    with open('input.txt', encoding="utf8", mode='r') as f:
        n = int(f.readline().strip())
        a = list(map(int, f.readline().strip().split()))

    sum = ans = a[0]
    for i in range(1, n):
        if sum <= 0 and a[i] > 0:
            sum = a[i]
            if sum > ans:
                ans = sum
        elif sum <=0 and a[i] <= 0:
            if a[i] > sum:
                sum = ans = a[i]
        elif sum > 0 and a[i] < 0:
            if sum + a[i] < 0:
                if sum > ans: 
                    ans = sum
                sum = 0
            if sum + a[i] >= 0:
                if sum > ans: 
                    ans = sum
                sum += a[i]
        elif sum > 0 and a[i] >= 0:
            sum += a[i]
    if sum > ans:
        ans = sum

    with open('output.txt', encoding="utf8", mode='w') as f:
        f.write(str(ans))

if __name__ == '__main__':
    func()