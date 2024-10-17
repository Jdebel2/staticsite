import shutil
import os

def copy_to_directory(source, destination):
    if not os.path.exists(source):
        raise ValueError("Source directory does not exist")
    if not os.path.exists(destination):
        raise ValueError("Destination directory does not exist")
    
    shutil.rmtree(destination)
    os.mkdir(destination)

    print(f"Copying {source} to {destination}")
    for item in os.listdir(source):
        item_source_path = os.path.join(source, item)
        item_destination_path = os.path.join(destination, item)
        if os.path.isfile(os.path.join(source, item)):
            shutil.copy(item_source_path, item_destination_path)
            print(f"Created file {item_destination_path}")
        else:
            os.mkdir(item_destination_path)
            copy_to_directory(item_source_path, item_destination_path)