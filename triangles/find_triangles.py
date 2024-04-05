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


file_name = "breadth_first_search"
par_dir = "utils"
path = __file__
for i in range(3):
    path = os.path.dirname(path)
file_path = path + "/" + par_dir + "/" + file_name + ".py"
loader = Loader()
breadth_first_search = loader.load_module(file_name, file_path)

breadth_first_search2 = breadth_first_search.breadth_first_search2


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
count_length_of_sides_of_triangle = utils.count_length_of_sides_of_triangle
count_value_of_angles_in_triangle = utils.count_value_of_angles_in_triangle
find_angles_coordinates = utils.find_angles_coordinates
find_outer_angles_coordinates_of_triangle = utils.find_outer_angles_coordinates_of_triangle
check_similarity_of_triangles = utils.check_similarity_of_triangles


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


### recognize triangles with cv2
img_name = "data/triangles1.jpg"
img = cv2.imread(img_name)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

quality = 90                # %

console_log(img.shape)
console_log(img.dtype)

# find triangles area
triangles_area = []
width = img.shape[0]
height = img.shape[1]
grid = squareGrid(width, height)
grid_center = (int(width / 2), int(height / 2))

triangles_area = create_triangle_area(img, quality)

# triangles_area = breadth_first_search(grid, grid_center, img, quality)

# console_log(triangles_area)

# create graph from triangles area
example_edges = {
    "A": ["B"],
    "B": ["A", "C", "D"],
    "C": ["A"],
    "D": ["E", "A"],
    "E": ["B"],
    (100, 40): [(169, 158), (165, 151), (162, 174)],
}

graph = create_graph(triangles_area)

# count connected components in graph
graph_example = {
    "A": {"B", "C", "D"},
    "B": {"A", "C", "E"},
    "C": {"A", "B"},
    "D": {"A"},
    "E": {"B"},
    "F": {"G"},
    "G": {"F"},
}

isolated_subgraphs_count, triangles_areas_list = connected_components_count(graph)
console_log()

# check if graph is consistent
if isolated_subgraphs_count == 1:
    console_log("graph is consistent")
else:
    console_log("graph is not consistent")

console_log()
console_log("number of isolated subgraphs")
console_log(isolated_subgraphs_count)
console_log()

# count angles and sides of triangles
graphs_list = []
for triangle_area in triangles_areas_list:
    graph = create_graph(triangle_area)
    graphs_list = push(graph, graphs_list)

for graph in graphs_list:
    # find coordinates of angles in triangle
    angles_coordinates = find_outer_angles_coordinates_of_triangle(graph, 3, 2, img, quality)
    graph.angles_coordinates = angles_coordinates
    console_log("angles coordinates")
    console_log(angles_coordinates)
    console_log()

    # check if there are three angles
    if length(angles_coordinates) == 3:
        console_log("there are three angles")
        console_log()

    # count length of sides of triangle
    sides_length = count_length_of_sides_of_triangle(angles_coordinates)
    graph.sides_length = sides_length
    console_log("length of sides of triangle")
    console_log(sides_length)
    console_log()

    # count values of angles in triangle
    values_of_angles = count_value_of_angles_in_triangle(sides_length)
    console_log("values of angles in triangle")
    console_log(values_of_angles)
    console_log()
    console_log()
    console_log()

if length(graphs_list) == 2:
    # check if two triangles are similar
    graph1 = graphs_list[0]
    graph2 = graphs_list[1]
    check_similarity_of_triangles(graph1, graph2)

if length(graphs_list) == 2:
    # check if graphs created from triangles are isomorphic
    graph3 = {
        graph1.angles_coordinates[0]: {graph1.angles_coordinates[1], graph1.angles_coordinates[2]},
        graph1.angles_coordinates[1]: {graph1.angles_coordinates[0], graph1.angles_coordinates[2]},
        graph1.angles_coordinates[2]: {graph1.angles_coordinates[0], graph1.angles_coordinates[1]},
    }

    graph4 = {
        graph2.angles_coordinates[0]: {graph2.angles_coordinates[1], graph2.angles_coordinates[2]},
        graph2.angles_coordinates[1]: {graph2.angles_coordinates[0], graph2.angles_coordinates[2]},
        graph2.angles_coordinates[2]: {graph2.angles_coordinates[0], graph2.angles_coordinates[1]},
    }

    graph3_result = get_graph_result(graph3, 1)
    graph4_result = get_graph_result(graph4, 1)

    compare_graphs(graph3_result, graph4_result)
