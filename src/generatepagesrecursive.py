import os

from generatepage import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        content_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        if not os.path.isfile(content_path):
            generate_pages_recursive(content_path, template_path, dest_path)
        else:
            dest_path = os.path.join(dest_path.split('.')[0]+'.html')
            generate_page(content_path, template_path, dest_path)
