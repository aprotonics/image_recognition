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


file_name = "utils"
par_dir = "utils"
path = __file__
utils = create_file_object(file_name, par_dir, path)
create_graph = utils.create_graph
modify_src = utils.modify_src

file_name = "console_log"
par_dir = "utils_functions"
path = __file__
console_log = create_file_object(file_name, par_dir, path)
console_log = console_log.console_log


img_name = "../data/modified.jpg"
img = cv2.imread(img_name)

modified_img = modify_src(img)

cv2.imwrite("../data/modified1.jpg", modified_img)
