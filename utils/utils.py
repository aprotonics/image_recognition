import math
import itertools
import numpy
from sympy import print_ccode


class Queue:
    def __init__(self):
        self.elements = []
    
    def length(self):
        return self.elements.__len__()

    def empty(self):
        return self.elements.__len__() == 0
    
    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.pop(0)


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def length(self):
        return self.elements.__len__()
    
    def empty(self):
        return self.elements.__len__() == 0

    def put(self, x, priority):
        self.elements.append((x, priority))
    
    def get(self):
        min_priority = 10000

        if self.length() > 0:
            min_priority = self.elements[0][1]

        for i in range(len(self.elements)):
            if self.elements[i][1] < min_priority:
                min_priority = self.elements[i][1]

        for i in range(len(self.elements)):
            if self.elements[i][1] == min_priority:
                value = self.elements[i][0]
                self.elements.remove((value, min_priority))
                return value


class SimpleGraph:
    def __init__(self):
        self.edges = {

        }

        self.vertices = []
    
    def nears(self, id):
        return self.edges[id]

    def nears2(self, id):
        point = id
        
        nears2 = [
                    (point[0]+1, point[1]), 
                    (point[0], point[1]+1), 
                    (point[0]-1, point[1]), 
                    (point[0], point[1]-1), 
                    (point[0]+1, point[1]+1), 
                    (point[0]-1, point[1]-1), 
                    (point[0]+1, point[1]-1), 
                    (point[0]-1, point[1]+1),
                    ]

        return nears2
    
    def nears3(self, id):
        point = id
        
        nears3 = [
                    (point[0]+1, point[1]), 
                    (point[0], point[1]+1), 
                    (point[0]-1, point[1]), 
                    (point[0], point[1]-1), 
                    (point[0]+1, point[1]+1), 
                    (point[0]-1, point[1]-1), 
                    (point[0]+1, point[1]-1), 
                    (point[0]-1, point[1]+1),
                    
                    (point[0]+2, point[1]),
                    (point[0], point[1]+2), 
                    (point[0]-2, point[1]), 
                    (point[0], point[1]-2), 
                    (point[0]+2, point[1]+2), 
                    (point[0]-2, point[1]-2), 
                    (point[0]+2, point[1]-2), 
                    (point[0]-2, point[1]+2),
                    (point[0]+1, point[1]+2),
                    (point[0]+2, point[1]+1),
                    (point[0]-1, point[1]-2),
                    (point[0]-2, point[1]-1),
                    (point[0]+1, point[1]-2),
                    (point[0]+2, point[1]-1),
                    (point[0]-1, point[1]+2),
                    (point[0]-2, point[1]+1),
                    ]

        return nears3
    
    def degree(self, id):
        edges = self.nears(id)
        degree = 0
        for key in edges.keys():
            degree += 1
        return degree
    
    def order(self):
        return len(self.vertices)


