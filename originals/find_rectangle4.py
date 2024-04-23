import os
import importlib
import cv2
import numpy


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
breadth_first_search4 = breadth_first_search.breadth_first_search4
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
create_graph = utils.create_graph
create_rectangular_graph = utils.create_rectangular_graph
count_length_of_sides_of_rectangle = utils.count_length_of_sides_of_rectangle
count_value_of_angles_in_rectangle = utils.count_value_of_angles_in_rectangle
find_angles_coordinates = utils.find_angles_coordinates
find_outer_angles_coordinates = utils.find_outer_angles_coordinates
find_inner_angles_coordinates = utils.find_inner_angles_coordinates
find_coordinates_to_cut = utils.find_coordinates_to_cut
modify_src = utils.modify_src

file_name = "graph_isomorphism"
par_dir = "graphs_isomorphism"
path = __file__
graph_isomorphism = create_file_object(file_name, par_dir, path)
get_graph_result = graph_isomorphism.get_graph_result
compare_graphs = graph_isomorphism.compare_graphs

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


img_name = "data/original4.jpg"
output = "output/find_rectangle4.txt"

img = cv2.imread(img_name)

quality = 95                 # %

with open(file=output, mode="at", encoding="utf-8") as f:
    f.write(str(img.shape))
    f.write("\n")
    f.write("\n")

console_log(img.shape)

width = img.shape[0]
height = img.shape[1]
height_to_width_ratio = (3, 2)

grid = squareGrid(width, height)
grid_center = (int(width / 2), int(height / 2))

rectangle_area = breadth_first_search2(grid, grid_center, img, quality)

with open(file=output, mode="at", encoding="utf-8") as f:
    f.write(str(length(rectangle_area)))
    f.write("\n")
    f.write("\n")

graph1 = create_graph(rectangle_area)

with open(file=output, mode="at", encoding="utf-8") as f:
    f.write(str(length(graph1.edges.keys())))
    f.write("\n")

angles_coordinates1 = []
for i in range(2, 6):
    with open(file=output, mode="at", encoding="utf-8") as f:
        f.write(str(f"Iterations: {i}"))
        f.write("\n")

    angles_coordinates1 = push(find_outer_angles_coordinates(graph1, 8, i, img, quality), angles_coordinates1)

with open(file=output, mode="at", encoding="utf-8") as f:
    f.write(str("angles coordinates"))
    f.write("\n")

graph1.angles_coordinates = []
graph1.angles_coordinates = angles_coordinates1[-1]

for angles_coordinates in angles_coordinates1:
    with open(file=output, mode="at", encoding="utf-8") as f:
        f.write(str(angles_coordinates))
        f.write("\n")
        f.write("\n")


modified_img = modify_src(img)
cv2.imwrite("data/modified_original4.jpg", modified_img)

coordinates_to_cut = find_coordinates_to_cut(graph1.angles_coordinates, img)
(min_x, min_y) = coordinates_to_cut[1]

modified_img1 = modified_img[(coordinates_to_cut[1][1])-10:(coordinates_to_cut[3][1]+10),
                            (coordinates_to_cut[1][0])-10:(coordinates_to_cut[3][0]+10)]

modified_img1_shape = get_maximum(modified_img1.shape[0], modified_img1.shape[1])
modified_img1 = numpy.zeros((modified_img1_shape, modified_img1_shape, 3), numpy.uint8)

coordinate1 = (coordinates_to_cut[3][1]+10) - (coordinates_to_cut[1][1]-10)
coordinate2 = (coordinates_to_cut[3][0]+10) - (coordinates_to_cut[1][0]-10)

img_to_cut = modified_img[(coordinates_to_cut[1][1])-10:(coordinates_to_cut[3][1]+10),
                        (coordinates_to_cut[1][0])-10:(coordinates_to_cut[3][0]+10)]

modified_img1[0:coordinate1, 0:coordinate2] = img_to_cut

cv2.imwrite("data/modified.jpg", modified_img1)

modified_img = modified_img1

with open(file=output, mode="at", encoding="utf-8") as f:
    f.write(str(modified_img.shape))
    f.write("\n")
    f.write("\n")

width = modified_img.shape[0]
height = modified_img.shape[1]
height_to_width_ratio = (3, 2)

grid = squareGrid(width, height)
grid_center = (int(width / 2), int(height / 2))

rectangle_area = breadth_first_search2(grid, grid_center, modified_img, quality)

with open(file=output, mode="at", encoding="utf-8") as f:
    f.write(str(length(rectangle_area)))
    f.write("\n")
    f.write("\n")

graph = create_graph(rectangle_area)

with open(file=output, mode="at", encoding="utf-8") as f:
    f.write(str(length(graph.edges.keys())))
    f.write("\n")

angles_coordinates2 = []
for i in range(2, 6):
    angles_coordinates2_2 = []

    with open(file=output, mode="at", encoding="utf-8") as f:
        f.write(str(f"Iterations: {i}"))
        f.write("\n")

    middle_coordinates = find_outer_angles_coordinates(graph, 4, i, modified_img, quality)
    for value in middle_coordinates:
        (x, y) = value
        angles_coordinates2_2 = push((x + min_x - 10, y + min_y - 10), angles_coordinates2_2)

    angles_coordinates2 = push(angles_coordinates2_2, angles_coordinates2)

graph1.angles_coordinates.extend(angles_coordinates2[-1])

with open(file=output, mode="at", encoding="utf-8") as f:
    f.write(str("angles coordinates"))
    f.write("\n")

for angles_coordinates in angles_coordinates2:
    with open(file=output, mode="at", encoding="utf-8") as f:
        f.write(str(angles_coordinates))
        f.write("\n")
        f.write("\n")

