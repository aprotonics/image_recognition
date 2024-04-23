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

breadth_first_search4 = breadth_first_search.breadth_first_search4
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

create_graph = utils.create_graph
create_rectangular_graph = utils.create_rectangular_graph
count_length_of_sides_of_rectangle = utils.count_length_of_sides_of_rectangle
count_length_of_sides_of_complete_graph = utils.count_length_of_sides_of_complete_graph
rectangle_to_letter_comparison = utils.rectangle_to_letter_comparison
count_value_of_angles_in_rectangle = utils.count_value_of_angles_in_rectangle
check_similarity_of_complete_graphs = utils.check_similarity_of_complete_graphs
check_similarity_of_complete_graphs2 = utils.check_similarity_of_complete_graphs2
find_angles_coordinates = utils.find_angles_coordinates
find_outer_angles_coordinates = utils.find_outer_angles_coordinates
find_inner_angles_coordinates = utils.find_inner_angles_coordinates
group_by_minimum_distance = utils.group_by_minimum_distance
find_nearest_point_to_point = utils.find_nearest_point_to_point
find_coordinates_to_cut = utils.find_coordinates_to_cut
modify_shape = utils.modify_shape
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


file_name = "get_maximum"
par_dir = "utils_functions"
path = __file__
for i in range(3):
    path = os.path.dirname(path)
file_path = path + "/" + par_dir + "/" + file_name + ".py"
loader = Loader()
get_maximum = loader.load_module(file_name, file_path)

get_maximum = get_maximum.get_maximum


file_name = "push"
par_dir = "utils_functions"
path = __file__
for i in range(3):
    path = os.path.dirname(path)
file_path = path + "/" + par_dir + "/" + file_name + ".py"
loader = Loader()
push = loader.load_module(file_name, file_path)

push = push.push


letters_to_letters = {

}

angles_coordinates2 =   [
                            (252, 48), (53, 47), (159, 346), (146, 346), (72, 47), (233, 47),
                            (153, 301)
                        ]

angles_coordinates3 =   [
                            (233, 346), (233, 47), (252, 346), (252, 47), (72, 346), (72, 47), (53, 346), (53, 47),
                            (232, 186), (232, 207), (73, 186), (73, 207)
                        ]

angles_coordinates4 =   [
                            (252, 206), (252, 187), (252, 327), (252, 66), (252, 346), (252, 47), (53, 346), (53, 47),
                            (73, 186), (73, 207), (73, 67), (73, 326)
                        ]

angles_coordinates5 =   [
                            (252, 327), (252, 66), (252, 346), (252, 47), (53, 346), (53, 47),
                            (73, 67), (73, 326)
                        ]

sides_length2 = count_length_of_sides_of_complete_graph(angles_coordinates2)
sides_length3 = count_length_of_sides_of_complete_graph(angles_coordinates3)
sides_length4 = count_length_of_sides_of_complete_graph(angles_coordinates4)
sides_length5 = count_length_of_sides_of_complete_graph(angles_coordinates5)

letters_to_letters[2] = sides_length2
letters_to_letters[3] = sides_length3
letters_to_letters[4] = sides_length4
letters_to_letters[5] = sides_length5


img_name = "data/figure3.jpg"
img = cv2.imread(img_name)

quality = 95                 # %

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

graph = create_graph(rectangle_area)
console_log(length(graph.edges.keys()))

isolated_subgraphs_count, rectangles_areas_list = connected_components_count(graph)
console_log()

if isolated_subgraphs_count == 1:
    console_log("graph is consistent")
else:
    console_log("graph is not consistent")

console_log()
console_log("number of isolated subgraphs")
console_log(isolated_subgraphs_count)
console_log()

graphs_list = []
for i in range(length(rectangles_areas_list)):
    graph1 = create_graph(rectangles_areas_list[i])
    graphs_list.append(graph1)

clusters = group_by_minimum_distance(graphs_list, img)


results = []

