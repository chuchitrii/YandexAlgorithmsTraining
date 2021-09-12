def func():
    with open('input.txt', 'r') as f:
        N = int(f.readline().strip())
        resultSet = set(range(1, N + 1, 1))
        help = False
        while not help:
            question = f.readline().strip()
            if question == 'HELP':
                help = True
                continue
            question = set(list(map(int, question.strip().split())))
            answer = f.readline().strip()
            if answer == 'YES':
                resultSet &= question
            else:
                resultSet -= question    
        
    resultSet = list(resultSet)
    resultSet.sort()

    with open('output.txt', 'w') as f:
        f.write(' '.join([str(i) for i in resultSet]))

if __name__ == '__main__':
    func()