class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.triangles = []
    
    def in_triangles_area(self, id):
        (x, y) = id
        
        return (x, y) in self.triangles

    def in_bounds(self, id):
        (x, y) = id

        return 0 <= x < self.width and 0 <= y < self.height
    
    def nears(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        results = filter(self.in_bounds, results)

        return results


def breadth_first_search2(graph, start, img, quality):
    graph = graph
    start = start
    img = img
    quality = quality

    graph_area = []
    frontier = Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True
    
    while not frontier.empty():
        current = frontier.get()

        (x, y) = current
        if check_not_in_bounds((y, x), img):
            if img[y, x, 0] < 100 - quality and\
                img[y, x, 1] < 100 - quality and\
                img[y, x, 2] < 100 - quality:
                graph_area.append(current)

        for next in graph.nears(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = True
    
    return graph_area


def get_coordinates_from_output(file_names):
    file_names = file_names
    
    output = None
    outputs = [output for i in range(len(file_names))]

    for i in range(len(file_names)):
        file_name = file_names[i]
        with open(file=file_name, mode="rt", encoding="utf-8") as f:
            file_text = f.read()
            
            file_strokes = file_text.split("\n")

            coordinates1 = file_strokes[1][(file_strokes[1].index("[(")+2):file_strokes[1].index(")]")].split("), (")
            coordinates2 = file_strokes[2][(file_strokes[2].index("[(")+2):file_strokes[2].index(")]")].split("), (")

            coordinates1_copy = []
            coordinates2_copy = []

            for value in coordinates1:

                coordinates = value.split(", ")
                coordinates_copy = []

                for coordinate in coordinates:
                    coordinate = int(coordinate)
                    coordinates_copy.append(coordinate)
                
                coordinates_copy = tuple(coordinates_copy)
                coordinates1_copy.append(coordinates_copy)
            
            for value in coordinates2:
                
                coordinates = value.split(", ")
                coordinates_copy = []

                for coordinate in coordinates:
                    coordinate = int(coordinate)
                    coordinates_copy.append(coordinate)
                
                coordinates_copy = tuple(coordinates_copy)
                coordinates2_copy.append(coordinates_copy)
            
            angles_coordinates = [coordinates1_copy, coordinates2_copy]

            outputs[i] = angles_coordinates

    return outputs


def are_near_points(start1, start2, search_radius):
    start1 = start1
    start2 = start2
    search_radius = search_radius

    (x1, y1) = start1
    (x2, y2) = start2
    distance = math.sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)
    
    return 0 < distance <= search_radius


def check_not_in_bounds(coordinates, img):
    (y, x) = coordinates
    width = img.shape[0]
    height = img.shape[1]

    return 0 < y < width and 0 < x < height


def check_similarity_of_complete_graphs(graph1, graph2):
    graph1 = graph1
    graph2 = graph2

    are_similar = True
    koeffs = []
    quad_diff = 0.1

    sides_length1 = graph1.sides_length
    sides_length2 = graph2.sides_length

    if abs(len(sides_length1) - len(sides_length2)) > 0:
        are_similar = False
        return are_similar

    sides_length1.sort()
    sides_length2.sort()

    number_of_sides = len(sides_length1)
    for i in range(number_of_sides):
        sides_length1[i]
        sides_length2[i]
        koeff = round(sides_length1[i] / sides_length2[i], 3)
        koeffs.append(koeff)

    for i in range(1, len(koeffs)):
        if abs(koeffs[i] - koeffs[i-1]) > quad_diff:
            are_similar = False
            return are_similar

    return are_similar


def check_similarity_of_complete_graphs2(sides_length1, sides_length2):
    sides_length1 = sides_length1
    sides_length2 = sides_length2

    are_similar = True
    koeffs = []
    quad_diff = 0.1

    if abs(len(sides_length1) - len(sides_length2)) > 0:
        are_similar = False
        return are_similar

    sides_length1.sort()
    sides_length2.sort()

    number_of_sides = len(sides_length1)
    for i in range(number_of_sides):
        sides_length1[i]
        sides_length2[i]
        koeff = round(sides_length1[i] / sides_length2[i], 3)
        koeffs.append(koeff)

    for i in range(1, len(koeffs)):
        if abs(koeffs[i] - koeffs[i-1]) > quad_diff:
            are_similar = False
            return are_similar

    return are_similar


def check_similarity_of_rectangles(graph1, graph2):
    graph1 = graph1
    graph2 = graph2

    are_similar = None
    koeff1 = round(graph1.sides_length[0] / graph2.sides_length[0], 2)
    koeff2 = round(graph1.sides_length[1] / graph2.sides_length[1], 2)
    koeff3 = round(graph1.sides_length[2] / graph2.sides_length[2], 2)
    koeff4 = round(graph1.sides_length[3] / graph2.sides_length[3], 2)

    if koeff1 == koeff2 == koeff3 == koeff4:
        are_similar = True
    else:
        are_similar = False


def check_similarity_of_triangles(graph1, graph2):
    graph1 = graph1
    graph2 = graph2
    
    are_similar = None
    koeff1 = round(graph1.sides_length[0] / graph2.sides_length[0], 2)
    koeff2 = round(graph1.sides_length[1] / graph2.sides_length[1], 2)
    koeff3 = round(graph1.sides_length[2] / graph2.sides_length[2], 2)

    if koeff1 == koeff2 == koeff3:
        are_similar = True
    else:
        are_similar = False


def compare_rectangle_to_letter_dict(sides_length, letters_to_letters):
    sides_length = sides_length
    letters_to_letters = letters_to_letters

    result = []

    for key in letters_to_letters.keys():
        if rectangle_to_letter_comparisons(sides_length, letters_to_letters[key]):
            result.append(key)
        else:
            result.append("")

    return result


async def compare_rectangle_to_letter_dict_async(sides_length, letters_to_letters, graph_number):
    print(graph_number)
    
    sides_length = sides_length
    letters_to_letters = letters_to_letters
    graph_number = graph_number

    result = []

    for key in letters_to_letters.keys():
        if rectangle_to_letter_comparisons(sides_length, letters_to_letters[key]):
            result.append(key)
        else:
            result.append("")

    return result


def count_length_of_sides(angles_coordinates):
    angles_coordinates = angles_coordinates
    sides_length = []

    for i in range(len(angles_coordinates)):
        sides_length1 = count_length_of_sides_of_complete_graph(angles_coordinates[i])
        sides_length.append(sides_length1)

    return sides_length


async def count_length_of_sides_async(angles_coordinates, graph_number):
    print(graph_number)
    
    angles_coordinates = angles_coordinates
    graph_number = graph_number

    sides_length = []

    for i in range(len(angles_coordinates)):
        sides_length1 = count_length_of_sides_of_complete_graph(angles_coordinates[i])
        sides_length.append(sides_length1)

    return sides_length


def count_length_of_sides_of_complete_graph(angles_coordinates):
    angles_coordinates = angles_coordinates
    sides_coordinates = []
    sides = []

    iter = itertools.combinations(angles_coordinates, 2)
    for value in iter:
        side = value
        sides_coordinates.append(side)

    sides_length = []

    for side in sides_coordinates:
        point1 = side[0]
        point2 = side[1]

        side_length = math.sqrt(abs(point1[0] - point2[0]) ** 2 + abs(point1[1] - point2[1]) ** 2)
        side_length1 = round(side_length, 3)
        side_length2 = int(side_length)
        sides_length.append(side_length1)
    
    sides = sides_length

    return sides


async def count_length_of_sides_of_complete_graph_async(angles_coordinates):
    angles_coordinates = angles_coordinates
    sides_coordinates = []
    sides = []

    iter = itertools.combinations(angles_coordinates, 2)
    for value in iter:
        side = value
        sides_coordinates.append(side)

    sides_length = []

    for side in sides_coordinates:
        point1 = side[0]
        point2 = side[1]

        side_length = math.sqrt(abs(point1[0] - point2[0]) ** 2 + abs(point1[1] - point2[1]) ** 2)
        side_length1 = round(side_length, 3)
        side_length2 = int(side_length)
        sides_length.append(side_length1)
    
    sides = sides_length

    return sides


def count_length_of_sides_of_rectangle(angles_coordinates):
    angles_coordinates = angles_coordinates
    sides_coordinates = []
    sides = []

    iter = itertools.combinations(angles_coordinates, 2)
    for value in iter:
        side = value
        sides_coordinates.append(side)

    sides_length = []

    for side in sides_coordinates:
        point1 = side[0]
        point2 = side[1]

        side_length = math.sqrt(abs(point1[0] - point2[0]) ** 2 + abs(point1[1] - point2[1]) ** 2)
        sides_length.append(int(side_length))
    
    sides_length2 = sides_length.copy()
    
    diagonals_length = []

    maximum_length = 0
    for side_length in sides_length2:
        if side_length > maximum_length:
            maximum_length = side_length
    diagonals_length.append(maximum_length)
    sides_length2.remove(maximum_length)

    maximum_length = 0
    for side_length in sides_length2:
        if side_length > maximum_length:
            maximum_length = side_length
    diagonals_length.append(maximum_length)

    for diagonal_length in diagonals_length:
        sides_length.remove(diagonal_length)

    sides_length2 = sides_length.copy() 
    
    minimum_side_length = diagonals_length[0]
    for side_length in sides_length2:
        if side_length < minimum_side_length:
            minimum_side_length = side_length
    
    ordinal_sides_length = []
    ordinal_sides_length.append(minimum_side_length)

    ordinal_side_length = 0
    for side_length in sides_length2:
        if side_length != minimum_side_length:
            ordinal_side_length = side_length
        
    ordinal_sides_length.append(ordinal_side_length)

    sides_length = []
    sides_length.extend(ordinal_sides_length)
    sides_length.extend(ordinal_sides_length)

    sides.append(sides_length)
    sides.append(diagonals_length)

    return sides


def count_length_of_sides_of_triangle(angles_coordinates):
    angles_coordinates = angles_coordinates
    sides_coordinates = []

    for i in range(len(angles_coordinates)):
        point1 = angles_coordinates[i-1]
        point2 = angles_coordinates[i]

        side = [point1, point2]
        sides_coordinates.append(side)

    sides_length = []

    for side in sides_coordinates:
        point1 = side[0]
        point2 = side[1]

        side_length = math.sqrt(abs(point1[0] - point2[0]) ** 2 + abs(point1[1] - point2[1]) ** 2)
        sides_length.append(int(side_length))

    return sides_length


def count_nears(graph, start, iterations, img, quality):
    graph = graph
    start = start
    iterations = iterations
    img = img
    quality = quality

    frontier = Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True
    nears_count = 0
    n = iterations

    # first iteration
    current = frontier.get()

    for next in graph.nears2(current):
        if next not in visited:
            (x, y) = next

            if check_not_in_bounds((y, x), img):

                if img[y, x, 0] < 100 - quality and\
                    img[y, x, 1] < 100 - quality and\
                    img[y, x, 2] < 100 - quality:
                    
                    nears_count += 1

            visited[next] = True
            frontier.put(next)
    n -= 1

    # next iterations
    for i in range(n):
        frontier2 = Queue()
        while not frontier.empty():
            current = frontier.get()

            for next in graph.nears2(current):
                if next not in visited:
                    (x, y) = next

                    if check_not_in_bounds((y, x), img):

                        if img[y, x, 0] < 100 - quality and\
                            img[y, x, 1] < 100 - quality and\
                            img[y, x, 2] < 100 - quality:
                            
                            nears_count += 1

                    visited[next] = True
                    frontier2.put(next)

        frontier = frontier2
        
    return nears_count


def count_nears2(graph, start, iterations, img, quality):
    graph = graph
    start = start
    iterations = iterations
    img = img
    quality = quality

    frontier = Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True
    nears_out_of_border_count = 0
    nears_in_border_count = 0
    in_to_out_ratio = 0
    nears_out_of_border = []
    nears_in_border = []
    n = iterations

    # first iteration
    current = frontier.get()

    for next in graph.nears2(current):
        if next not in visited:
            (x, y) = next

            if check_not_in_bounds((y, x), img):

                if img[y, x, 0] > 255 - (100 - quality) and\
                    img[y, x, 1] > 255 - (100 - quality) and\
                    img[y, x, 2] > 255 - (100 - quality):
                    
                    nears_out_of_border_count += 1
                    nears_out_of_border.append(next)

                if img[y, x, 0] < (100 - quality) and\
                    img[y, x, 1] < (100 - quality) and\
                    img[y, x, 2] < (100 - quality):

                    nears_in_border_count += 1
                    nears_in_border.append(next)

            visited[next] = True
            frontier.put(next)

    n -= 1

    # next iterations
    for i in range(n):
        frontier2 = Queue()
        while not frontier.empty():
            current = frontier.get()

            for next in graph.nears2(current):
                if next not in visited:
                    (x, y) = next

                    if check_not_in_bounds((y, x), img):

                        if img[y, x, 0] > 255 - (100 - quality) and\
                            img[y, x, 1] > 255 - (100 - quality) and\
                            img[y, x, 2] > 255 - (100 - quality):
                        
                            nears_out_of_border_count += 1
                            nears_out_of_border.append(next)

                        if img[y, x, 0] < (100 - quality) and\
                            img[y, x, 1] < (100 - quality) and\
                            img[y, x, 2] < (100 - quality):

                            nears_in_border_count += 1
                            nears_in_border.append(next)

                    visited[next] = True
                    frontier2.put(next)

        frontier = frontier2

    if nears_out_of_border_count > 0:
        in_to_out_ratio = nears_in_border_count / nears_out_of_border_count

    min_y = img.shape[1]
    max_y = 0
    for value in nears_out_of_border:
        (x, y) = value
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y
    out_of_border_height = max_y - min_y

    min_y = img.shape[1]
    max_y = 0
    for value in nears_in_border:
        (x, y) = value
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y
    in_border_height = max_y - min_y

    min_x = img.shape[0]
    max_x = 0
    for value in nears_out_of_border:
        (x, y) = value
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
    out_of_border_width = max_x - min_x

    min_x = img.shape[0]
    max_x = 0
    for value in nears_in_border:
        (x, y) = value
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
    in_border_width = max_x - min_x

    if out_of_border_height == in_border_height or out_of_border_width == in_border_width:
        in_to_out_ratio = 0

    return in_to_out_ratio


def count_nears2_in_triangle(graph, start, iterations, img, quality):
    graph = graph
    start = start
    iterations = iterations
    img = img
    quality = quality

    frontier = Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True

    nears_out_of_border_count = 0
    nears_in_border_count = 0
    in_to_out_ratio = 0
    nears_out_of_border = []
    nears_in_border = []
    n = iterations

    # first iteration
    current = frontier.get()

    for next in graph.nears2(current):
        if next not in visited:
            (x, y) = next

            if check_not_in_bounds((y, x), img):

                if img[y, x, 0] > 255 - (100 - quality) and\
                    img[y, x, 1] > 255 - (100 - quality) and\
                    img[y, x, 2] > 255 - (100 - quality):
                    
                    nears_out_of_border_count += 1
                    nears_out_of_border.append(next)

                if img[y, x, 0] < (100 - quality) and\
                    img[y, x, 1] < (100 - quality) and\
                    img[y, x, 2] < (100 - quality):

                    nears_in_border_count += 1
                    nears_in_border.append(next)

            visited[next] = True

            frontier.put(next)

    n -= 1

    # next iterations
    for i in range(n):
        frontier2 = Queue()
        while not frontier.empty():
            current = frontier.get()

            for next in graph.nears2(current):
                if next not in visited:
                    (x, y) = next

                    if check_not_in_bounds((y, x), img):
                    
                        if img[y, x, 0] > 255 - (100 - quality) and\
                            img[y, x, 1] > 255 - (100 - quality) and\
                            img[y, x, 2] > 255 - (100 - quality):
                        
                            nears_out_of_border_count += 1
                            nears_out_of_border.append(next)

                        if img[y, x, 0] < (100 - quality) and\
                            img[y, x, 1] < (100 - quality) and\
                            img[y, x, 2] < (100 - quality):

                            nears_in_border_count += 1
                            nears_in_border.append(next)

                    visited[next] = True
                    
                    frontier2.put(next)

        frontier = frontier2
    
    if nears_out_of_border_count > 0:
        in_to_out_ratio = nears_in_border_count / nears_out_of_border_count

    min_y = img.shape[1]
    max_y = 0
    for value in nears_out_of_border:
        (x, y) = value
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y
    out_of_border_height = max_y - min_y

    min_y = img.shape[1]
    max_y = 0
    for value in nears_in_border:
        (x, y) = value
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y
    in_border_height = max_y - min_y

    min_x = img.shape[0]
    max_x = 0
    for value in nears_out_of_border:
        (x, y) = value
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
    out_of_border_width = max_x - min_x

    min_x = img.shape[0]
    max_x = 0
    for value in nears_in_border:
        (x, y) = value
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
    in_border_width = max_x - min_x

    if out_of_border_height == in_border_height: 
        range_height = out_of_border_height
    else:
        range_height = out_of_border_height + in_border_height

    if out_of_border_width == in_border_width: 
        range_width = out_of_border_width
    else:
        range_width = out_of_border_width + in_border_width
    height_to_width_ratio = range_height / range_width

    if out_of_border_width == in_border_width:
        in_to_out_ratio = 0
    
    if (out_of_border_height + in_border_height) / (out_of_border_width + in_border_width) == height_to_width_ratio:
        in_to_out_ratio = 0

    return in_to_out_ratio


def count_value_of_angles_in_rectangle(sides):
    sides = sides

    sides_length = sides[0]
    side1 = sides_length[0]
    side2 = sides_length[1]
    side3 = sides_length[2]
    side4 = sides_length[3]
    diagonals_length = sides[1]
    diagonal_1_3 = diagonals_length[0]
    diagonal_2_4 = diagonals_length[1]

    values_of_angles = []

    angle_1_2 = 180 / math.pi * math.acos((side1 ** 2 + side2 ** 2 - diagonal_1_3 **2) / (2 * side1 * side2))
    values_of_angles.append(int(angle_1_2))
    angle_2_3 = 180 / math.pi * math.acos((side2 ** 2 + side3 ** 2 - diagonal_2_4 **2) / (2 * side2 * side3))
    values_of_angles.append(int(angle_2_3))
    angle_3_4 = 180 / math.pi * math.acos((side3 ** 2 + side4 ** 2 - diagonal_1_3 **2) / (2 * side3 * side4))
    values_of_angles.append(int(angle_3_4))
    angle_4_1 = 180 / math.pi * math.acos((side4 ** 2 + side1 ** 2 - diagonal_2_4 **2) / (2 * side4 * side1))
    values_of_angles.append(int(angle_4_1))

    return values_of_angles


def count_value_of_angles_in_similar_triangle(graph1):
    graph1 = graph1

    values_of_angles_in_similar_triangle = graph1.values_of_angles

    return values_of_angles_in_similar_triangle


def count_value_of_angles_in_triangle(sides_length):
    sides_length = sides_length
    side1 = sides_length[0]
    side2 = sides_length[1]
    side3 = sides_length[2]

    values_of_angles = []

    angle_1_2 = 180 / math.pi * math.acos((side1 ** 2 + side2 ** 2 - side3 **2) / (2 * side1 * side2))
    angle_2_3 = 180 / math.pi * math.acos((side2 ** 2 + side3 ** 2 - side1 **2) / (2 * side2 * side3))
    angle_3_1 = 180 / math.pi * math.acos((side3 ** 2 + side1 ** 2 - side2 **2) / (2 * side3 * side1))

    values_of_angles.append(int(angle_3_1))
    values_of_angles.append(int(angle_1_2))
    values_of_angles.append(int(angle_2_3))

    return values_of_angles


def create_graph(graph_area):
    graph_area = graph_area
    graph = SimpleGraph()
    
    graph_area2 = []
    for i in range(len(graph_area)):
        graph_area2.append(graph_area[i])

    for i in range(len(graph_area)):
        x = graph_area[i][0]
        y = graph_area[i][1]
        graph.edges[(x, y)] = []

        nears = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        for near in nears:
            if near in graph_area:
                graph.edges[(x, y)].append(near)
        
        graph_area2.remove((x, y))
    
    return graph


async def create_graph_async(graph_area, graph_number):
    print(graph_number)
    
    graph_area = graph_area
    graph_number = graph_number

    graph = SimpleGraph()
    graph_area2 = []

    for i in range(len(graph_area)):
        graph_area2.append(graph_area[i])

    for i in range(len(graph_area)):
        x = graph_area[i][0]
        y = graph_area[i][1]
        graph.edges[(x, y)] = []

        nears = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        for near in nears:
            if near in graph_area:
                graph.edges[(x, y)].append(near)
        
        graph_area2.remove((x, y))

    return graph


def create_img_array(img_shape):
    img_shape = img_shape

    img_array = numpy.zeros((img_shape, img_shape, 3), numpy.uint8)

    return img_array


def create_img_array_from_graph(graph, img):
    graph = graph
    img = img

    coordinates_to_cut = find_coordinates_to_cut2(graph, img)
    (min_x, min_y) = coordinates_to_cut[1]
    modified_img1 = img[(coordinates_to_cut[1][1])-10:(coordinates_to_cut[3][1]+10),
                        (coordinates_to_cut[1][0])-10:(coordinates_to_cut[3][0]+10)]
    
    maximum_shape = modified_img1.shape[0]
    if modified_img1.shape[1] > maximum_shape:
        maximum_shape = modified_img1.shape[1]

    modified_img1_shape = maximum_shape

    img_array = [[[255 for i in range(3)] for i in range(modified_img1_shape)] for i in range(modified_img1_shape)]
    modified_img1 = numpy.array(img_array, dtype=numpy.uint8)

    coordinate1 = (coordinates_to_cut[3][1]+10) - (coordinates_to_cut[1][1]-10)
    coordinate2 = (coordinates_to_cut[3][0]+10) - (coordinates_to_cut[1][0]-10)

    img_to_cut = img[(coordinates_to_cut[1][1])-10:(coordinates_to_cut[3][1]+10),
                            (coordinates_to_cut[1][0])-10:(coordinates_to_cut[3][0]+10)]

    modified_img1[0:coordinate1, 0:coordinate2] = img_to_cut

    return modified_img1


async def create_img_array_from_graph_async(graph, img):
    graph = graph
    img = img

    coordinates_to_cut = find_coordinates_to_cut2(graph, img)
    (min_x, min_y) = coordinates_to_cut[1]
    modified_img1 = img[(coordinates_to_cut[1][1])-10:(coordinates_to_cut[3][1]+10),
                        (coordinates_to_cut[1][0])-10:(coordinates_to_cut[3][0]+10)]
    
    maximum_shape = modified_img1.shape[0]
    if modified_img1.shape[1] > maximum_shape:
        maximum_shape = modified_img1.shape[1]

    modified_img1_shape = maximum_shape

    img_array = [[[255 for i in range(3)] for i in range(modified_img1_shape)] for i in range(modified_img1_shape)]
    modified_img1 = numpy.array(img_array, dtype=numpy.uint8)

    coordinate1 = (coordinates_to_cut[3][1]+10) - (coordinates_to_cut[1][1]-10)
    coordinate2 = (coordinates_to_cut[3][0]+10) - (coordinates_to_cut[1][0]-10)

    img_to_cut = img[(coordinates_to_cut[1][1])-10:(coordinates_to_cut[3][1]+10),
                            (coordinates_to_cut[1][0])-10:(coordinates_to_cut[3][0]+10)]

    modified_img1[0:coordinate1, 0:coordinate2] = img_to_cut

    return modified_img1


def create_rectangular_graph(graph_area, height_to_width_ratio):
    graph_area = graph_area
    height_to_width_ratio = height_to_width_ratio
    
    height_step = height_to_width_ratio[0]
    width_step = height_to_width_ratio[1]

    graph = SimpleGraph()
    
    graph_area2 = []
    for i in range(len(graph_area)):
        graph_area2.append(graph_area[i])

    for i in range(len(graph_area)):
        x = graph_area[i][0]
        y = graph_area[i][1]
        graph.edges[(x, y)] = []

        nears = [(x+width_step, y), (x, y-height_step), (x-width_step, y), (x, y+height_step)]
        for near in nears:
            if near in graph_area:
                graph.edges[(x, y)].append(near)
        
        graph_area2.remove((x, y))
    
    return graph



def create_triangle_area(img, quality):
    img = img
    quality = quality

    triangle_area = []
    
    for i in range(img.shape[0]): 
        for j in range(img.shape[1]):
            if img[i][j][0] < 100 - quality and\
                img[i][j][1] < 100 - quality and\
                img[i][j][2] < 100 - quality:
                
                triangle_area.append((j, i))
    
    return triangle_area


def find_coordinates_to_cut(angles_coordinates, img):
    angles_coordinates = angles_coordinates
    img = img

    width = img.shape[0]
    height = img.shape[1]

    min_x = height
    min_y = width
    max_x = 0
    max_y = 0

    for value in angles_coordinates:
        (x, y) = value

        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y
        if x > max_x:
            max_x = x
        if y > max_y:   
            max_y = y

    coordinates_to_cut = [(min_x, max_y), (min_x, min_y), (max_x, min_y), (max_x, max_y)]

    return coordinates_to_cut


def find_coordinates_to_cut2(graph, img):
    graph = graph
    img = img

    width = img.shape[0]
    height = img.shape[1]

    min_x = height
    min_y = width
    max_x = 0
    max_y = 0

    for value in graph.edges.keys():
        (x, y) = value

        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y
        if x > max_x:
            max_x = x
        if y > max_y:   
            max_y = y

    coordinates_to_cut = [(min_x, max_y), (min_x, min_y), (max_x, min_y), (max_x, max_y)]

    return coordinates_to_cut


async def find_coordinates_to_cut_async(angles_coordinates, img):
    angles_coordinates = angles_coordinates
    img = img

    width = img.shape[0]
    height = img.shape[1]

    min_x = height
    min_y = width
    max_x = 0
    max_y = 0

    for value in angles_coordinates:
        (x, y) = value

        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y
        if x > max_x:
            max_x = x
        if y > max_y:   
            max_y = y

    coordinates_to_cut = [(min_x, max_y), (min_x, min_y), (max_x, min_y), (max_x, max_y)]

    return coordinates_to_cut


def find_inner_angles_coordinates(graph, angles_number, iterations, img, quality):
    graph = graph
    angles_number = angles_number
    iterations = iterations
    img = img
    quality = quality
    
    angles_coordinates_dict = {}
    angles_coordinates = []
    in_to_out_ratio_dict = {}

    for key in graph.edges.keys():
        in_to_out_ratio = count_nears2(graph, key, iterations, img, quality)
        in_to_out_ratio_dict[key] = in_to_out_ratio

    for key, value in in_to_out_ratio_dict.items():
        if value == 3:
            angles_coordinates_dict[key] = value

    if len(angles_coordinates_dict.keys()) > angles_number:
        angles_neighbors_copy = angles_coordinates_dict.copy()
        search_radius = math.ceil(iterations * 1.5)             # > iterations
        angles_regions = []
        visited = []

        for key, value in angles_coordinates_dict.items():
            if key not in visited:
                nears = near_points_search(angles_neighbors_copy.keys(), key, search_radius)
                region = [key]
                region.extend(nears)
                angles_regions.append(region)
                visited.extend(region)

        for region in angles_regions:
            sum_x = 0
            sum_y = 0

            for value in region:
                (x, y) = value
                sum_x += x
                sum_y += y
            
            angle_coordinate_x = sum_x / len(region)
            angle_coordinate_y = sum_y / len(region)

            angle_coordinates = (angle_coordinate_x, angle_coordinate_y)
            angle_coordinates_rounded = (round(angle_coordinate_x), round(angle_coordinate_y))
            angles_coordinates.append(angle_coordinates_rounded)
    else:
        for key in angles_coordinates_dict.keys():
            angles_coordinates.append(key)
    
    angles_coordinates = angles_coordinates

    return angles_coordinates


def find_inner_angles_coordinates_of_triangle(graph, angles_number, iterations, img, quality):
    graph = graph
    angles_number = angles_number
    iterations = iterations
    img = img
    quality = quality
    
    angles_coordinates_dict = {}
    angles_coordinates = []
    in_to_out_ratio_dict = {}

    for key in graph.edges.keys():
        in_to_out_ratio = count_nears(graph, key, iterations, img, quality)
        in_to_out_ratio_dict[key] = in_to_out_ratio

    for key, value in in_to_out_ratio_dict.items():
        if 7 <= value <= 11:
            angles_coordinates_dict[key] = value

    for key, value in in_to_out_ratio_dict.items():
        if value > 0:
            value_to_reduce = .225
            quad_diff = 0.1

            if value_to_reduce - value_to_reduce * quad_diff <= value <= value_to_reduce + value_to_reduce * quad_diff:
                angles_coordinates_dict[key] = value

    if len(angles_coordinates_dict.keys()) > angles_number:
        angles_nears_copy = angles_coordinates_dict.copy()
        search_radius = math.ceil(iterations * 1.5)             # > iterations
        angles_regions = []
        visited = []

        for key, value in angles_coordinates_dict.items():
            if key not in visited:
                nears = near_points_search(angles_nears_copy.keys(), key, search_radius)
                region = [key]
                region.extend(nears)
                angles_regions.append(region)
                visited.extend(region)

        for region in angles_regions:
            sum_x = 0
            sum_y = 0

            for value in region:
                (x, y) = value
                sum_x += x
                sum_y += y
            
            angle_coordinate_x = sum_x / len(region)
            angle_coordinate_y = sum_y / len(region)

            angle_coordinates = (angle_coordinate_x, angle_coordinate_y)
            angle_coordinates_rounded = (round(angle_coordinate_x), round(angle_coordinate_y))
            angles_coordinates.append(angle_coordinates_rounded)
    else:
        for key in angles_coordinates_dict.keys():
            angles_coordinates.append(key)
    
    angles_coordinates = angles_coordinates

    print(angles_coordinates)
    
    coordinates = {}

    for value in angles_coordinates:
        for value2, ratio in angles_coordinates_dict.items():
            if value2 == value:
                coordinates[value] = ratio

    return coordinates


def find_nearest_point(rectangle, points):
    rectangle = rectangle
    points = points
    nearest_point = (None, None)

    minimum_distance = 100
    for rectangle_point in rectangle:
        (x1, y1) = rectangle_point
        for point in points:
            (x2, y2) = point
            distance = math.sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)
            if distance < minimum_distance:
                minimum_distance = distance
                nearest_point = point
    
    return nearest_point


