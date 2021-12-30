import os
import datetime

DIR = r"D:\homework"
now = datetime.datetime.now()


def rename_files(my_dir):
    for root, dirs, files in os.walk(my_dir):
        for name in files:
            rename_file(root, name)


def rename_file(root, name):
    new_name = f'{name.split(".")[0]}_{now.strftime("%d-%m-%Y_%H-%M-%S")}.{name.split(".")[1]}'
    old_file = os.path.join(root, name)
    new_file = os.path.join(root, new_name)
    print(old_file)
    print(new_file)
    os.rename(old_file, new_file)


rename_files(DIR)
