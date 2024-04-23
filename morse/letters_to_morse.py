import numpy
import cv2


letters_to_morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
}

letters = []
morse_array = []


class Point():
    def init(self):
        pass
    
    def create(self):
        pass


class Dash():
    def init(self):
        pass

    def create(self):
        pass


stroke = "PP"

for i in range(len(stroke)):
    letters.append(stroke[i])
morse_stroke = ""
for i in range(len(letters)):
    morse_stroke += letters_to_morse[letters[i]]
for i in range(len(morse_stroke)):
    morse_array.append(morse_stroke[i])

# create img array
img_array = [[[255 for i in range(3)] for i in range(100)] for i in range(100)]

template_array =    [   [   [255, 255, 255],
                            [255, 255, 255],
                            [255, 255, 255],
                            [255, 255, 255],
                            [255, 255, 255],
                            [255, 255, 255],
                        ],
                        [   [255, 255, 255],
                            [255, 255, 255],
                            [255, 255, 255],
                            [255, 255, 255],
                            [255, 255, 255],
                            [255, 255, 255],
                        ],
                        [   [255, 255, 255],
                            [255, 255, 255],
                            [255, 255, 255],
                            [255, 255, 255],
                            [255, 255, 255],
                            [255, 255, 255],
                        ],
                    ]

img2 = numpy.array(img_array, dtype=numpy.uint8)

print(img2.shape)
print(type(img2))
print(img2.dtype)

vertical_indent = 12
horizontal_indent = 12

# create first symbol
if morse_array[0] == ".":
    for i in range(vertical_indent, vertical_indent+2):
        for j in range(horizontal_indent, horizontal_indent+2):
            img2[i, j] = [0, 0, 0]
    horizontal_indent += 2
elif morse_array[0] == "-":
    for i in range(vertical_indent, vertical_indent+2):
        for j in range(horizontal_indent, horizontal_indent+6):
            img2[i, j] = [0, 0, 0]
    horizontal_indent += 6

horizontal_indent += 2

# create other symbols
for i in range(1, len(morse_array)):
    if morse_array[i] == ".":
        for i in range(vertical_indent, vertical_indent+2):
            for j in range(horizontal_indent, horizontal_indent+2):
                img2[i, j] = [0, 0, 0]
        horizontal_indent += 2
    elif morse_array[i] == "-":
        for i in range(vertical_indent, vertical_indent+2):
            for j in range(horizontal_indent, horizontal_indent+6):
                img2[i, j] = [0, 0, 0]
        horizontal_indent += 6

    horizontal_indent += 2

cv2.imwrite("letters_to_morse.jpg", img2)