def find_nearest_point_to_point(point, points_to_find, img):
    point = point
    points_to_find = points_to_find
    img = img

    nearest_point = (None, None)
    minimum_distance = img.shape[0]

    (x1, y1) = point
    for point_to_find in points_to_find:
        (x2, y2) = point_to_find
        distance = math.sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)
        if distance < minimum_distance:
            minimum_distance = distance
            nearest_point = point_to_find

    return nearest_point


def find_nearest_rectangle(rectangle, rectangles):
    rectangle = rectangle
    near_rectangles = rectangles
    nearest_rectangle = []

    minimum_distance = 100
    for rectangle_point in rectangle:
        (x1, y1) = rectangle_point
        for near_rectangle in near_rectangles:
            for point in near_rectangle:
                (x2, y2) = point
                distance = math.sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)
                if distance < minimum_distance:
                    minimum_distance = distance
                    nearest_point = point
                    nearest_rectangle = near_rectangle

    return nearest_rectangle, nearest_point


def find_angles_coordinates(graph, img, quality):
    graph = graph
    img = img
    quality = quality

    angles_coordinates = []

    for k in range(1, 11):
        angles_coordinates1 = []
        for i in range(2, 3):
            outer_angles_coordinates = find_outer_angles_coordinates(graph, k, i, img, quality)
            angles_coordinates1.append(outer_angles_coordinates)

        angles_coordinates.append(angles_coordinates1[-1])

    return angles_coordinates


