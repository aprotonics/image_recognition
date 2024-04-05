
class Iterator():
    def __init__(self, iterable_list):
        self._iterable_list = []

        if len(iterable_list) > 0:
            self._iterable_list = iterable_list
            
        self._last_index = 0

    @property
    def iterable_list(self):
        return self._iterable_list
    
    @iterable_list.getter
    def iterable_list(self):
        return self._iterable_list

    @iterable_list.setter
    def iterable_list(self, value):
        self._iterable_list = value

    @property
    def last_index(self):
        return self._last_index
    
    @last_index.getter
    def last_index(self):
        return self._last_index

    @last_index.setter
    def last_index(self, value):
        self._last_index = value

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.last_index < len(self.iterable_list):
            value_to_return = self.iterable_list[self.last_index]
            new_value = self.last_index + 1
            self.last_index = new_value
        else:
            raise Warning

        return value_to_return

    def next(self):
        return self.__next__()


def next(iterator):
    next_value = iterator.__next__()

    return next_value


iterator = Iterator("vwhbh")
list_to_send = []

for i in range(iterator.iterable_list.__len__()):
    value = next(iterator)
    list_to_send.append(value)

iterator2 = Iterator(list_to_send)


stroke_to_send = """some Tumblr primavera Crystall unknown never everyday mighty composition compromise\
                    cliche aqualung oblivion struggle"""

def filter_stroke(stroke_to_send):
    for i in range(len(stroke_to_send)):
        yield stroke_to_send[i]

character_generator = filter_stroke(stroke_to_send)

new_stroke = ""
for value in character_generator:
    new_stroke += value

print(new_stroke)
