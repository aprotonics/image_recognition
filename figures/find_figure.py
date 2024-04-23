import os
import importlib
import cv2
import asyncio


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

get_coordinates_from_output = utils.get_coordinates_from_output
count_length_of_sides_of_complete_graph = utils.count_length_of_sides_of_complete_graph
modify_shape = utils.modify_shape
create_graph = utils.create_graph
group_by_minimum_distance = utils.group_by_minimum_distance
create_img_array_from_graph = utils.create_img_array_from_graph
create_graph_async = utils.create_graph_async
find_angles_coordinates_async = utils.find_angles_coordinates_async
modify_img_from_angles_coordinates_async = utils.modify_img_from_angles_coordinates_async
find_angles_coordinates_from_img_async = utils.find_angles_coordinates_from_img_async
merge_angles_coordinates_async = utils.merge_angles_coordinates_async
count_length_of_sides_async = utils.count_length_of_sides_async
compare_rectangle_to_letter_dict_async = utils.compare_rectangle_to_letter_dict_async


file_name = "utils_os"
par_dir = "utils_os"
path = __file__
for i in range(3):
    path = os.path.dirname(path)
file_path = path + "/" + par_dir + "/" + file_name + ".py"
loader = Loader()
utils_os = loader.load_module(file_name, file_path)

create_dir = utils_os.create_dir
delete_dir = utils_os.delete_dir


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


letters_to_letters = {

}


file_names =    [
                    "output/find_rectangle2.txt",
                    "output/find_rectangle3.txt",
                    "output/find_rectangle4.txt",
                    "output/find_rectangle5.txt"
                ]

recieved_coordinates = get_coordinates_from_output(file_names)

angles_coordinates2 = recieved_coordinates[0]
anlges_coordinates = []
anlges_coordinates.extend(angles_coordinates2[0])
anlges_coordinates.extend(angles_coordinates2[1])
angles_coordinates2 = anlges_coordinates

angles_coordinates3 = recieved_coordinates[1]
anlges_coordinates = []
anlges_coordinates.extend(angles_coordinates3[0])
anlges_coordinates.extend(angles_coordinates3[1])
angles_coordinates3 = anlges_coordinates

angles_coordinates4 = recieved_coordinates[2]
anlges_coordinates = []
anlges_coordinates.extend(angles_coordinates4[0])
anlges_coordinates.extend(angles_coordinates4[1])
angles_coordinates4 = anlges_coordinates

angles_coordinates5 = recieved_coordinates[3]
anlges_coordinates = []
anlges_coordinates.extend(angles_coordinates5[0])
anlges_coordinates.extend(angles_coordinates5[1])
angles_coordinates5 = anlges_coordinates

sides_length2 = count_length_of_sides_of_complete_graph(angles_coordinates2)
sides_length3 = count_length_of_sides_of_complete_graph(angles_coordinates3)
sides_length4 = count_length_of_sides_of_complete_graph(angles_coordinates4)
sides_length5 = count_length_of_sides_of_complete_graph(angles_coordinates5)

letters_to_letters[2] = sides_length2
letters_to_letters[3] = sides_length3
letters_to_letters[4] = sides_length4
letters_to_letters[5] = sides_length5


img_name = "data/figure1.jpg"
img = cv2.imread(img_name)


if img.shape[1] > img.shape[0]:
    img = modify_shape(img)


quality = 98
width = img.shape[0]
height = img.shape[1]
height_to_width_ratio = (3, 2)

grid = squareGrid(width, height)
grid_center = (int(width / 2), int(height / 2))

rectangle_area = breadth_first_search2(grid, grid_center, img, quality)
graph = create_graph(rectangle_area)
isolated_subgraphs_count, rectangles_areas_list = connected_components_count(graph)


graphs_list = []
for i in range(len(rectangles_areas_list)):
    graph1 = create_graph(rectangles_areas_list[i])
    graphs_list.append(graph1)

clusters = group_by_minimum_distance(graphs_list, img)


current_dir = os.path.curdir
dir_to_create = current_dir + "/data/cache"
create_dir(dir_to_create)


number_of_graphs = 0
graph_number = 0

for cluster in clusters:
    for graph in cluster:
        
        graph_number += 1
        modified_img = create_img_array_from_graph(graph, img)
        cv2.imwrite(f"data/cache/000{graph_number}.jpg", modified_img)

number_of_graphs = graph_number


images = []
for i in range(1, number_of_graphs + 1):
    img_name = f"data/cache/000{i}.jpg"
    img = cv2.imread(img_name)
    images.append(img)