async def find_angles_coordinates_async(graph, img, quality, graph_number):
    print(graph_number)
    
    graph = graph
    img = img
    quality = quality
    graph_number = graph_number

    angles_coordinates = []

    for k in range(1, 11):
        angles_coordinates1 = []
        for i in range(2, 3):
            outer_angles_coordinates = find_outer_angles_coordinates(graph, k, i, img, quality)
            angles_coordinates1.append(outer_angles_coordinates)

        angles_coordinates.append(angles_coordinates1[-1])

    return angles_coordinates


def find_angles_coordinates_from_img(modified_images, inf_coordinates, quality):
    modified_images = modified_images
    inf_coordinates = inf_coordinates
    quality = quality

    angles_coordinates = []

    for k in range(1, 11):
        modified_img = modified_images[k-1]
        (min_x, min_y) = inf_coordinates[k-1]

        width = modified_img.shape[0]
        height = modified_img.shape[1]
        height_to_width_ratio = (3, 2)

        grid = SquareGrid(width, height)
        grid_center = (int(width / 2), int(height / 2))

        rectangle_area = breadth_first_search2(grid, grid_center, modified_img, quality)
        graph = create_graph(rectangle_area)

        angles_coordinates2 = []

        for i in range(2, 3):
            angles_coordinates2_2 = []
            middle_coordinates = find_outer_angles_coordinates(graph, k, i, modified_img, quality)
            for value in middle_coordinates:
                (x, y) = value
                angles_coordinates2_2.append((x + min_x - 10, y + min_y - 10))

            angles_coordinates2.append(angles_coordinates2_2)
        
        angles_coordinates.append(angles_coordinates2[-1])

    return angles_coordinates


async def find_angles_coordinates_from_img_async(modified_images, inf_coordinates, quality, graph_number):
    print(graph_number)
    
    modified_images = modified_images
    inf_coordinates = inf_coordinates
    quality = quality
    graph_number = graph_number

    angles_coordinates = []

    for k in range(1, 11):
        modified_img = modified_images[k-1]
        (min_x, min_y) = inf_coordinates[k-1]

        width = modified_img.shape[0]
        height = modified_img.shape[1]
        height_to_width_ratio = (3, 2)

        grid = SquareGrid(width, height)
        grid_center = (int(width / 2), int(height / 2))

        rectangle_area = breadth_first_search2(grid, grid_center, modified_img, quality)
        graph = create_graph(rectangle_area)

        angles_coordinates2 = []

        for i in range(2, 3):
            angles_coordinates2_2 = []
            middle_coordinates = find_outer_angles_coordinates(graph, k, i, modified_img, quality)
            for value in middle_coordinates:
                (x, y) = value
                angles_coordinates2_2.append((x + min_x - 10, y + min_y - 10))

            angles_coordinates2.append(angles_coordinates2_2)
        
        angles_coordinates.append(angles_coordinates2[-1])

    return angles_coordinates


def find_outer_angles_coordinates(graph, angles_number, iterations, img, quality):
    graph = graph
    angles_number = angles_number
    iterations = iterations
    img = img
    quality = quality
    
    angles_coordinates_dict = {}
    angles_coordinates = []
    number_of_nears = {}
    search_radius = math.ceil(iterations * 1.5)             # > iterations

    for key in graph.edges.keys():
        nears_count = count_nears(graph, key, iterations, img, quality)
        number_of_nears[key] = nears_count
    
    number_of_nears_copy = number_of_nears.copy()

    width = img.shape[0]
    height = img.shape[1]
    bounds = [
                (width-1, height-1), (width-1, 0), (0, height-1),
                (0, 0), (1, 0), (0, 1), (1, 1),
                (height-1, width-1), (0, width-1), (height-1, 0),
            ]
    
    for value in number_of_nears_copy.keys():
        (x1, y1) = value
        for bound in bounds:
            (x2, y2) = bound
            if x1 == x2 or y1 == y2 or x1 == y2 or y1 == x2:
                if value in number_of_nears.keys():
                    number_of_nears.pop(value)

    number_of_nears_copy = number_of_nears.copy()

    while len(angles_coordinates_dict) < angles_number:
        min_value = max(number_of_nears_copy.values())

        for key, value in number_of_nears_copy.items():
            if value == min_value:
                min_value_key = key

        for key, value in number_of_nears_copy.items():
            if value < min_value:
                min_value = value
                min_value_key = key
        
        is_min_value_redundant = False
        for value in angles_coordinates_dict.keys():
            if are_near_points(value, min_value_key, search_radius):
                is_min_value_redundant = True
                
        if not is_min_value_redundant:
            angles_coordinates_dict[min_value_key] = min_value

        number_of_nears_copy.pop(min_value_key)

    if len(angles_coordinates_dict) == angles_number:
        additional_min_value = max(number_of_nears_copy.values())

        for key, value in number_of_nears_copy.items():
            if value == additional_min_value:
                additional_min_value_key = key

        for key, value in number_of_nears_copy.items():
            if value < additional_min_value:
                additional_min_value = value
                additional_min_value_key = key

    angles_coordinates_dict_values = []
    angles_coordinates_dict_keys = []
    for key, value in angles_coordinates_dict.items():
        angles_coordinates_dict_keys.append(key)
        angles_coordinates_dict_values.append(value)

    values_length = len(angles_coordinates_dict_values)
    while additional_min_value == angles_coordinates_dict_values[values_length-1] and len(number_of_nears_copy) >= 1:
        angles_coordinates_dict[additional_min_value_key] = additional_min_value
        angles_coordinates_dict_values.append(additional_min_value)
        angles_coordinates_dict_keys.append(additional_min_value_key)

        number_of_nears_copy.pop(additional_min_value_key)
        if len(number_of_nears_copy.values()) > 0:
            additional_min_value = max(number_of_nears_copy.values())
            
            for key, value in number_of_nears_copy.items():
                if value == additional_min_value:
                    additional_min_value_key = key

        for key, value in number_of_nears_copy.items():
            if value < additional_min_value:
                additional_min_value = value
                additional_min_value_key = key

    search_radius = math.ceil(iterations * 1.5)             # > iterations
    angles_regions = []
    visited = []

    for key in angles_coordinates_dict_keys:
        if key not in visited:
            nears = near_points_search(angles_coordinates_dict_keys, key, search_radius)
            region = [key]
            region.extend(nears)
            angles_regions.append(region)
            visited.extend(region)

    for region in angles_regions:
        sum_x = 0
        sum_y = 0

        for value in region:
            (x, y) = value
            sum_x += x
            sum_y += y
        
        angle_coordinate_x = sum_x / len(region)
        angle_coordinate_y = sum_y / len(region)

        angle_coordinates = (angle_coordinate_x, angle_coordinate_y)
        angle_coordinates_rounded = (round(angle_coordinate_x), round(angle_coordinate_y))
        angles_coordinates.append(angle_coordinates_rounded)

    angles_coordinates_copy = angles_coordinates.copy()
    width = img.shape[0]
    height = img.shape[1]
    bounds = [
                (width-1, height-1), (width-1, 0), (0, height-1),
                (0, 0), (1, 0), (0, 1), (1, 1),
                (height-1, width-1), (0, width-1), (height-1, 0),
            ]
    for value in angles_coordinates_copy:
        (x1, y1) = value
        for bound in bounds:
            (x2, y2) = bound
            if x1 == x2 or y1 == y2 or x1 == y2 or y1 == x2:
                if value in angles_coordinates:
                    angles_coordinates.remove(value)

    return angles_coordinates


