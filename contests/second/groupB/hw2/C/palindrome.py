def func():
    with open('input.txt', 'r') as f:
        string = f.readline().strip()
    
    def getCost(_string):
        result = 0
        for i in range(len(_string) // 2):
            if _string[i] != _string[len(_string) - 1 - i]:
                result += 1
        return result

    ans = getCost(string)

    with open('output.txt', 'w') as f:
        f.write(str(ans))

if __name__ == '__main__':
    func()