import os
import importlib


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
queue = structures.Queue()