for i in range(length(rectangles_areas_list)):

    graph1 = create_graph(rectangles_areas_list[i])
    result = []

    graph1.angles_coordinates = []
    graph1.angles_coordinates1 = []
    angles_coordinates = []

    for k in range(1, 11):
        angles_coordinates1 = []
        for i in range(3, 4):
            console_log(f"Iterations: {i}")
            angles_coordinates1 = push(find_outer_angles_coordinates(graph1, k, i, img, quality), angles_coordinates1)

        angles_coordinates = push(angles_coordinates1[-1], angles_coordinates)

    graph1.angles_coordinates1 = angles_coordinates

    console_log()
    console_log()


    modified_images = []
    inf_coordinates = []

    for i in range(length(graph1.angles_coordinates1)):
        modified_img = modify_src(img)

        coordinates_to_cut = find_coordinates_to_cut(graph1.angles_coordinates1[i], img)
        (min_x, min_y) = coordinates_to_cut[1]

        modified_img2 = modified_img[(coordinates_to_cut[1][1])-10:(coordinates_to_cut[3][1]+10),
                                    (coordinates_to_cut[1][0])-10:(coordinates_to_cut[3][0]+10)]
        
        img_to_cut = modified_img2

        modified_img2_shape = get_maximum(modified_img2.shape[0], modified_img2.shape[1])
        modified_img2 = numpy.zeros((modified_img2_shape, modified_img2_shape, 3), numpy.uint8)

        coordinate1 = (coordinates_to_cut[3][1]+10) - (coordinates_to_cut[1][1]-10)
        coordinate2 = (coordinates_to_cut[3][0]+10) - (coordinates_to_cut[1][0]-10)

        modified_img2[0:coordinate1, 0:coordinate2] = img_to_cut

        modified_images = push(modified_img2, modified_images)
        inf_coordinates = push((min_x, min_y), inf_coordinates)


    graph1.angles_coordinates2 = []
    angles_coordinates = []

    for k in range(1, 11):
        modified_img = modified_images[k-1]
        (min_x, min_y) = inf_coordinates[k-1]

        width = modified_img.shape[0]
        height = modified_img.shape[1]
        height_to_width_ratio = (3, 2)

        grid = squareGrid(width, height)
        grid_center = (int(width / 2), int(height / 2))

        rectangle_area = breadth_first_search2(grid, grid_center, modified_img, quality)
        graph = create_graph(rectangle_area)

        angles_coordinates2 = []
        for i in range(3, 4):
            angles_coordinates2_2 = []
            console_log(f"Iterations: {i}")
            middle_coordinates = find_outer_angles_coordinates(graph, k, i, modified_img, quality)
            for value in middle_coordinates:
                (x, y) = value
                angles_coordinates2_2 = push((x + min_x - 10, y + min_y - 10), angles_coordinates2_2)

            angles_coordinates2 = push(angles_coordinates2_2, angles_coordinates2)
        
        angles_coordinates = push(angles_coordinates2[-1], angles_coordinates)

    graph1.angles_coordinates2 = angles_coordinates


    for k in range(length(graph1.angles_coordinates1)):
        for i in range(length(graph1.angles_coordinates2)):
            angles_coordinates = []
            angles_coordinates.extend(graph1.angles_coordinates1[k])
            angles_coordinates.extend(graph1.angles_coordinates2[i])

            graph1.angles_coordinates = push(angles_coordinates, graph1.angles_coordinates)


    graph1.sides_length = []
    sides_length = []

    for i in range(length(graph1.angles_coordinates)):
        sides_length1 = count_length_of_sides_of_complete_graph(graph1.angles_coordinates[i])
        sides_length = push(sides_length1, sides_length)

    graph1.sides_length = sides_length


    for key in letters_to_letters.keys():
        if rectangle_to_letter_comparison(graph1, letters_to_letters[key]):
            result = push(key, result)
        else:
            result = push("", result)

    results = push(result, results)


console_log(isolated_subgraphs_count == length(results))


for value in results:
    console_log(value)
