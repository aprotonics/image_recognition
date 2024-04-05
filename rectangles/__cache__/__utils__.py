import math
import itertools
import numpy


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

def check_similarity_of_triangles(graph1, graph2):
    graph1 = graph1
    graph2 = graph2
    
    are_similar = None
    koeff1 = round(graph1.sides_length[0] / graph2.sides_length[0], 2)
    koeff2 = round(graph1.sides_length[1] / graph2.sides_length[1], 2)
    koeff3 = round(graph1.sides_length[2] / graph2.sides_length[2], 2)

    if koeff1 == koeff2 == koeff3:
        are_similar = True
        print(koeff1)
    else:
        are_similar = False
        print(koeff1, koeff2, koeff3)

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
        print(koeff1)
    else:
        are_similar = False
        print(koeff1, koeff2, koeff3, koeff4)

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
        print("side lenghts differ")
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
            print(koeffs)
            return are_similar

    print(koeffs)
    return are_similar

def check_similarity_of_complete_graphs2(sides_length1, sides_length2):
    sides_length1 = sides_length1
    sides_length2 = sides_length2

    are_similar = True
    koeffs = []
    quad_diff = 0.1

    if abs(len(sides_length1) - len(sides_length2)) > 0:
        are_similar = False
        print("side lenghts differ")
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
            print(koeffs)
            return are_similar

    print(koeffs)
    return are_similar

def rectangle_to_letter_comparison(rectangle, letter_complete_graph):
    rectangle = rectangle
    letter_complete_graph = letter_complete_graph
    
    are_similar = False
    number_of_sides_length = len(rectangle.sides_length)
    i = 0
    while not are_similar and i < number_of_sides_length:
        are_similar = check_similarity_of_complete_graphs2(rectangle.sides_length[i], letter_complete_graph)
        i += 1

    print(number_of_sides_length)
    print(i)
    if number_of_sides_length == i:
        print(are_similar)
    print()

    return are_similar

def count_value_of_angles_in_similar_triangle(graph1):
    graph1 = graph1

    values_of_angles_in_similar_triangle = graph1.values_of_angles

    return values_of_angles_in_similar_triangle

def find_coordinates_of_angles_in_triangle(graph):
    graph = graph
    angles_coordinates = []

    # find points with one neighbor
    points_with_one_neighbor = []

    for key, values in graph.edges.items():
        if len(values) == 1:
            points_with_one_neighbor.append(key)
        
        if len(points_with_one_neighbor) == 3:
            break

    angles_coordinates.extend(points_with_one_neighbor)

    print("number of pairs of angles coordinates")
    print(len(angles_coordinates))

    # find points with two neighbors
    if len(points_with_one_neighbor) < 3:
        points_with_two_neighbors = []

        for key, values in graph.edges.items():
            if len(values) == 2:

                [x, y] = key
                points_with_two_neighbors.append([x, y])
        
        point = [10, 10]

        (point[0]+1, point[1]), 
        (point[0], point[1]+1), 
        (point[0]-1, point[1]), 
        (point[0], point[1]-1), 
        (point[0]+1, point[1]+1), 
        (point[0]-1, point[1]-1), 
        (point[0]+1, point[1]-1), 
        (point[0]-1, point[1]+1), 

        for point in points_with_two_neighbors:
            point_neighbors = [
                                (point[0]+1, point[1]), 
                                (point[0], point[1]+1), 
                                (point[0]-1, point[1]), 
                                (point[0], point[1]-1), 
                                (point[0]+1, point[1]+1), 
                                (point[0]-1, point[1]-1), 
                                (point[0]+1, point[1]-1), 
                                (point[0]-1, point[1]+1), 
                            ]
            
            point.append(point_neighbors)
            point.append(0)

        point = [10, 10, point_neighbors, 0]

        for point in points_with_two_neighbors:
            for neighbor in point[2]:
                for key in graph.edges.keys():
                    if key == neighbor:
                        point[3] += 1

        # filter nonangle points
        points_with_two_neighbors2 = []
        for point in points_with_two_neighbors:
            points_with_two_neighbors2.append(point)

        for point in points_with_two_neighbors:
            if point[3] > 3: # point_neighbors_count > 3
                points_with_two_neighbors2.remove(point)

        print()
        print("number of other pairs of angles coordinates")
        print(len(points_with_two_neighbors2))
        print()

        points_with_two_neighbors = []
        for point in points_with_two_neighbors2:
            x, y, neighbors, count = point
            points_with_two_neighbors.append((x, y))

        angles_coordinates.extend(points_with_two_neighbors)

    print("total number of pairs of angles coordinates")
    print(len(angles_coordinates))
    print()

    return angles_coordinates

