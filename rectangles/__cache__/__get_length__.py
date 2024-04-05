
def length(obj):
    length = get_length(obj)
    return length

def get_length(obj):
    obj = obj

    length = obj.__len__()

    return length
