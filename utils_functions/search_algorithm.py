
def filter_stroke(stroke_to_send):
    for i in range(len(stroke_to_send)):
        yield stroke_to_send[i]

stroke_to_send = """some Tumblr primavera Crystall unknown never everyday mighty composition compromise cliche aqualung oblivion struggle"""





character_generator = filter_stroke(stroke_to_send)

symbols_count = 0
words_count = 0
for value in character_generator:
    value

    if value == " ":
        words_count += 1
    else:
        symbols_count += 1

words_count += 1

print(symbols_count)
print(words_count)
print()





input_stroke = "gh"
input_stroke_length = len(input_stroke)

character_generator = filter_stroke(stroke_to_send)

count_index = 0
count_value = 0
for value in character_generator:
    for i in range(count_value, len(input_stroke)):
        input_stroke_value = input_stroke[i]
        if str(value) == str(input_stroke_value):
            count_value += 1
            break
        else:
            count_value = 0
            break

    if count_value == input_stroke_length:
        break
    
    count_index += 1

if count_index == len(stroke_to_send):
    count_index = 0

input_stroke_index = count_index - input_stroke_length + 1
print(input_stroke_index)
print()