async def find_outer_angles_coordinates_async(graph, angles_number, iterations, img, quality):
    graph = graph
    angles_number = angles_number
    iterations = iterations
    img = img
    quality = quality

    angles_coordinates_dict = {}
    angles_coordinates = []
    number_of_nears = {}
    search_radius = math.ceil(iterations * 1.5)             # > iterations

    for key in graph.edges.keys():
        nears_count = count_nears(graph, key, iterations, img, quality)
        number_of_nears[key] = nears_count
    
    number_of_nears_copy = number_of_nears.copy()

    width = img.shape[0]
    height = img.shape[1]
    bounds = [
                (width-1, height-1), (width-1, 0), (0, height-1),
                (0, 0), (1, 0), (0, 1), (1, 1),
                (height-1, width-1), (0, width-1), (height-1, 0),
            ]
    
    for value in number_of_nears_copy.keys():
        (x1, y1) = value
        for bound in bounds:
            (x2, y2) = bound
            if x1 == x2 or y1 == y2 or x1 == y2 or y1 == x2:
                if value in number_of_nears.keys():
                    number_of_nears.pop(value)

    number_of_nears_copy = number_of_nears.copy()

    while len(angles_coordinates_dict) < angles_number:
        min_value = max(number_of_nears_copy.values())

        for key, value in number_of_nears_copy.items():
            if value == min_value:
                min_value_key = key

        for key, value in number_of_nears_copy.items():
            if value < min_value:
                min_value = value
                min_value_key = key
        
        is_min_value_redundant = False
        for value in angles_coordinates_dict.keys():
            if are_near_points(value, min_value_key, search_radius):
                is_min_value_redundant = True
                
        if not is_min_value_redundant:
            angles_coordinates_dict[min_value_key] = min_value

        number_of_nears_copy.pop(min_value_key)

    if len(angles_coordinates_dict) == angles_number:
        additional_min_value = max(number_of_nears_copy.values())

        for key, value in number_of_nears_copy.items():
            if value == additional_min_value:
                additional_min_value_key = key

        for key, value in number_of_nears_copy.items():
            if value < additional_min_value:
                additional_min_value = value
                additional_min_value_key = key

    angles_coordinates_dict_values = []
    angles_coordinates_dict_keys = []
    for key, value in angles_coordinates_dict.items():
        angles_coordinates_dict_keys.append(key)
        angles_coordinates_dict_values.append(value)

    values_length = len(angles_coordinates_dict_values)
    while additional_min_value == angles_coordinates_dict_values[values_length-1] and len(number_of_nears_copy) >= 1:
        angles_coordinates_dict[additional_min_value_key] = additional_min_value
        angles_coordinates_dict_values.append(additional_min_value)
        angles_coordinates_dict_keys.append(additional_min_value_key)

        number_of_nears_copy.pop(additional_min_value_key)
        if len(number_of_nears_copy.values()) > 0:
            additional_min_value = max(number_of_nears_copy.values())
            
            for key, value in number_of_nears_copy.items():
                if value == additional_min_value:
                    additional_min_value_key = key

        for key, value in number_of_nears_copy.items():
            if value < additional_min_value:
                additional_min_value = value
                additional_min_value_key = key

    search_radius = math.ceil(iterations * 1.5)             # > iterations
    angles_regions = []
    visited = []

    for key in angles_coordinates_dict_keys:
        if key not in visited:
            nears = near_points_search(angles_coordinates_dict_keys, key, search_radius)
            region = [key]
            region.extend(nears)
            angles_regions.append(region)
            visited.extend(region)

    for region in angles_regions:
        sum_x = 0
        sum_y = 0

        for value in region:
            (x, y) = value
            sum_x += x
            sum_y += y
        
        angle_coordinate_x = sum_x / len(region)
        angle_coordinate_y = sum_y / len(region)

        angle_coordinates = (angle_coordinate_x, angle_coordinate_y)
        angle_coordinates_rounded = (round(angle_coordinate_x), round(angle_coordinate_y))
        angles_coordinates.append(angle_coordinates_rounded)

    angles_coordinates_copy = angles_coordinates.copy()
    width = img.shape[0]
    height = img.shape[1]
    bounds = [
                (width-1, height-1), (width-1, 0), (0, height-1),
                (0, 0), (1, 0), (0, 1), (1, 1),
                (height-1, width-1), (0, width-1), (height-1, 0),
            ]
    for value in angles_coordinates_copy:
        (x1, y1) = value
        for bound in bounds:
            (x2, y2) = bound
            if x1 == x2 or y1 == y2 or x1 == y2 or y1 == x2:
                if value in angles_coordinates:
                    angles_coordinates.remove(value)

    return angles_coordinates


def find_outer_angles_coordinates_of_triangle(graph, angles_number, iterations, img, quality):
    graph = graph
    angles_number = angles_number
    iterations = iterations
    img = img
    quality = quality

    angles_coordinates_dict = {}
    angles_coordinates = []
    number_of_nears = {}

    for key in graph.edges.keys():
        nears_count = count_nears(graph, key, iterations, img, quality)
        number_of_nears[key] = nears_count

    number_of_nears_copy = number_of_nears.copy()

    while len(angles_coordinates_dict) < angles_number:
        min_value = max(number_of_nears_copy.values())

        for key, value in number_of_nears_copy.items():
            if value == min_value:
                min_value_key = key

        for key, value in number_of_nears_copy.items():
            if value < min_value:
                min_value = value
                min_value_key = key
        
        angles_coordinates_dict[min_value_key] = min_value
        number_of_nears_copy.pop(min_value_key)
    
    if len(angles_coordinates_dict) == angles_number:
        additional_min_value = max(number_of_nears_copy.values())

        for key, value in number_of_nears_copy.items():
            if value == additional_min_value:
                additional_min_value_key = key

        for key, value in number_of_nears_copy.items():
            if value < additional_min_value:
                additional_min_value = value
                additional_min_value_key = key

    angles_coordinates_dict_values = []
    angles_coordinates_dict_keys = []
    for key, value in angles_coordinates_dict.items():
        angles_coordinates_dict_keys.append(key)
        angles_coordinates_dict_values.append(value)

    values_length = len(angles_coordinates_dict_values)
    while additional_min_value == angles_coordinates_dict_values[values_length-1] and len(number_of_nears_copy) >= 1:
        angles_coordinates_dict[additional_min_value_key] = additional_min_value
        angles_coordinates_dict_values.append(additional_min_value)
        angles_coordinates_dict_keys.append(additional_min_value_key)

        number_of_nears_copy.pop(additional_min_value_key)
        if len(number_of_nears_copy.values()) > 0:
            additional_min_value = max(number_of_nears_copy.values())

            for key, value in number_of_nears_copy.items():
                if value == additional_min_value:
                    additional_min_value_key = key

        for key, value in number_of_nears_copy.items():
            if value < additional_min_value:
                additional_min_value = value
                additional_min_value_key = key

    search_radius = math.ceil(iterations * 1.5)             # > iterations
    angles_regions = []
    visited = []

    for key in angles_coordinates_dict_keys:
        if key not in visited:
            nears = near_points_search(angles_coordinates_dict_keys, key, search_radius)
            region = [key]
            region.extend(nears)
            angles_regions.append(region)
            visited.extend(region)

    for region in angles_regions:
        sum_x = 0
        sum_y = 0

        for value in region:
            (x, y) = value
            sum_x += x
            sum_y += y
        
        angle_coordinate_x = sum_x / len(region)
        angle_coordinate_y = sum_y / len(region)

        angle_coordinates = (angle_coordinate_x, angle_coordinate_y)
        angle_coordinates_rounded = (round(angle_coordinate_x), round(angle_coordinate_y))
        angles_coordinates.append(angle_coordinates_rounded)

    angles_coordinates_copy = angles_coordinates.copy()
    width = img.shape[0]
    height = img.shape[1]
    bounds = [(width-1, height-1), (width-1, 0), (0, height-1), (0, 0)]
    for value in angles_coordinates_copy:
        if value in bounds:
            angles_coordinates.remove(value)

    return angles_coordinates


def group_by_minimum_distance(graphs_list, img):
    graphs_list = graphs_list
    img = img

    width = img.shape[0]
    clusters = []
    min_distance1 = width
    min_distance2 = width

    for i in range(len(graphs_list)-1):
        min_x_1 = width
        max_x_1 = 0

        for value in graphs_list[i].edges.keys():
            (x, y) = value
            if x < min_x_1:
                min_x_1 = x
            if x > max_x_1:
                max_x_1 = x
        
        min_x_2 = width
        max_x_2 = 0

        for value in graphs_list[i+1].edges.keys():
            (x, y) = value
            if x < min_x_2:
                min_x_2 = x
            if x > max_x_2:
                max_x_2 = x

        distances = [
                        abs(max_x_2 - max_x_1),
                        abs(max_x_2 - min_x_1),
                        abs(min_x_2 - max_x_1),
                        abs(min_x_2 - min_x_1),
                    ]

        if min(distances) < min_distance1:
            min_distance1 = min(distances)

    min_distance2 = 4 * min_distance1

    for i in range(len(graphs_list)-1):
        min_x_1 = width
        max_x_1 = 0

        for value in graphs_list[i].edges.keys():
            (x, y) = value
            if x < min_x_1:
                min_x_1 = x
            if x > max_x_1:
                max_x_1 = x
        
        min_x_2 = width
        max_x_2 = 0

        for value in graphs_list[i+1].edges.keys():
            (x, y) = value
            if x < min_x_2:
                min_x_2 = x
            if x > max_x_2:
                max_x_2 = x

        distances = [
                        abs(max_x_2 - max_x_1),
                        abs(max_x_2 - min_x_1),
                        abs(min_x_2 - max_x_1),
                        abs(min_x_2 - min_x_1),
                    ]

        if 2 * min_distance1 < min(distances) < min_distance2:
            min_distance2 = min(distances)
    
    number_of_clusters = 1

    for i in range(len(graphs_list)-1):
        min_x_1 = width
        max_x_1 = 0

        for value in graphs_list[i].edges.keys():
            (x, y) = value
            if x < min_x_1:
                min_x_1 = x
            if x > max_x_1:
                max_x_1 = x
        
        min_x_2 = width
        max_x_2 = 0

        for value in graphs_list[i+1].edges.keys():
            (x, y) = value
            if x < min_x_2:
                min_x_2 = x
            if x > max_x_2:
                max_x_2 = x

        distances = [
                        abs(max_x_2 - max_x_1),
                        abs(max_x_2 - min_x_1),
                        abs(min_x_2 - max_x_1),
                        abs(min_x_2 - min_x_1),
                    ]

        min(distances)

        if abs(min_distance1 - min(distances)) > abs(min_distance2 - min(distances)):
            number_of_clusters += 1

    cluster = []
    clusters = [cluster for i in range(number_of_clusters)]
    cluster_index = 0

    for i in range(len(graphs_list)-1):
        min_x_1 = width
        max_x_1 = 0

        for value in graphs_list[i].edges.keys():
            (x, y) = value
            if x < min_x_1:
                min_x_1 = x
            if x > max_x_1:
                max_x_1 = x
        
        min_x_2 = width
        max_x_2 = 0

        for value in graphs_list[i+1].edges.keys():
            (x, y) = value
            if x < min_x_2:
                min_x_2 = x
            if x > max_x_2:
                max_x_2 = x

        distances = [
                        abs(max_x_2 - max_x_1),
                        abs(max_x_2 - min_x_1),
                        abs(min_x_2 - max_x_1),
                        abs(min_x_2 - min_x_1),
                    ]

        if abs(min_distance1 - min(distances)) < abs(min_distance2 - min(distances)):
            clusters[cluster_index].append(graphs_list[i])
            clusters[cluster_index].append(graphs_list[i+1])
        elif abs(min_distance1 - min(distances)) > abs(min_distance2 - min(distances)):
            graph_in_current_cluster = None
            graph_not_in_current_cluster = None

            if graphs_list[i] in clusters[cluster_index]:
                graph_in_current_cluster = graphs_list[i]
                graph_not_in_current_cluster = graphs_list[i+1]
            elif graphs_list[i+1] in clusters[cluster_index]:
                graph_in_current_cluster = graphs_list[i+1]
                graph_not_in_current_cluster = graphs_list[i]

            clusters[cluster_index].append(graph_in_current_cluster)
            cluster_index += 1
            clusters[cluster_index].append(graph_not_in_current_cluster)

    return clusters


