import shutil
import os
from generate_page import generate_pages_recursive

def del_dir(dest_dir_path):
    if os.path.exists(dest_dir_path):
        shutil.rmtree(dest_dir_path)
        return f"{dest_dir_path} was deleted"
    else:
        return f"{dest_dir_path} does not exist"
    
def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    files_in_source = os.listdir(source_dir_path)
    for item in files_in_source:
        from_path = os.path.join(source_dir_path, item)
        to_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
            print(f"{from_path} has been copied to {to_path}")
        else:
            copy_files_recursive(from_path, to_path)

        
    





def main():
    del_dir("public")
    copy_files_recursive("static", "public")
    generate_pages_recursive("content", "template.html", "public")


main()