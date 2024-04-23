import cv2


morse_to_letters = {
    ".-":   "A",
    "-...": "B",
    "-.-.": "C",
    "-..":  "D", 
    ".":    "E", 
    "..-.": "F",
    "--.":  "G",
    "....": "H",
    "..":   "I", 
    ".---": "J",
    "-.-":  "K",
    ".-..": "L",
    "--":   "M",
    "-.":   "N",
    "---":  "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.":  "R",
    "...":  "S",
    "-":    "T", 
    "..-":  "U", 
    "...-": "V", 
    ".--":  "W", 
    "-..-": "X", 
    "-.--": "Y", 
    "--..": "Z"
}

letters = []
recognized_strokes = []
recognized_symbols = []

img_name = "new_img.jpg"
img = cv2.imread(img_name)

# img = [[[255, 255, 255], ..., [255, 255, 255]], ..., [[255, 255, 255], ..., [255, 255, 255]]]

print(img.shape)
print(type(img))
print(img.dtype)

basic_indent = 12                   # px
vertical_indent = basic_indent      # px
horizontal_indent = basic_indent    # px
length_between_symbols = 2          # px
length_between_strokes = 6          # px
quality = 90                        # %

### recognize strokes of letters from symbol to symbol with cv2

def check_if_symbol_is_point(img, vertical_indent, horizontal_indent):
    comparable_array = img[vertical_indent:vertical_indent+2, horizontal_indent:horizontal_indent+2]
    symbol_is_point = True

    for i in range(len(comparable_array)):
        for j in range(len(comparable_array[0])):
            
            # refactoring
            # b, g, r = comparable_array[i][j]
            # if r >= 100 - quality or g >= 100 - quality or b >= 100 - quality:
            #     symbol_is_point = False
            #     break

            for g in range(len(comparable_array[0][0])):
                if comparable_array[i][j][g] >= 10:
                    symbol_is_point = False
                    break

            if symbol_is_point == False:
                break
        
        if symbol_is_point == False:
            break
    
    return symbol_is_point

def check_if_symbol_is_dash(img, vertical_indent, horizontal_indent):
    comparable_array = img[vertical_indent:vertical_indent+2, horizontal_indent:horizontal_indent+6]
    symbol_is_dash = True

    for i in range(len(comparable_array)):
        for j in range(len(comparable_array[0])):
            for g in range(len(comparable_array[0][0])):
                if comparable_array[i][j][g] >= 10:
                    symbol_is_dash = False
                    break

            if symbol_is_dash == False:
                break
        
        if symbol_is_dash == False:
            break
    
    return symbol_is_dash

def check_if_symbol_is_empty(img, vertical_indent, horizontal_indent, quality):
    symbol_is_empty = True

    if img[vertical_indent, horizontal_indent, 0] < 100 - quality and\
        img[vertical_indent, horizontal_indent, 1] < 100 - quality and\
        img[vertical_indent, horizontal_indent, 2] < 100 - quality:
        symbol_is_empty = False

    return symbol_is_empty

# check if image is empty
img_is_empty = check_if_symbol_is_empty(img, vertical_indent, horizontal_indent, quality)

if img_is_empty:
    print("Image is empty")

# first stroke
# check if first symbol is point
if not img_is_empty:
    symbol_is_point = check_if_symbol_is_point(img, vertical_indent, horizontal_indent)

# check if first symbol is dash
if symbol_is_point:
    symbol_is_dash = check_if_symbol_is_dash(img, vertical_indent, horizontal_indent)

if symbol_is_dash:
    horizontal_indent += 6
    recognized_symbols.append("-")
elif symbol_is_point:
    horizontal_indent += 2
    recognized_symbols.append(".")

horizontal_indent += length_between_symbols

# checking other symbols
end_of_cycle = int((img.shape[1] - basic_indent * 2) / 4)
for i in range(0, end_of_cycle):

    # check if symbol is empty
    symbol_is_empty = check_if_symbol_is_empty(img, vertical_indent, horizontal_indent, quality)

    if symbol_is_empty:
        break

    # check if symbol is point
    if not symbol_is_empty:
        symbol_is_point = check_if_symbol_is_point(img, vertical_indent, horizontal_indent)

    # check if symbol is dash
    if symbol_is_point:
        symbol_is_dash = check_if_symbol_is_dash(img, vertical_indent, horizontal_indent)

    if symbol_is_dash:
        horizontal_indent += 6
        recognized_symbols.append("-")
    elif symbol_is_point:
        horizontal_indent += 2
        recognized_symbols.append(".")

    horizontal_indent += length_between_symbols

vertical_indent += 2
recognized_strokes.append(recognized_symbols)
print(recognized_symbols)
print(len(recognized_symbols))
print()

# other strokes
end_of_cycle = 3
for i in range(0, end_of_cycle):
    recognized_symbols = []
    horizontal_indent = basic_indent
    vertical_indent += length_between_strokes

    # checking if stroke is empty
    stroke_is_empty = check_if_symbol_is_empty(img, vertical_indent, horizontal_indent, quality)
    
    if stroke_is_empty:
        print("Stroke is empty")
        break

    # check if first symbol is point
    if not stroke_is_empty:
        symbol_is_point = check_if_symbol_is_point(img, vertical_indent, horizontal_indent)

    # check if first symbol is dash
    if symbol_is_point:
        symbol_is_dash = check_if_symbol_is_dash(img, vertical_indent, horizontal_indent)

    if symbol_is_dash:
        horizontal_indent += 6
        recognized_symbols.append("-")
    elif symbol_is_point:
        horizontal_indent += 2
        recognized_symbols.append(".")

    horizontal_indent += length_between_symbols

    # checking other symbols
    end_of_cycle = int((img.shape[1] - basic_indent * 2) / 4)
    for i in range(0, end_of_cycle):

        # check if symbol is empty
        symbol_is_empty = check_if_symbol_is_empty(img, vertical_indent, horizontal_indent, quality)
        
        if symbol_is_empty:
            break

        # check if symbol is point
        if not symbol_is_empty:
            symbol_is_point = check_if_symbol_is_point(img, vertical_indent, horizontal_indent)

        # check if symbol is dash
        if symbol_is_point:
            symbol_is_dash = check_if_symbol_is_dash(img, vertical_indent, horizontal_indent)

        if symbol_is_dash:
            horizontal_indent += 6
            recognized_symbols.append("-")
        elif symbol_is_point:
            horizontal_indent += 2
            recognized_symbols.append(".")

        horizontal_indent += length_between_symbols

    vertical_indent += 2    
    recognized_strokes.append(recognized_symbols)
    print(recognized_symbols)
    print(len(recognized_symbols))
    print()

print(recognized_strokes)
print(len(recognized_strokes))