def merge_angles_coordinates(angles_coordinates1, angles_coordinates2):
    angles_coordinates1 = angles_coordinates1
    angles_coordinates2 = angles_coordinates2

    angles_coordinates_list = []

    for k in range(len(angles_coordinates1)):
        for i in range(len(angles_coordinates2)):
            angles_coordinates = []
            angles_coordinates.extend(angles_coordinates1[k])
            angles_coordinates.extend(angles_coordinates2[i])
            angles_coordinates_list.append(angles_coordinates)

    return angles_coordinates_list


async def merge_angles_coordinates_async(angles_coordinates1, angles_coordinates2, graph_number):
    print(graph_number)

    angles_coordinates1 = angles_coordinates1
    angles_coordinates2 = angles_coordinates2
    graph_number = graph_number

    angles_coordinates_list = []

    for k in range(len(angles_coordinates1)):
        for i in range(len(angles_coordinates2)):
            angles_coordinates = []
            angles_coordinates.extend(angles_coordinates1[k])
            angles_coordinates.extend(angles_coordinates2[i])
            angles_coordinates_list.append(angles_coordinates)

    return angles_coordinates_list


def modify_shape(img):
    img = img

    max_value = img.shape[0]
    if img.shape[1] > max_value:
        max_value = img.shape[1]

    modified_img_shape = max_value
    img_array = [[[255 for i in range(3)] for i in range(modified_img_shape)] for i in range(modified_img_shape)]
    modified_img = numpy.array(img_array, dtype=numpy.uint8)
    img_to_cut = img[0:img.shape[0], 0:img.shape[1]]
    modified_img[0:img.shape[0], 0:img.shape[1]] = img_to_cut

    return modified_img


def modify_img_from_angles_coordinates(angles_coordinates, img):
    angles_coordinates = angles_coordinates
    img = img

    modified_images1 = []
    inf_coordinates = []

    for i in range(len(angles_coordinates)):
        modified_img = modify_src(img)

        coordinates_to_cut = find_coordinates_to_cut(angles_coordinates[i], img)
        (min_x, min_y) = coordinates_to_cut[1]
        
        modified_img2 = modified_img[(coordinates_to_cut[1][1])-10:(coordinates_to_cut[3][1]+10),
                                    (coordinates_to_cut[1][0])-10:(coordinates_to_cut[3][0]+10)]

        img_to_cut = modified_img2

        maximum_modified_img2_shape = modified_img2.shape[0]
        if modified_img2.shape[1] > maximum_modified_img2_shape:
            maximum_modified_img2_shape = modified_img2.shape[1]

        modified_img2_shape = maximum_modified_img2_shape
        modified_img2 = create_img_array(modified_img2_shape)

        coordinate1 = (coordinates_to_cut[3][1]+10) - (coordinates_to_cut[1][1]-10)
        coordinate2 = (coordinates_to_cut[3][0]+10) - (coordinates_to_cut[1][0]-10)

        modified_img2[0:coordinate1, 0:coordinate2] = img_to_cut

        modified_images1.append(modified_img2)
        inf_coordinates.append((min_x, min_y))

    modified_images = [modified_images1 , inf_coordinates]

    return modified_images


async def modify_img_from_angles_coordinates_async(angles_coordinates, img, graph_number):
    print(graph_number)
    
    angles_coordinates = angles_coordinates
    img = img
    graph_number = graph_number

    modified_images1 = []
    inf_coordinates = []

    for i in range(len(angles_coordinates)):
        modified_img = modify_src(img)

        coordinates_to_cut = find_coordinates_to_cut(angles_coordinates[i], img)
        (min_x, min_y) = coordinates_to_cut[1]
        
        modified_img2 = modified_img[(coordinates_to_cut[1][1])-10:(coordinates_to_cut[3][1]+10),
                                    (coordinates_to_cut[1][0])-10:(coordinates_to_cut[3][0]+10)]

        img_to_cut = modified_img2

        maximum_modified_img2_shape = modified_img2.shape[0]
        if modified_img2.shape[1] > maximum_modified_img2_shape:
            maximum_modified_img2_shape = modified_img2.shape[1]

        modified_img2_shape = maximum_modified_img2_shape
        modified_img2 = create_img_array(modified_img2_shape)

        coordinate1 = (coordinates_to_cut[3][1]+10) - (coordinates_to_cut[1][1]-10)
        coordinate2 = (coordinates_to_cut[3][0]+10) - (coordinates_to_cut[1][0]-10)

        modified_img2[0:coordinate1, 0:coordinate2] = img_to_cut

        modified_images1.append(modified_img2)
        inf_coordinates.append((min_x, min_y))

    modified_images = [modified_images1 , inf_coordinates]

    return modified_images


def modify_src(src):
    src = src
    
    values_complex_array = []
    for i in range(len(src)):
        values = src[i]

        values_arr = []
        for i in range(len(values)):
            values2 = values[i]
            
            [value1, value2, value3] = values2
            value1 = 255 - value1
            value2 = 255 - value2
            value3 = 255 - value3

            value_arr = numpy.array([value1, value2, value3], dtype=numpy.uint8)

            values_arr.append(value_arr)

        modified_values = numpy.vstack(values_arr)

        values_complex_array.append(modified_values)

    modified_values2 = numpy.array(values_complex_array, dtype=numpy.uint8)

    modified_src = modified_values2

    return modified_src


async def modify_src_async(src):
    src = src
    
    values_complex_array = []
    for i in range(len(src)):
        values = src[i]

        values_arr = []
        for i in range(len(values)):
            values2 = values[i]
            
            [value1, value2, value3] = values2
            value1 = 255 - value1
            value2 = 255 - value2
            value3 = 255 - value3

            value_arr = numpy.array([value1, value2, value3], dtype=numpy.uint8)

            values_arr.append(value_arr)

        modified_values = numpy.vstack(values_arr)

        values_complex_array.append(modified_values)

    modified_values2 = numpy.array(values_complex_array, dtype=numpy.uint8)

    modified_src = modified_values2

    return modified_src


def near_points_search(graph, start, search_radius):
    graph = graph
    start = start
    search_radius = search_radius
    
    near_points = []
    (x1, y1) = start

    for value in graph:
        (x2, y2) = value
        distance = math.sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)
        
        if 0 < distance <= search_radius:
            near_points.append(value)

    return near_points


def find_near_points(coordinates1, coordinates2):
    coordinates1 = coordinates1
    coordinates2 = coordinates2

    near_points_list = []
    min_distance = math.inf

    for coordinate1 in coordinates1:
        (x1, y1) = coordinate1
        near_points = []
        for coordinate2 in coordinates2:
            (x2, y2) = coordinate2
            distance = math.sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)
            if distance < min_distance:
                min_distance = distance
                near_points = [coordinate1, coordinate2]
        
        near_points_list.append(near_points)
        min_distance = math.inf

    return near_points_list


def find_near_points2(coordinates):
    coordinates = coordinates
    near_points_list = []

    coordinates_copy = coordinates.copy()
    min_distance = math.inf

    for coordinate1 in coordinates:
        (x1, y1) = coordinate1
        near_points = []
        for coordinate2 in coordinates_copy:
            (x2, y2) = coordinate2

            if coordinate1 != coordinate2:
                distance = math.sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)
                if distance < min_distance:
                    min_distance = distance
                    near_points = [coordinate1, coordinate2]

        near_points_list.append(near_points)
        min_distance = math.inf

    near_points_list2 = []

    for i in range(2):
        min_distance = math.inf

        for value in near_points_list:
            (x1, y1) = value[0]
            (x2, y2) = value[1]
            distance = math.sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)
            if distance < min_distance:
                min_distance = distance
                near_points = value
        
        min_distance = math.inf
        near_points_list2.append(near_points)
        near_points_list.remove(near_points)

    near_points_list = near_points_list2

    return near_points_list


def find_near_points_pairs(coordinates):
    coordinates = coordinates

    coordinates_pairs = []
    coordinates_copy = coordinates.copy()
    min_distance = math.inf
    nearest_point = None

    for coordinate1 in coordinates:
        (x1, y1) = coordinate1
        near_points = []
        
        for coordinate2 in coordinates_copy:
            (x2, y2) = coordinate2
            distance = math.sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)
            if distance > 0:
                if distance < min_distance:
                    min_distance = distance
                    nearest_point = coordinate2
        
        near_points = [coordinate1, nearest_point]
        if [nearest_point, coordinate1] not in coordinates_pairs:
            coordinates_pairs.append(near_points)
        min_distance = math.inf
        nearest_point = None

    return coordinates_pairs


def filter_edge_corners(angles_coordinates, graph):
    angles_coordinates = angles_coordinates
    graph = graph
    angles_coordinates2 = []

    coordinates1_is_in_graph = True
    coordinates2_is_in_graph = True
    coordinates3_is_in_graph = True
    coordinates4_is_in_graph = True

    for angle_coordinates in angles_coordinates:
        (x1, y1) = angle_coordinates[0]
        (x2, y2) = angle_coordinates[1]

        distance = 0
        distance1 = abs(y2 - y1)
        distance2 = abs(x2 - x1)
        
        max_distance = 0
        for value in [distance1, distance2]:
            if value > max_distance:
                max_distance = value

        distance = max_distance

        coordinate1 = (x1 - round(distance / 2), y1 - round(distance / 2))
        coordinate2 = (x1 + round(distance / 2), y1 - round(distance / 2))

        coordinates1 = [coordinate1, coordinate2]

        for value in coordinates1:
            if value not in graph.edges.keys():
                coordinates1_is_in_graph = False

        coordinate3 = (x1 - round(distance / 2), y1 + round(distance / 2))
        coordinate4 = (x1 + round(distance / 2), y1 + round(distance / 2))

        coordinates2 = [coordinate3, coordinate4]

        for value in coordinates2:
            if value not in graph.edges.keys():
                coordinates2_is_in_graph = False

        coordinate5 = (x2 - round(distance / 2), y2 - round(distance / 2))
        coordinate6 = (x2 + round(distance / 2), y2 - round(distance / 2))

        coordinates3 = [coordinate5, coordinate6]

        for value in coordinates3:
            if value not in graph.edges.keys():
                coordinates3_is_in_graph = False

        coordinate7 = (x2 - round(distance / 2), y2 + round(distance / 2))
        coordinate8 = (x2 + round(distance / 2), y2 + round(distance / 2))

        coordinates4 = [coordinate7, coordinate8]

        for value in coordinates4:
            if value not in graph.edges.keys():
                coordinates4_is_in_graph = False

        if coordinates1_is_in_graph or coordinates2_is_in_graph or coordinates3_is_in_graph or coordinates4_is_in_graph:
            angles_coordinates2.append(angle_coordinates)

        coordinates1_is_in_graph = True
        coordinates2_is_in_graph = True
        coordinates3_is_in_graph = True
        coordinates4_is_in_graph = True

    angles_coordinates = angles_coordinates2

    return angles_coordinates