rectangles_areas_list = []
for img in images:
    width = img.shape[0]
    height = img.shape[1]
    height_to_width_ratio = (3, 2)

    grid = squareGrid(width, height)
    grid_center = (int(width / 2), int(height / 2))

    rectangle_area = breadth_first_search2(grid, grid_center, img, quality)
    rectangles_areas_list.append(rectangle_area)


async def main(rectangles_areas_list):
    rectangles_areas_list = rectangles_areas_list

    global quality
    global images
    global letters_to_letters
    global isolated_subgraphs_count

    tasks = []
    number_of_graphs = length(rectangles_areas_list)

    rectangles_areas_list_copy = []

    for i in range(21, 22):
        rectangles_areas_list_copy.append(rectangles_areas_list[i])

    number_of_graphs = length(rectangles_areas_list_copy)

    if number_of_graphs > 0:
        for i in range(number_of_graphs):
            rectangle_area = rectangles_areas_list_copy[i]
            task = asyncio.create_task(create_graph_async(rectangle_area, i))
            tasks.append(task)

    for task in tasks:
        await task
    
    graphs_list = []

    for task in tasks:
        task_result = task.result()
        graphs_list.append(task_result)
    
    console_log()
    console_log(length(graphs_list))
    console_log()


    tasks = []
    
    if number_of_graphs > 0:
        for i in range(number_of_graphs):
            graph = graphs_list[i]
            img = images[i]
            task = asyncio.create_task(find_angles_coordinates_async(graph, img, quality, i))
            tasks.append(task)

    for task in tasks:
        await task

    angles_coordinates1_list = []

    for task in tasks:
        task_result = task.result()
        angles_coordinates1_list.append(task_result)

    console_log()
    console_log(length(angles_coordinates1_list))
    console_log()


    tasks = []

    if number_of_graphs > 0:
        for i in range(number_of_graphs):
            angles_coordinates = angles_coordinates1_list[i]
            img = images[i]
            task = asyncio.create_task(modify_img_from_angles_coordinates_async(angles_coordinates, img, i))
            tasks.append(task)

    for task in tasks:
        await task

    modified_images_list = []

    for task in tasks:
        task_result = task.result()
        modified_images_list.append(task_result)

    console_log()
    console_log(length(modified_images_list))
    console_log()


    tasks = []
    modified_images1_list = []
    inf_coordinates_list = []

    for value in modified_images_list:
        modified_images = value[0]
        inf_coordinates = value[1]
        modified_images1_list.append(modified_images)
        inf_coordinates_list.append(inf_coordinates)

    if number_of_graphs > 0:
        for i in range(number_of_graphs):
            modified_images = modified_images1_list[i]
            inf_coordinates = inf_coordinates_list[i]
            task = asyncio.create_task(find_angles_coordinates_from_img_async(modified_images, inf_coordinates, quality, i))
            tasks.append(task)

    for task in tasks:
        await task
    
    angles_coordinates2_list = []

    for task in tasks:
        task_result = task.result()
        angles_coordinates2_list.append(task_result)

    console_log()
    console_log(length(angles_coordinates2_list))
    console_log()
    

    tasks = []

    if number_of_graphs > 0:
        for i in range(number_of_graphs):
            angles_coordinates1 = angles_coordinates1_list[i]
            angles_coordinates2 = angles_coordinates2_list[i]
            task = asyncio.create_task(merge_angles_coordinates_async(angles_coordinates1, angles_coordinates2, i))
            tasks.append(task)
    
    for task in tasks:
        await task

    angles_coordinates_list = []

    for task in tasks:
        task_result = task.result()
        angles_coordinates_list.append(task_result)

    console_log()
    console_log(length(angles_coordinates_list))
    console_log()


    tasks = []

    if number_of_graphs > 0:
        for i in range(number_of_graphs):
            angles_coordinates = angles_coordinates_list[i]
            task = asyncio.create_task(count_length_of_sides_async(angles_coordinates, i))
            tasks.append(task)

    for task in tasks:
        await task
    
    sides_length_list = []

    for task in tasks:
        task_result = task.result()
        sides_length_list.append(task_result)

    console_log()
    console_log(length(sides_length_list))
    console_log()


    tasks = []

    if number_of_graphs > 0:
        for i in range(number_of_graphs):
            sides_length = sides_length_list[i]
            task = asyncio.create_task(compare_rectangle_to_letter_dict_async(sides_length, letters_to_letters, i))
            tasks.append(task)
    
    for task in tasks:
        await task
    
    results = []

    for task in tasks:
        task_result = task.result()
        results.append(task_result)
    

    console_log(isolated_subgraphs_count == length(results))

    console_log()
    for value in results:
        console_log(value)
    console_log()

asyncio.run(main(rectangles_areas_list))


current_dir = os.path.curdir
dir_to_delete = current_dir + "/data/cache"
delete_dir(dir_to_delete)
