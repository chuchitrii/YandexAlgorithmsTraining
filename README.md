Repository with my solutions of the problems from Yandex Algorithm Training

I'm testing my solutions using [test.py](test.py) in the root directory.   Script is cofigurable using [config.json](config.json):

```python 
searchDirectory ## directory which will be scanned recursively for .py files
functionName ## function that will be imported from .py file
answerSeparator ## string that separates multiple answer in one file
```

[template.py](template.py) contains boilerplate for reading and writing to file
```python
def func():
    with open('input.txt', encoding="utf8", mode='r') as f:
        inp = f.read()
    
    outp = inp

    with open('output.txt', encoding="utf8", mode='w') as f:
        f.write(outp)

if __name__ == '__main__':
    func()
```

Type `python test.py` in console to start script, and choose one of files it will suggest.  
Script will run all test files from solution file directory. Names of input and output test files should match this pattern:  
`<name>` - input  
`<name>.a` - output  

If some of tests will fail log will be saved to `failedtests` file
