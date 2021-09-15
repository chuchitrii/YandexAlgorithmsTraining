def func():
    with open('input.txt', encoding="utf8", mode='r') as f:
        inp = f.read()
    
    outp = inp

    with open('output.txt', encoding="utf8", mode='w') as f:
        f.write(outp)

if __name__ == '__main__':
    func()