def find_near_points_alongside_axis(coordinate1, coordinate2, coordinates_list):
    coordinate1 = coordinate1
    coordinate2 = coordinate2
    coordinates_list = coordinates_list
    
    coordinates_list2 = []
    for value in coordinates_list:
        if value != coordinate1 and value != coordinate2:
            coordinates_list2.append(value)

    distances = []
    for value in coordinates_list2:
        (x1, y1) = value[0]
        (x2, y2) = value[1]
        distance = math.sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)
        distances.append(distance)

    distances_sum = 0
    average_distance = 0
    for value in distances:
        distances_sum += value
    average_distance = round(distances_sum / len(distances))

    coordinates_list3 = []
    for value in coordinates_list2:
        coordinates_list3.append(value[0])
        coordinates_list3.append(value[1])

    min_x = math.inf
    max_x = 0
    for value in coordinates_list3:
        (x, y) = value
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x

    (x1, y1) = coordinate1
    (x2, y2) = coordinate2
    coordinates = []

    if abs(x1 - min_x) < abs(max_x - x1):
        coordinates =   [
                            (x1 - average_distance, y1),
                            (x1, y1),
                            (x2, y2),
                            (x2 - average_distance, y2),
                        ]
    
    if abs(x1 - min_x) > abs(max_x - x1):
        coordinates =   [
                            (x1, y1),
                            (x1 + average_distance, y1),
                            (x2 + average_distance, y2),
                            (x2, y2) 
                        ]

    (x1, y1) = coordinates[0]
    (x2, y2) = coordinates[1]
    (x3, y3) = coordinates[2]
    (x4, y4) = coordinates[3]

    near_points = [(x1, y1), (x3, y3)]

    return near_points


def rectangle_to_letter_comparison(rectangle, letter_complete_graph):
    rectangle = rectangle
    letter_complete_graph = letter_complete_graph
    
    are_similar = False
    number_of_sides_length = len(rectangle.sides_length)
    i = 0
    while not are_similar and i < number_of_sides_length:
        are_similar = check_similarity_of_complete_graphs2(rectangle.sides_length[i], letter_complete_graph)
        i += 1

    return are_similar


def rectangle_to_letter_comparisons(sides_length, letter_complete_graph):
    sides_length = sides_length
    letter_complete_graph = letter_complete_graph
    
    are_similar = False
    number_of_sides_length = len(sides_length)

    i = 0
    while not are_similar and i < number_of_sides_length:
        are_similar = check_similarity_of_complete_graphs2(sides_length[i], letter_complete_graph)
        i += 1

    return are_similar


async def rectangle_to_letter_comparisons_async(sides_length, letter_complete_graph):
    sides_length = sides_length
    letter_complete_graph = letter_complete_graph
    
    are_similar = False
    number_of_sides_length = len(sides_length)

    i = 0
    while not are_similar and i < number_of_sides_length:
        are_similar = check_similarity_of_complete_graphs2(sides_length[i], letter_complete_graph)
        i += 1

    return are_similar


def cut_from_img(img_to_cut_from, angles_coordinates, img):
    img_to_cut_from = img_to_cut_from
    angles_coordinates = angles_coordinates
    img = img

    coordinates_to_cut = find_coordinates_to_cut(angles_coordinates, img)
    (min_x, min_y) = coordinates_to_cut[1]

    modified_img = img_to_cut_from[(coordinates_to_cut[1][1])-10:(coordinates_to_cut[3][1]+10),
                                (coordinates_to_cut[1][0])-10:(coordinates_to_cut[3][0]+10)]

    max_modified_img_shape = modified_img.shape[0]
    
    if modified_img.shape[1] > max_modified_img_shape:
        max_modified_img_shape = modified_img.shape[1]

    modified_img_shape = max_modified_img_shape
    modified_img = numpy.zeros((modified_img_shape, modified_img_shape, 3), numpy.uint8)
    
    coordinate1 = (coordinates_to_cut[3][1]+10) - (coordinates_to_cut[1][1]-10)
    coordinate2 = (coordinates_to_cut[3][0]+10) - (coordinates_to_cut[1][0]-10)

    img_to_cut = img_to_cut_from[(coordinates_to_cut[1][1])-10:(coordinates_to_cut[3][1]+10),
                            (coordinates_to_cut[1][0])-10:(coordinates_to_cut[3][0]+10)]

    modified_img[0:coordinate1, 0:coordinate2] = img_to_cut

    return [modified_img, (min_x, min_y)]


def sort_angles_coordinates_of_triangle(angles_coordinates, img):
    angles_coordinates = angles_coordinates
    sorted_angles_coordinates = []

    min_x = img.shape[0]
    max_x = 0
    min_y = img.shape[1]
    for value in angles_coordinates:
        (x, y) = value
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y

    for value in angles_coordinates:
        (x, y) = value
        if x == min_x:
            sorted_angles_coordinates.append(value)
    
    for value in angles_coordinates:
        (x, y) = value
        if x == max_x:
            sorted_angles_coordinates.append(value)
    
    for value in angles_coordinates:
        (x, y) = value
        if y == min_y:
            sorted_angles_coordinates.append(value)

    return sorted_angles_coordinates






def find_corners_coordinates_of_triangle(angles_coordinates, angle_value):
    angles_coordinates = angles_coordinates
    angle_value = angle_value

    coordinates = []
    coordinates_list = []
    angle_value_singleton = [angle_value]
    angles_coordinates1 = angles_coordinates[0]
    angles_coordinates2 = angles_coordinates[1]

    near_points = find_near_points(angles_coordinates1, angles_coordinates2)

    for value in near_points:

        (x1, y1) = value[0]
        (x2, y2) = value[1]
        
        min_x = math.inf
        min_y = math.inf
        max_x = 0
        max_y = 0

        for value in [x1, x2]:
            if value < min_x:
                min_x = value
        
        for value in [x1, x2]:
            if value > max_x:
                max_x = value

        for value in [y1, y2]:
            if value < min_y:
                min_y = value

        for value in [y1, y2]:
            if value > max_y:
                max_y = value

        corner_height = abs(y2 - y1)
        corner_side = float()

        if min_x == x2:
            corner_side = corner_height / math.sin(math.radians(angle_value)) * math.sin(math.radians(90 - angle_value))
            corner_side = round(corner_side)
        
        if min_x == x1:
            corner_side = corner_height / math.sin(math.radians(angle_value)) * math.sin(math.radians(90 - angle_value))
            corner_side = round(corner_side)
        
        if min_y == y1:
            corner_side = (corner_height/2) / math.sin(math.radians(90 - angle_value/2)) * math.sin(math.radians(angle_value/2))
            corner_side = round(corner_side)

        diagonale_coordinate1 = tuple()
        diagonale_coordinate2 = tuple()

        if min_x == x2:
            diagonale_coordinate1 = (x2 + corner_side, y1)
            diagonale_coordinate2 = (x1 - corner_side, y2)

        if min_x == x1:
            diagonale_coordinate1 = (x1 + corner_side, y2)
            diagonale_coordinate2 = (x2 - corner_side, y1)
        
        if min_y == y1:
            diagonale_coordinate1 = (x1 - corner_side, y1 + round(corner_height / 2))
            diagonale_coordinate2 = (x1 + corner_side, y1 + round(corner_height / 2))

        coordinates1 = [diagonale_coordinate1, diagonale_coordinate2]
        coordinates_list.append(coordinates1)

    coordinates.append(coordinates_list)
    coordinates.append(angle_value_singleton)

    return coordinates


def sort_corners_coordinates_of_triangle(coordinates):
    coordinates = coordinates
    coordinates_list = coordinates[0]
    angle_value_singleton = coordinates[1]
    angle_value = angle_value_singleton[0]
    coordinates_list2 = []

    for value in coordinates_list:

        (x1, y1) = value[0]
        (x2, y2) = value[1]

        width_coordinates = (x1, x2)
        height_coordinates = (y1, y2)

        min_x = math.inf
        max_x = 0
        min_y = math.inf
        max_y = 0

        for value in width_coordinates:
            if value < min_x:
                min_x = value
        
        for value in width_coordinates:
            if value > max_x:
                max_x = value

        for value in height_coordinates:
            if value < min_y:
                min_y = value
        
        for value in height_coordinates:
            if value > max_y:
                max_y = value

        coordinate1 = (min_x, min_y)
        coordinate2 = (max_x, max_y)

        coordinates = [coordinate1, coordinate2]
        coordinates_list2.append(coordinates)

    coordinates = []

    coordinates.append(coordinates_list2)
    coordinates.append(angle_value_singleton)

    return coordinates


