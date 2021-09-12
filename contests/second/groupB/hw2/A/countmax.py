def func():
    maxValue = 0
    maxValueCount = 0
    lastValue = 0
    with open('input.txt', 'r') as f:
        while True:
            lastValue = int(f.readline())
            if lastValue == 0:
                break
            elif lastValue > maxValue:
                maxValue = lastValue
                maxValueCount = 1 
            elif lastValue == maxValue:
                maxValueCount += 1

    with open('output.txt', 'w') as f:
        f.write(str(maxValueCount))

if __name__ == '__main__':
    func()