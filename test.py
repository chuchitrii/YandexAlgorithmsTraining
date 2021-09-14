import time
import glob
import importlib
import sys
import pathlib
from math import ceil

functionName = 'func'
searchDirectory = 'contests'
doubleBacklash = '\\'
newline = '\n'
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def printCol(string: str, color: str) -> None:
    print(f'{color}{string}{bcolors.RESET}')

def getDirectoryPath(_pathToFile: str) -> str:
    return _pathToFile.rsplit('.', 1)[0].replace('.', '/')

def getFilePathForImport(_pathFromGlob: str) -> str:
    return _pathFromGlob.rsplit('.', 1)[0].replace('\\', '.')

def getFilePathForConsole(_pathFromGlob: str) -> str:
    part1, part2 = getFilePathForImport(_pathFromGlob).replace(searchDirectory + '.', '').rsplit('.', 1)
    return f'{part1}.{bcolors.OK}{part2}{bcolors.RESET}'

def indexWithIndents(i: int) -> str:
    return ' ' * (4 - len(str(i))) + str(i) + '  '

def passedString(_passed: bool):
    if _passed:
        return f'{bcolors.OK}passed{bcolors.RESET}'
    else:
        return f'{bcolors.FAIL}failed{bcolors.RESET}'

try:
    with open('test.config', encoding="utf8", mode='r') as config:
        for line in config.readlines():
            if line.startswith('functionName'):
                functionName = line.strip().rsplit(' ', 1)[1]
            if line.startswith('searchDirectory'):
                searchDirectory = line.strip().rsplit(' ', 1)[1]
except FileNotFoundError:
    print('test.config not found in directory')
    
pyFiles = glob.glob(searchDirectory + '/**/*.py', recursive=True)
if len(pyFiles) == 0:
    sys.exit(f'{bcolors.FAIL}No *.py files found in {searchDirectory}{bcolors.RESET}')

[print(f'{bcolors.OK}{indexWithIndents(i)}{bcolors.RESET}{getFilePathForConsole(file)}') for i, file in enumerate(pyFiles)]
printCol('Enter index of the file you want to test', bcolors.WARNING)

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
                printCol('Index not found in list. Enter valid index', bcolors.WARNING)
        except ValueError:
            printCol('Enter int', bcolors.WARNING)
    else:
        printCol('Enter int', bcolors.WARNING)

try:
    func = getattr(importlib.import_module(getFilePathForImport(pyFiles[currentFileIndex])), functionName)
except AttributeError:
    sys.exit(f'{bcolors.FAIL}{functionName}() not found in {pyFiles[currentFileIndex]}{bcolors.RESET}')

answers = glob.glob(getDirectoryPath(getFilePathForImport(pyFiles[currentFileIndex])) + '/*.a')
tests: list[tuple[str, str]] = []
for answer in answers:
    _question = glob.glob(answer.rsplit('.', 1)[0])
    if len(_question) > 0:
        question = _question[0]
    else:
        continue
    tests.append((question, answer))

if len(tests) > 0:
    printCol(f'Running tests for {pyFiles[currentFileIndex]}', bcolors.WARNING)
    outp = open('output.txt', encoding='utf-8', mode='w+')
    outp.close()
    inp = open('input.txt', encoding='utf-8', mode='w+')
    inp.close()
    inp = open('testerror.log', encoding='utf-8', mode='w+')
    inp.close()
    for test in tests:
        with open(test[0], encoding="utf8", mode='r') as q:
            with open('input.txt', encoding="utf8", mode='w') as inp: 
                inp.write(q.read())
        start = ceil(time.time() * 1000)
        func()
        end = ceil(time.time() * 1000)
        with open(test[1], encoding="utf8", mode='r') as a:
            with open('output.txt', encoding="utf8", mode='r') as outp: 
                rightAnswers = [ans.strip() for ans in a.read().split('---')]
                yourAnswer = outp.read().rstrip()
                passed = any(yourAnswer == rightAnswer for rightAnswer in rightAnswers)
                print(f'test {bcolors.WARNING}{test[0].rsplit(doubleBacklash, 1)[1]}{bcolors.RESET} {passedString(passed)} | time elapsed: {bcolors.OK}{end - start}{bcolors.RESET} ms')
                if not passed:
                    with open('testerror.log', encoding='utf-8', mode='a') as errorlog:
                        errorlog.write(f'test - {test[0].rsplit(doubleBacklash, 1)[1]}{newline}your answer:{newline}{newline}{yourAnswer}{newline}{newline}')
                        errorlog.write(f'expected answers:{newline}{newline}{"".join([f"{rightAnswer}{newline}{newline}" for rightAnswer in rightAnswers])}')
    pathlib.Path('input.txt').unlink()
    pathlib.Path('output.txt').unlink()
else:
    printCol(f'Test files weren\'t found in directory: {getDirectoryPath(getFilePathForImport(pyFiles[currentFileIndex]))}', bcolors.FAIL)