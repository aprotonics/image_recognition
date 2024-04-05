
def console_log(*value, sep=None, end=None):
    value = value
    sep = sep
    end = end
    
    if len(value) == 0:
        value = ""
        print(value, sep=sep, end=end)
        return

    value = value[0]

    if isinstance(value, type({}.keys())):
        values = value
        values_list = []
        for value in values:
            values_list.append(value)
        value = values_list

    if isinstance(value, type({}.values())):
        values = value
        values_list = []
        for value in values:
            values_list.append(value)
        value = values_list

    if isinstance(value, type({}.items())):
        items = value
        items_list = []
        for key, value in items:
            item = (key, value)
            items_list.append(item)
        value = items_list

    print(value, sep=sep, end=end)
    return
