import time
import glob
import importlib
import sys
import pathlib
from math import ceil

functionName = 'func'
searchDirectory = 'contests'
answerSeparator = '---'
doubleBacklash = '\\'
newline = '\n'
class colors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def printCol(string: str, color: str) -> None:
    print(f'{color}{string}{colors.RESET}')

def getDirectoryPath(_pathToFile: str) -> str:
    return _pathToFile.rsplit('.', 1)[0].replace('.', '/')

def getFilePathForImport(_pathFromGlob: str) -> str:
    return _pathFromGlob.rsplit('.', 1)[0].replace('\\', '.')

def getFilePathForConsole(_pathFromGlob: str) -> str:
    part1, part2 = getFilePathForImport(_pathFromGlob).replace(searchDirectory + '.', '').rsplit('.', 1)
    return f'{part1}.{colors.OK}{part2}{colors.RESET}'

def indexWithIndents(i: int) -> str:
    return ' ' * (4 - len(str(i))) + str(i) + '  '

def passedString(_passed: bool):
    if _passed:
        return f'{colors.OK}passed{colors.RESET}'
    else:
        return f'{colors.FAIL}failed{colors.RESET}'

def initFilesForTests():
    for filename in ['input.txt', 'output.txt', 'testerror.log']:
        file = open(filename, encoding='utf-8', mode='w+')
        file.close()

try:
    with open('test.config', encoding="utf8", mode='r') as config:
        for line in config.readlines():
            if line.startswith('functionName'):
                functionName = line.strip().rsplit(' ', 1)[1]
            if line.startswith('searchDirectory'):
                searchDirectory = line.strip().rsplit(' ', 1)[1]
            if line.startswith('answerSeparator'):
                answerSeparator = line.strip().rsplit(' ', 1)[1]
except FileNotFoundError:
    print('test.config not found in directory')
    
pyFiles = glob.glob(searchDirectory + '/**/*.py', recursive=True)
if len(pyFiles) == 0:
    sys.exit(f'{colors.FAIL}No *.py files found in {searchDirectory}{colors.RESET}')
[print(f'{colors.OK}{indexWithIndents(i)}{colors.RESET}{getFilePathForConsole(file)}') for i, file in enumerate(pyFiles)]
printCol('Enter index of the file you want to test', colors.WARNING)

currentFileIndex = None
while type(currentFileIndex) is not int:
    _currentFileIndex = input().strip()
    if len(_currentFileIndex) > 0:
        try:
            _currentFileIndex = int(_currentFileIndex)
            try:
                pyFiles[_currentFileIndex]
                currentFileIndex = _currentFileIndex
            except IndexError:
                printCol('Index not found in list. Enter valid index', colors.WARNING)
        except ValueError:
            printCol('Enter int', colors.WARNING)
    else:
        printCol('Enter int', colors.WARNING)

filePathForImport = getFilePathForImport(pyFiles[currentFileIndex])
directoryPath = getDirectoryPath(filePathForImport)

try:
    func = getattr(importlib.import_module(filePathForImport), functionName)
except AttributeError:
    sys.exit(f'{colors.FAIL}{functionName}() not found in {pyFiles[currentFileIndex]}{colors.RESET}')

answers = glob.glob(directoryPath + '/*.a')
tests: list[tuple[str, str]] = []
for answer in answers:
    _question = glob.glob(answer.rsplit('.', 1)[0])
    if len(_question) > 0:
        question = _question[0]
    else:
        continue
    tests.append((question, answer))

if len(tests) == 0:
    sys.exit(f'{colors.FAIL}Test files weren\'t found in directory: {directoryPath}{colors.RESET}')

printCol(f'Running tests for {pyFiles[currentFileIndex]}', colors.WARNING)
initFilesForTests()
for test in tests:
    with open(test[0], encoding="utf8", mode='r') as q:
        with open('input.txt', encoding="utf8", mode='w') as inp: 
            inp.write(q.read())
    start = ceil(time.time() * 1000)
    func()
    end = ceil(time.time() * 1000)
    with open(test[1], encoding="utf8", mode='r') as answers:
        with open('output.txt', encoding="utf8", mode='r') as outp: 
            rightAnswers = [ans.strip() for ans in answers.read().split(answerSeparator)]
            yourAnswer = outp.read().rstrip()
    passed = any(yourAnswer == rightAnswer for rightAnswer in rightAnswers)
    print(f'test {colors.WARNING}{test[0].rsplit(doubleBacklash, 1)[1]}{colors.RESET} {passedString(passed)} | time elapsed: {colors.OK}{end - start}{colors.RESET} ms')
    if not passed:
        with open('testerror.log', encoding='utf-8', mode='a') as errorlog:
            errorlog.write(f'test - {test[0].rsplit(doubleBacklash, 1)[1]}{newline}your answer:{newline}{newline}{yourAnswer}{newline}{newline}')
            errorlog.write(f'expected answers:{newline}{newline}{"".join([f"{rightAnswer}{newline}{newline}" for rightAnswer in rightAnswers])}')

pathlib.Path('input.txt').unlink()
pathlib.Path('output.txt').unlink()