import os
import shutil
import re

public_dir = "../public"
static_dir = "../../static"
MODE=0o700
file_pattern = re.compile(r"[a-zA-Z0-9]+\.[a-z]{,4}")

def clear_public():
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
        os.mkdir(public_dir, mode=MODE)
    else:
        os.mkdir(public_dir, mode=MODE)
    copy_dir(static_dir, public_dir)
    print("Done")

def copy_dir(source_dir, dest_dir):
    from_dir_list = os.listdir(source_dir)
    to_dir_list = os.listdir(dest_dir)
    files = []
    directories = []
    for item in from_dir_list:
        if re.match(file_pattern, item):
            files.append(item)
        else:
            directories.append(item)
    for file in files:
        if file not in os.listdir(dest_dir):
            shutil.copy(os.path.join(source_dir, file), dest_dir)
    for folder in directories:
        if folder not in to_dir_list:
            os.mkdir(os.path.join(dest_dir, folder), mode=MODE)
            return copy_dir(os.path.join(source_dir, folder), os.path.join(dest_dir, folder))
    if source_dir == static_dir and dest_dir == public_dir:
        return
    from_broken = source_dir.split("/")
    new_source = "/".join(from_broken[:-1])
    to_broken = dest_dir.split("/")
    new_dest = "/".join(to_broken[:-1])
    return copy_dir(new_source, new_dest)