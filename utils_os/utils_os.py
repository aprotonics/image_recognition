import os


def create_dir(dir_to_create):
    dir_to_create = dir_to_create

    if not os.path.exists(dir_to_create):
        os.mkdir(os.path.abspath(dir_to_create))


def delete_dir(dir_to_delete):
    dir_to_delete = dir_to_delete

    files_to_delete = os.listdir(os.path.abspath(dir_to_delete))

    for value in files_to_delete:
        file_to_delete = dir_to_delete + "/" + value
        os.remove(os.path.abspath(file_to_delete))

    os.rmdir(os.path.abspath(dir_to_delete))
