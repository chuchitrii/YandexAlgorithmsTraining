def func():
    with open('input.txt', 'r') as f:
        input = f.read()
    
    output = input

    with open('output.txt', 'w') as f:
        f.write(output)

if __name__ == '__main__':
    func()