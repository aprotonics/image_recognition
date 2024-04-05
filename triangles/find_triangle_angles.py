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


file_name = "structures"
par_dir = "utils"
path = __file__
for i in range(3):
    path = os.path.dirname(path)
file_path = path + "/" + par_dir + "/" + file_name + ".py"
loader = Loader()
structures = loader.load_module(file_name, file_path)

squareGrid = structures.SquareGrid
rectangularGrid = structures.RectangularGrid


file_name = "breadth_first_search"
par_dir = "utils"
path = __file__
for i in range(3):
    path = os.path.dirname(path)
file_path = path + "/" + par_dir + "/" + file_name + ".py"
loader = Loader()
breadth_first_search = loader.load_module(file_name, file_path)

breadth_first_search2 = breadth_first_search.breadth_first_search2
breadth_first_search4 = breadth_first_search.breadth_first_search4
breadth_first_search6 = breadth_first_search.breadth_first_search6


file_name = "connected_components_count"
par_dir = "utils"
path = __file__
for i in range(3):
    path = os.path.dirname(path)
file_path = path + "/" + par_dir + "/" + file_name + ".py"
loader = Loader()
connected_components_count = loader.load_module(file_name, file_path)

connected_components_count = connected_components_count.connected_components_count


file_name = "utils"
par_dir = "utils"
path = __file__
for i in range(3):
    path = os.path.dirname(path)
file_path = path + "/" + par_dir + "/" + file_name + ".py"
loader = Loader()
utils = loader.load_module(file_name, file_path)

create_triangle_area = utils.create_triangle_area
create_graph = utils.create_graph
create_rectangular_graph = utils.create_rectangular_graph
count_length_of_sides_of_triangle = utils.count_length_of_sides_of_triangle
count_value_of_angles_in_triangle = utils.count_value_of_angles_in_triangle
find_angles_coordinates = utils.find_angles_coordinates
find_inner_angles_coordinates_of_triangle = utils.find_inner_angles_coordinates_of_triangle
check_similarity_of_triangles = utils.check_similarity_of_triangles
modify_src = utils.modify_src


file_name = "graph_isomorphism"
par_dir = "graphs_isomorphism"
path = __file__
for i in range(3):
    path = os.path.dirname(path)
file_path = path + "/" + par_dir + "/" + file_name + ".py"
loader = Loader()
graph_isomorphism = loader.load_module(file_name, file_path)

get_graph_result = graph_isomorphism.get_graph_result
compare_graphs = graph_isomorphism.compare_graphs


file_name = "console_log"
par_dir = "utils_functions"
path = __file__
for i in range(3):
    path = os.path.dirname(path)
file_path = path + "/" + par_dir + "/" + file_name + ".py"
loader = Loader()
console_log = loader.load_module(file_name, file_path)

console_log = console_log.console_log


file_name = "get_length"
par_dir = "utils_functions"
path = __file__
for i in range(3):
    path = os.path.dirname(path)
file_path = path + "/" + par_dir + "/" + file_name + ".py"
loader = Loader()
get_length = loader.load_module(file_name, file_path)

length = get_length.length


file_name = "push"
par_dir = "utils_functions"
path = __file__
for i in range(3):
    path = os.path.dirname(path)
file_path = path + "/" + par_dir + "/" + file_name + ".py"
loader = Loader()
push = loader.load_module(file_name, file_path)

push = push.push


img_name = "data/modified_triangle6.jpg"
img = cv2.imread(img_name)

quality = 95                 # %

console_log(img.shape)
console_log()

width = img.shape[0]
height = img.shape[1]
height_to_width_ratio = (3, 2)

grid = rectangularGrid(width, height, height_to_width_ratio)
grid_center = (int(width / 2), int(height / 2))

triangle_area = breadth_first_search2(grid, grid_center, img, quality)
console_log(length(triangle_area))
console_log()

graph = create_rectangular_graph(triangle_area, height_to_width_ratio)

graph_edges = []
for value in graph.edges.keys():
    graph_edges = push(value, graph_edges)

angles_coordinates = []
angles_coordinates2 = []
for i in range(2, 6):
    console_log(f"Iterations: {i}")
    angles_coordinates2 = push(find_inner_angles_coordinates_of_triangle(graph, 3, i, img, quality), angles_coordinates2)

angles_coordinates = push(angles_coordinates2, angles_coordinates)

console_log("angles coordinates")

for angles_coordinates in angles_coordinates2:
    console_log(angles_coordinates)
    console_log()




