import math


def get_minimum(*values):
    values = values
    
    minimum = None
    value = values[0]
    
    if isinstance(value, type(1)) and len(values) == 2:
        minimum = get_minimum1(values)
    
    if isinstance(value, type(1)) and len(values) > 2:
        minimum = get_minimum2(*values)
    
    if isinstance(value, type([])):
        minimum = get_minimum3(values)

    return minimum

def get_minimum1(values):
    (value1, value2) = values

    if value1 < value2:
        minimum = value1
    else:
        minimum = value2

    return minimum

def get_minimum2(*values):
    values = values

    minimum = math.inf

    for value in values:
        if value < minimum:
            minimum = value

    return minimum

def get_minimum3(iterable):
    values = iterable[0]

    minimum = math.inf

    for value in values:
        if value < minimum:
            minimum = value

    return minimum


def get_nth_minimums(values, number_of_values):
    values = values
    number_of_values = number_of_values
    n = number_of_values

    minimum = math.inf
    minimums = []
    values_copy = values.copy()

    for value in values_copy:
        if value <= minimum:
            minimum = value
    
    values_copy.remove(minimum)
    minimums.append(minimum)
    minimum = math.inf
    n -= 1

    while n >= 1:
        for value in values_copy:
            if value <= minimum:
                minimum = value
        
        values_copy.remove(minimum)
        minimums.append(minimum)
        minimum = math.inf
        n -= 1

    return minimums
