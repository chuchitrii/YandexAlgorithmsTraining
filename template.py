def func():
    with open('input.txt', encoding="utf8", mode='r') as f:
        input = f.read()
    
    output = input

    with open('output.txt', encoding="utf8", mode='w') as f:
        f.write(output)

if __name__ == '__main__':
    func()