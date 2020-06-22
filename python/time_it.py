"""
Using timeit snippet
Ref:https://stackoverflow.com/questions/5086430/how-to-pass-parameters-of-a-function-when-using-timeit-timer
"""
import timeit


def func(x):
    n = [i for i in range(x)]
    print(n)


# Take note on how parameters are defined and passed to timeit.Timer
t = timeit.Timer("func(5)", "from time_it import func")
print(t.timeit(1))