def find_angles_coordinates(graph, angles_number1, angles_number2, iterations, img, quality):
    graph = graph
    graph1 = []
    graph2 = []
    angles_number1 = angles_number1
    angles_number2 = angles_number2
    iterations = iterations
    img = img
    quality = quality

    angles_coordinates1 = find_outer_angles_coordinates(graph1, angles_number1, iterations, img, quality)
    angles_coordinates2 = find_outer_angles_coordinates(graph2, angles_number2, iterations, img, quality)
    angles_coordinates = [angles_coordinates1, angles_coordinates2]

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

    neighbors_out_of_border_count = 0
    neighbors_in_border_count = 0
    in_to_out_ratio = 0
    neighbors_out_of_border = []
    neighbors_in_border = []
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
                    
                    neighbors_out_of_border_count += 1
                    neighbors_out_of_border.append(next)

                if img[y, x, 0] < (100 - quality) and\
                    img[y, x, 1] < (100 - quality) and\
                    img[y, x, 2] < (100 - quality):

                    neighbors_in_border_count += 1
                    neighbors_in_border.append(next)

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
                        
                            neighbors_out_of_border_count += 1
                            neighbors_out_of_border.append(next)

                        if img[y, x, 0] < (100 - quality) and\
                            img[y, x, 1] < (100 - quality) and\
                            img[y, x, 2] < (100 - quality):

                            neighbors_in_border_count += 1
                            neighbors_in_border.append(next)

                    visited[next] = True
                    
                    frontier2.put(next)

        frontier = frontier2
    
    if neighbors_out_of_border_count > 0:
        in_to_out_ratio = neighbors_in_border_count / neighbors_out_of_border_count

    min_y = img.shape[1]
    max_y = 0
    for value in neighbors_out_of_border:
        (x, y) = value
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y
    out_of_border_height = max_y - min_y

    min_y = img.shape[1]
    max_y = 0
    for value in neighbors_in_border:
        (x, y) = value
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y
    in_border_height = max_y - min_y

    min_x = img.shape[0]
    max_x = 0
    for value in neighbors_out_of_border:
        (x, y) = value
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
    out_of_border_width = max_x - min_x

    min_x = img.shape[0]
    max_x = 0
    for value in neighbors_in_border:
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
    neighbors_out_of_border_count = 0
    neighbors_in_border_count = 0
    in_to_out_ratio = 0
    neighbors_out_of_border = []
    neighbors_in_border = []
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
                    
                    neighbors_out_of_border_count += 1
                    neighbors_out_of_border.append(next)

                if img[y, x, 0] < (100 - quality) and\
                    img[y, x, 1] < (100 - quality) and\
                    img[y, x, 2] < (100 - quality):

                    neighbors_in_border_count += 1
                    neighbors_in_border.append(next)

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
                        
                            neighbors_out_of_border_count += 1
                            neighbors_out_of_border.append(next)

                        if img[y, x, 0] < (100 - quality) and\
                            img[y, x, 1] < (100 - quality) and\
                            img[y, x, 2] < (100 - quality):

                            neighbors_in_border_count += 1
                            neighbors_in_border.append(next)

                    visited[next] = True
                    frontier2.put(next)

        frontier = frontier2

    if neighbors_out_of_border_count > 0:
        in_to_out_ratio = neighbors_in_border_count / neighbors_out_of_border_count

    min_y = img.shape[1]
    max_y = 0
    for value in neighbors_out_of_border:
        (x, y) = value
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y
    out_of_border_height = max_y - min_y

    min_y = img.shape[1]
    max_y = 0
    for value in neighbors_in_border:
        (x, y) = value
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y
    in_border_height = max_y - min_y

    min_x = img.shape[0]
    max_x = 0
    for value in neighbors_out_of_border:
        (x, y) = value
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
    out_of_border_width = max_x - min_x

    min_x = img.shape[0]
    max_x = 0
    for value in neighbors_in_border:
        (x, y) = value
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
    in_border_width = max_x - min_x

    if out_of_border_height == in_border_height or out_of_border_width == in_border_width:
        in_to_out_ratio = 0

    return in_to_out_ratio

def are_near_points(start1, start2, search_radius):
    start1 = start1
    start2 = start2
    search_radius = search_radius

    (x1, y1) = start1
    (x2, y2) = start2
    distance = math.sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)
    
    return 0 < distance <= search_radius

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

def check_not_in_bounds(coordinates, img):
    (y, x) = coordinates
    width = img.shape[0]
    height = img.shape[1]

    return 0 < y < width and 0 < x < height
