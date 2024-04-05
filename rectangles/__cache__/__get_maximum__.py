import math


def get_maximum(*values):
    values = values
    
    maximum = None
    value = values[0]
    
    if isinstance(value, type(1)) and len(values) == 2:
        maximum = get_maximum1(values)
    
    if isinstance(value, type(1)) and len(values) > 2:
        maximum = get_maximum2(*values)
    
    if isinstance(value, type([])):
        maximum = get_maximum3(values)

    return maximum

def get_maximum1(values):
    (value1, value2) = values

    if value1 > value2:
        maximum = value1
    else:
        maximum = value2

    return maximum

def get_maximum2(*values):
    values = values

    maximum = math.inf * -1

    for value in values:
        if value > maximum:
            maximum = value

    return maximum

def get_maximum3(iterable):
    values = iterable

    maximum = math.inf * -1

    for value in values:
        if value > maximum:
            maximum = value

    return maximum


def get_nth_maximums(values, number_of_values):
    values = values
    number_of_values = number_of_values
    n = number_of_values

    maximum = -1 * math.inf
    maximums = []
    values_copy = values.copy()

    for value in values_copy:
        if value >= maximum:
            maximum = value
    
    values_copy.remove(maximum)
    maximums.append(maximum)
    maximum = -1 * math.inf
    n -= 1

    while n >= 1:
        for value in values_copy:
            if value >= maximum:
                maximum = value
        
        values_copy.remove(maximum)
        maximums.append(maximum)
        maximum = -1 * math.inf
        n -= 1

    return maximums