def cut_triangle_carcass_angle1(coordinates, img):
    coordinates = coordinates
    img = img

    coordinates1_angle_index = None
    coordinates2_angle_index = None
    coordinates3_angle_index = None

    coordinates_list = coordinates[0]
    angle_value_singleton = coordinates[1]
    angle_value = angle_value_singleton[0]

    min_value = math.inf

    for coordinates in coordinates_list:

        (x1, y1) = coordinates[0]
        (x2, y2) = coordinates[1]

        if x1 < min_value:
            min_value = x1
        
        if x2 < min_value:
            min_value = x2

    max_value = -math.inf

    for coordinates in coordinates_list:

        (x1, y1) = coordinates[0]
        (x2, y2) = coordinates[1]

        if x1 > max_value:
            max_value = x1
        
        if x2 > max_value:
            max_value = x2

    coordinates1 = coordinates_list[0]
    coordinates2 = coordinates_list[1]
    coordinates3 = coordinates_list[2]


    (x1, y1) = coordinates1[0]
    (x2, y2) = coordinates1[1]

    if min_value in (x1, y1):
        coordinates1_angle_index = 0

    if min_value in (x2, y2):
        coordinates1_angle_index = 0
    
    if max_value in (x1, y1):
        coordinates1_angle_index = 1

    if max_value in (x2, y2):
        coordinates1_angle_index = 1


    (x1, y1) = coordinates2[0]
    (x2, y2) = coordinates2[1]

    if min_value in (x1, y1):
        coordinates2_angle_index = 0

    if min_value in (x2, y2):
        coordinates2_angle_index = 0

    if max_value in (x1, y1):
        coordinates2_angle_index = 1

    if max_value in (x2, y2):
        coordinates2_angle_index = 1


    (x1, y1) = coordinates3[0]
    (x2, y2) = coordinates3[1]

    if min_value in (x1, y1):
        coordinates3_angle_index = 0

    if min_value in (x2, y2):
        coordinates3_angle_index = 0

    if max_value in (x1, y1):
        coordinates3_angle_index = 1

    if max_value in (x2, y2):
        coordinates3_angle_index = 1


    coordinates_angle_indexes = [
                                    [coordinates1_angle_index, coordinates1],
                                    [coordinates2_angle_index, coordinates2],
                                    [coordinates3_angle_index, coordinates3]
                                ]
    
    coordinates_angle_indexes_copy = []


    for value in coordinates_angle_indexes:
        if isinstance(value[0], int):
            coordinates_angle_indexes_copy.append(value)

    coordinates_angle_indexes = coordinates_angle_indexes_copy


    for d in range(2):
        
        if coordinates_angle_indexes[d][0] == 0:

            coordinates = coordinates_angle_indexes[d][1]
            
            (x1, y1) = coordinates[0]
            (x2, y2) = coordinates[1]

            corner_height = abs(y2 - y1)
            corner_side = corner_height / math.sin(math.radians(angle_value)) * math.sin(math.radians(90 - angle_value))
            corner_side = round(corner_side)

            coordinate1 = (x1 - corner_side, y2)
            coordinate2 = (x1, y1)
            coordinate3 = (x2 + corner_side, y1)
            coordinate4 = (x2, y2)

            (x1, y1) = coordinate1
            (x2, y2) = coordinate2
            (x3, y3) = coordinate3
            (x4, y4) = coordinate4
            
            width_koeff = 1
            height_koeff = 1

            width_koeff, height_koeff = get_koefficients(angle_value)

            height = corner_height
            padding_koeff = round(corner_height / 7)
            x_step = 1
            y_step = 2
            w_k = width_koeff
            h_k = height_koeff
            p_k = padding_koeff

            for p in range(0, height + 1, x_step):
                for i in range(x2 - round(p/w_k) - p_k, x3 - round(p/w_k) + 1):
                    for j in range(y2 + p*h_k, y2 + p*h_k + y_step + 1):
                        img[j, i] = [255, 255, 255]


        if coordinates_angle_indexes[d][0] == 1:

            coordinates = coordinates_angle_indexes[d][1]
            
            (x1, y1) = coordinates[0]
            (x2, y2) = coordinates[1]

            corner_height = abs(y2 - y1)
            corner_side = corner_height / math.sin(math.radians(angle_value)) * math.sin(math.radians(90 - angle_value))
            corner_side = round(corner_side)

            coordinate1 = (x1 - corner_side, y1)
            coordinate2 = (x2, y1)
            coordinate3 = (x2 + corner_side, y2)
            coordinate4 = (x1, y2)

            (x1, y1) = coordinate1
            (x2, y2) = coordinate2
            (x3, y3) = coordinate3
            (x4, y4) = coordinate4

            width_koeff = 1
            height_koeff = 1

            width_koeff, height_koeff = get_koefficients(angle_value)

            height = corner_height
            padding_koeff = round(corner_height / 7)
            x_step = 1
            y_step = 2
            w_k = width_koeff
            h_k = height_koeff
            p_k = padding_koeff

            for p in range(0, height + 1, x_step):
                for i in range(x1 + round(p/w_k), x2 + round(p/w_k) + p_k + 1):
                    for j in range(y1 + p*h_k, y1 + p*h_k + y_step + 1):
                        img[j, i] = [255, 255, 255]


    return img


def cut_triangle_carcass_angle2(coordinates, img):
    coordinates = coordinates
    img = img

    coordinates1_angle_index = None
    coordinates2_angle_index = None
    coordinates3_angle_index = None

    coordinates_list = coordinates[0]
    angle_value_singleton = coordinates[1]
    angle_value = angle_value_singleton[0]

    min_value = math.inf

    for coordinates in coordinates_list:

        (x1, y1) = coordinates[0]
        (x2, y2) = coordinates[1]

        if y1 < min_value:
            min_value = y1
        
        if y2 < min_value:
            min_value = y2

    coordinates1 = coordinates_list[0]
    coordinates2 = coordinates_list[1]
    coordinates3 = coordinates_list[2]


    (x1, y1) = coordinates1[0]
    (x2, y2) = coordinates1[1]
    
    if min_value in (x1, y1):
        coordinates1_angle_index = 2

    if min_value in (x2, y2):
        coordinates1_angle_index = 2


    (x1, y1) = coordinates2[0]
    (x2, y2) = coordinates2[1]

    if min_value in (x1, y1):
        coordinates2_angle_index = 2

    if min_value in (x2, y2):
        coordinates2_angle_index = 2


    (x1, y1) = coordinates3[0]
    (x2, y2) = coordinates3[1]

    if min_value in (x1, y1):
        coordinates3_angle_index = 2

    if min_value in (x2, y2):
        coordinates3_angle_index = 2


    coordinates_angle_indexes = [
                                    [coordinates1_angle_index, coordinates1],
                                    [coordinates2_angle_index, coordinates2],
                                    [coordinates3_angle_index, coordinates3]
                                ]

    coordinates_angle_indexes_copy = []

    for value in coordinates_angle_indexes:
        if isinstance(value[0], int):
            coordinates_angle_indexes_copy.append(value)

    coordinates_angle_indexes = coordinates_angle_indexes_copy

    coordinates = coordinates_angle_indexes[0][1]


    (x1, y1) = coordinates[0]
    (x2, y2) = coordinates[1]

    corner_side = abs(x2 - x1) / 2
    corner_side = round(corner_side)
    corner_height = corner_side / math.sin(math.radians(angle_value/2)) *  math.sin(math.radians(90 - angle_value/2)) * 2

    coordinate1 = (x1 + corner_side, y1 + round(corner_height / 2))
    coordinate2 = (x1, y1)
    coordinate3 = (x1 + corner_side, y1 - round(corner_height / 2))
    coordinate4 = (x2, y2)

    (x1, y1) = coordinate1
    (x2, y2) = coordinate2
    (x3, y3) = coordinate3
    (x4, y4) = coordinate4

    width_koeff = 1
    height_koeff = 1

    width_koeff, height_koeff = get_koefficients(angle_value)
    
    height = corner_height
    x_step = 1
    y_step = 2
    w_k = width_koeff
    h_k = height_koeff
    
    for p in range(0, round(height/2) + 3, x_step):
        for i in range(round((x2 + x4) / 2) - round(p/w_k), round((x2 + x4) / 2) + round(p/w_k) + 4):
            for j in range(y3 + p*h_k - 2, y3 + p*h_k + y_step + 1):
                img[j, i] = [255, 255, 255]

    for p in range(round(height/2) + 2, 0, -x_step):
        for i in range(round((x2 + x4) / 2) - round(p/w_k), round((x2 + x4) / 2) + round(p/w_k) + 4):
            for j in range(y1 - p*h_k + 2, y1 - p*h_k - y_step - 1, -1):
                img[j, i] = [255, 255, 255]

    return img


def get_koefficients(angle_value):
        angle_value = angle_value

        angles_ratio = round((90 - angle_value) / angle_value, 1)

        angles_ratios = [
                            (2, 1),
                            (3, 1),
                            (4, 1)
                        ]

        for value in angles_ratios:
            if round(1 / angles_ratio) == value[0]:
                width_koeff = value[0]
                height_koeff = value[1]

        return width_koeff, height_koeff


def find_corners_coordinates_of_rectangle(angles_coordinates):
    angles_coordinates = angles_coordinates

    coordinates = []
    angles_coordinates1 = angles_coordinates[0]
    angles_coordinates2 = angles_coordinates[1]

    near_points = find_near_points(angles_coordinates1, angles_coordinates2)

    coordinates = near_points

    return coordinates


def find_corners_coordinates_of_rectangle2(angles_coordinates):
    angles_coordinates = angles_coordinates
    coordinates = []

    angles_coordinates1 = angles_coordinates[0]
    angles_coordinates2 = angles_coordinates[1]

    near_points1 = find_near_points(angles_coordinates1, angles_coordinates2)
    near_points2 = find_near_points2(angles_coordinates2)

    near_points = []
    near_points.extend(near_points1)
    near_points.extend(near_points2)

    near_points2 = []

    for value in near_points:
        coordinates = value
        are_correct = False

        while not are_correct:
            are_correct = check_corner_coordinates(coordinates)

            if not are_correct:

                coordinates = additional_corners_coordinates_of_rectangle_search(coordinates, near_points)

        near_points2.append(coordinates)

    coordinates = near_points2

    return coordinates


def find_corners_coordinates(angles_coordinates, graph):
    angles_coordinates = angles_coordinates
    graph = graph
    coordinates = []

    near_points = find_near_points_pairs(angles_coordinates)

    filtered_near_points = filter_edge_corners(near_points, graph)

    near_points2 = []

    for value in filtered_near_points:
        coordinates = value
        are_correct = False

        while not are_correct:
            are_correct = check_corner_coordinates(coordinates)

            if not are_correct:

                coordinates = additional_corners_coordinates_of_rectangle_search(coordinates, near_points)

        near_points2.append(coordinates)

    coordinates = near_points2

    return coordinates


def sort_corners_coordinates_of_rectangle(coordinates):
    coordinates = coordinates

    coordinates_list = coordinates
    coordinates_list2 = []

    for value in coordinates_list:
    
        (x1, y1) = value[0]
        (x2, y2) = value[1]
        
        width_coordinates = [x1, x2]
        height_coordinates = [y1, y2]
        
        min_x = math.inf
        max_x = 0
        min_y = math.inf
        max_y = 0

        for value in width_coordinates:
            if value < min_x:
                min_x = value
        
        for value in width_coordinates:
            if value > max_x:
                max_x = value

        for value in height_coordinates:
            if value < min_y:
                min_y = value
        
        for value in height_coordinates:
            if value > max_y:
                max_y = value

        coordinate1 = (min_x, min_y)
        coordinate2 = (max_x, max_y)

        coordinates = [coordinate1, coordinate2]
        coordinates_list2.append(coordinates)

    coordinates_list = coordinates_list2
    coordinates = coordinates_list
    
    return coordinates


def cut_rectangle_carcass_angle(coordinates, img):
    coordinates = coordinates
    img = img

    (x1, y1) = coordinates[0]
    (x2, y2) = coordinates[1]

    for i in range(x1 - 3, x2 + 4):
        for j in range(y1 - 3, y2 + 4):
            img[j, i] = [255, 255, 255]

    return img


def cut_rectangle_corners(coordinates, img):
    coordinates = coordinates
    img = img
    
    for i in range(len(coordinates)):
        img = cut_rectangle_carcass_angle(coordinates[i], img)

    return img


def cut_corners(coordinates, img):
    coordinates = coordinates
    img = img

    for i in range(len(coordinates)):
        img = cut_rectangle_carcass_angle(coordinates[i], img)

    return img


def check_corner_coordinates(coordinates):
    coordinates = coordinates
    are_correct = True

    coordinate1 = coordinates[0]
    coordinate2 = coordinates[1]

    (x1, y1) = coordinate1
    (x2, y2) = coordinate2

    if x1 == x2:
        are_correct = False

    if y1 == y2:
        are_correct = False

    return are_correct


def additional_corners_coordinates_of_rectangle_search(coordinates, coordinates_list):
    coordinates = coordinates
    coordinates_list = coordinates_list

    coordinate1 = coordinates[0]
    coordinate2 = coordinates[1]

    near_points = find_near_points_alongside_axis(coordinate1, coordinate2, coordinates_list)

    coordinates = near_points

    return coordinates
