def func():
    with open('input.txt', encoding="utf8", mode='r') as f:
        string = f.readline().strip()

    balance = 0
    for char in string:
        if char == '(': balance += 1
        else: balance -= 1
        if balance < 0: break

    with open('output.txt', encoding="utf8", mode='w') as f:
        f.write('YES' if balance == 0 else 'NO')

if __name__ == '__main__':
    func()