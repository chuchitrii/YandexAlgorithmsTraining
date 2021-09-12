def func():
    board = []
    with open('input.txt', 'r') as f:
        for i in range(3):
            board.extend(f.readline().strip().split())
    
    win_lines = [
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 4, 8],
        [2, 4, 6]
        ]
    def calcWinLines(type):
        count = 0
        for w in win_lines:
            if board[w[0]] == type and board[w[1]] == type and board[w[2]] == type:
                count += 1
        return count

    count1 = 0
    count2 = 0
    for i in board:
        if i == '1':
            count1 += 1
        elif i == '2':
            count2 += 1

    win1 = calcWinLines('1')
    win2 = calcWinLines('2')
    if abs(count1 - count2) > 1 or (count2 > 0 and count1 == 0) or count2 > 4 or win1 > 2 or (win1 == 2 and count2 != 4) or win2 > 1 or (win1 > 0 and win2 > 0) or (win1 == 1 and count2 >= count1) or (win2 == 1 and count2 != count1):
        ans = 'NO'
    else:
        ans = 'YES'
    
    with open('output.txt', 'w') as f:
        f.write(ans)

if __name__ == '__main__':
    func()