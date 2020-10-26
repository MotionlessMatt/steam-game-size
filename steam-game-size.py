import os
import time

def convert_bytes(game_bytes):
    """Convert Bytes to either MB or GB and return as a string."""
    megabytes = round(game_bytes * 0.000001, 3)
    if megabytes >= 1024:
        gigabytes = round(megabytes * 0.001, 3)
    if 'gigabytes' in locals():
        return f"{gigabytes} GB"
    else:
        return f"{megabytes} MB"

def get_directories(text_file:str):
    """Get the list of Steam directories."""
    with open(text_file, "r") as f:
        list_of_dir = f.read().splitlines()
    return list_of_dir

def calculate_directory_size(directory):
    """Get the size of one folder."""
    total_size = 0
    for root, dirs, files in os.walk(directory):
        for f in files:
            fp = os.path.join(root, f)
            total_size += os.path.getsize(fp)
    return total_size

def get_steam_folders(directory):
    """Get a list of all of the folders in the steam directory.
    This will be used to get the size of each game."""
    return os.listdir(directory+"/steamapps/common")

def get_list():
    """Get an 'output.txt' file with all directories and game sizes calculated."""
    with open("output.txt", "w+") as f:
        f.write("")
    dirs = get_directories("directories.txt")
    for directory in dirs:
        folders = get_steam_folders(directory)
        size_of_directory = 0
        for folder in folders:
            size = calculate_directory_size(
                directory+"/steamapps/common/"+folder)
            size_of_directory += size
            with open("output.txt", "a+") as f:
                f.write(f"{folder}: {convert_bytes(size)}\n")
        with open("output.txt", "a+") as f:
            f.write(f'"{directory}": {convert_bytes(size_of_directory)}\n')

if __name__ == '__main__':
    get_list()
