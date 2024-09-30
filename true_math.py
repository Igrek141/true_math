import math
from math import inf
def divide2(first, second):
    try:
        res = first / second
        if second != 0:
            return res
    except ZeroDivisionError:
        return inf