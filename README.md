# Script-Timer

A module for calculating function and script execution time for python.

The module has two main components (`timer` and `scriptTime`).

`timer` is a function decorator that prints the execution time of a function. 

`scriptTime` is a class that should be initialized at the beginning of 'main' and `scriptTime.end()` is called at the end of 'main' to print the execution time of the whole script. `__file__` needs to be passed to the instance in order to get the script's filename. 

Example Script:
```python
# test.py
from script_timer import timer, scriptTime

@timer
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result 

if __name__ == '__main__':
    scriptTime = scriptTime(__file__)

    factorial(50_000)
    factorial(40_000)

    scriptTime.end()
```

Output:
```
factorial executed in 0.523 Seconds.
factorial executed in 0.408 Seconds.
test.py executed in 0.931 Seconds. 
```