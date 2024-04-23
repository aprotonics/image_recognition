import os
import importlib
import cv2


class Loader():
    def __init__(self):
        current_dir = os.path.curdir
        dir_to_create = current_dir + "/__cache__"
        if not os.path.exists(dir_to_create):
            os.mkdir(os.path.abspath(dir_to_create))
    
    def load_module(self, module_name, file_path):
        module_name = module_name
        file_path = file_path

        file = file_path
        file2 = "__cache__/" + f"__{module_name}__"
        text = ""

        with open(file=file, mode="rt", encoding="utf-8") as f:
            text = f.read()
        
        if text.find(" from") != -1:
            left_index = text.find(" from") + len("from") + 1
            right_index = text.find("import", left_index) - 1
            module_name_to_fix = text[left_index:right_index]

            old_value = module_name_to_fix
            new_value = f"__{module_name_to_fix}__"
            text = text.replace(old_value, new_value)

        file2 += ".py"

        with open(file=file2, mode="wt", encoding="utf-8") as f:
            f.write(text)
        
        importlib.invalidate_caches()
        loaded_module = importlib.import_module(f"__cache__.__{module_name}__")

        return loaded_module


def create_file_object(file_name, par_dir, path):
    file_name = file_name
    par_dir = par_dir
    path = path
    
    for i in range(3):
        path = os.path.dirname(path)
    file_path = path + "/" + par_dir + "/" + file_name + ".py"
    loader = Loader()
    file_object = loader.load_module(file_name, file_path)

    return file_object


file_name = "structures"
par_dir = "utils"
path = __file__
structures = create_file_object(file_name, par_dir, path)
squareGrid = structures.SquareGrid
rectangularGrid = structures.RectangularGrid

file_name = "breadth_first_search"
par_dir = "utils"
path = __file__
breadth_first_search = create_file_object(file_name, par_dir, path)
breadth_first_search2 = breadth_first_search.breadth_first_search2

file_name = "connected_components_count"
par_dir = "utils"
path = __file__
connected_components_count = create_file_object(file_name, par_dir, path)
connected_components_count = connected_components_count.connected_components_count

file_name = "utils"
par_dir = "utils"
path = __file__
utils = create_file_object(file_name, par_dir, path)
modify_shape = utils.modify_shape
create_graph = utils.create_graph
find_outer_angles_coordinates = utils.find_outer_angles_coordinates
count_length_of_sides_of_triangle = utils.count_length_of_sides_of_triangle
count_value_of_angles_in_triangle = utils.count_value_of_angles_in_triangle
modify_src = utils.modify_src
cut_from_img = utils.cut_from_img
find_near_points = utils.find_near_points
find_corners_coordinates_of_rectangle = utils.find_corners_coordinates_of_rectangle
find_corners_coordinates_of_rectangle2 = utils.find_corners_coordinates_of_rectangle2
sort_corners_coordinates_of_rectangle = utils.sort_corners_coordinates_of_rectangle
cut_rectangle_corners = utils.cut_rectangle_corners

file_name = "utils_os"
par_dir = "utils_os"
path = __file__
utils_os = create_file_object(file_name, par_dir, path)
create_dir = utils_os.create_dir
delete_dir = utils_os.delete_dir

file_name = "console_log"
par_dir = "utils_functions"
path = __file__
console_log = create_file_object(file_name, par_dir, path)
console_log = console_log.console_log

file_name = "get_length"
par_dir = "utils_functions"
path = __file__
get_length = create_file_object(file_name, par_dir, path)
length = get_length.length

file_name = "get_maximum"
par_dir = "utils_functions"
path = __file__
get_maximum = create_file_object(file_name, par_dir, path)
get_maximum = get_maximum.get_maximum

file_name = "push"
par_dir = "utils_functions"
path = __file__
push = create_file_object(file_name, par_dir, path)
push = push.push


current_dir = os.path.curdir
dir_to_create = current_dir + "/data/cache"
create_dir(dir_to_create)


img_name = "data/rectangle2.jpg"
img = cv2.imread(img_name, 1)

quality = 95

if img.shape[1] > img.shape[0]:
    img = modify_shape(img)

console_log(img.shape)
console_log()

width = img.shape[0]
height = img.shape[1]
height_to_width_ratio = (3, 2)

grid = squareGrid(width, height)
grid_center = (int(width / 2), int(height / 2))

rectangle_area = breadth_first_search2(grid, grid_center, img, quality)
console_log(length(rectangle_area))
console_log()

graph1 = create_graph(rectangle_area)
console_log(length(graph1.edges.keys()))
console_log()


angles_coordinates1 = []
for i in range(2, 6):
    angles_coordinates1 = push(find_outer_angles_coordinates(graph1, 4, i, img, quality), angles_coordinates1)

graph1.angles_coordinates1 = []
graph1.angles_coordinates1 = angles_coordinates1[-1]


modified_img = modify_src(img)
cv2.imwrite("data/modified_rectangle2.jpg", modified_img)

[modified_img, (min_x, min_y)] = cut_from_img(modified_img, graph1.angles_coordinates1, img)


width = modified_img.shape[0]
height = modified_img.shape[1]
height_to_width_ratio = (3, 2)

grid = squareGrid(width, height)
grid_center = (int(width / 2), int(height / 2))

rectangle_area = breadth_first_search2(grid, grid_center, modified_img, quality)
console_log(length(rectangle_area))
console_log()

graph = create_graph(rectangle_area)
console_log(length(graph.edges.keys()))
console_log()

isolated_subgraphs_count, rectangle_areas_list = connected_components_count(graph)


graphs_list = []

for i in range(2):
    rectangle_area = rectangle_areas_list[i]
    graph = create_graph(rectangle_area)
    graphs_list = push(graph, graphs_list)

graph1.angles_coordinates2 = []

for graph in graphs_list:

    angles_coordinates2 = []
    for i in range(2, 6):
        angles_coordinates2_2 = []

        middle_coordinates = find_outer_angles_coordinates(graph, 4, i, modified_img, quality)

        for value in middle_coordinates:
            (x, y) = value
            angles_coordinates2_2 = push((x + min_x - 10, y + min_y - 10), angles_coordinates2_2)

        angles_coordinates2 = push(angles_coordinates2_2, angles_coordinates2)

    if length(angles_coordinates2[-1]) > 0:    
        graph1.angles_coordinates2.extend(angles_coordinates2[-1])


angles_coordinates1 = graph1.angles_coordinates1
angles_coordinates2 = graph1.angles_coordinates2

angles_coordinates = [angles_coordinates1, angles_coordinates2]




coordinates = find_corners_coordinates_of_rectangle2(angles_coordinates)

console_log()
for value in coordinates:
    console_log(value)

coordinates = sort_corners_coordinates_of_rectangle(coordinates)

console_log()
for value in coordinates:
    console_log(value)

console_log()
console_log()

img = cut_rectangle_corners(coordinates, img)

cv2.imwrite("data/cache/modified_img.jpg", img)


img_name = "data/cache/modified_img.jpg"
img = cv2.imread(img_name)

width = img.shape[0]
height = img.shape[1]
height_to_width_ratio = (3, 2)

grid = squareGrid(width, height)
grid_center = (int(width / 2), int(height / 2))

rectangle_area = breadth_first_search2(grid, grid_center, img, quality)
graph = create_graph(rectangle_area)
isolated_subgraphs_count, rectangles_areas_list = connected_components_count(graph)

console_log(isolated_subgraphs_count)


current_dir = os.path.curdir
dir_to_delete = current_dir + "/data/cache"
delete_dir(dir_to_delete)
