from os.path import isfile, join
import os
import shutil
from pathlib import Path

def main():
    file_path = '/Users/_______/Downloads'
    create_folders(file_path)

def create_folders(file_path):
    dir = os.listdir(file_path)
    files = []
    for f in dir:
        if isfile(join(file_path, f)):
            files.append(f)

    type_list = []
    f_dict = {}
    i = 1

    for f in files:
        src_path = file_path + "/" + f
        type = (f.split('.')[-1]).lower()
        
        if type == "heic":
            heic_to_jpg(type, src_path)
            type = "jpg"
            f = f.split('.')[-2] + "." + type
            src_path = file_path + "/" + f
        if type not in type_list:
            type_list.append(type)
            folder_name = file_path + "/" + type + "_folder"
            f_dict[type] = folder_name
            if os.path.isdir(folder_name) != True:
                os.mkdir(folder_name)

        if type in f_dict:
            new_path = f_dict[type] + "/" + f
            shutil.move(src_path, new_path)

        print("{}. {} from {} to {}".format(i, f, src_path, new_path))
        i += 1
                
def heic_to_jpg(type, f):
    if type == "heic":
        path = Path(f)
        new_path = path.with_suffix(".jpg")

        try:
            path = path.rename(new_path)
        except FileNotFoundError:
            print("File not found")
        except FileExistsError:
            print("File already exists")

main()
