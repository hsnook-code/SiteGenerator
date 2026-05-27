from markdown_blocks import markdown_to_html_node
from htmlnode import LeafNode, ParentNode
import os
import pathlib

def extract_title(markdown):
    if not markdown.startswith("# "):
        raise Exception("h1 missing. Does the markdown start with #?")
    title_with_hash = markdown.split("\n", 1)
    title = title_with_hash[0].split("#", 1)
    return title[1].strip()
    
def generate_page(from_path, template_path, dest_path):
    print(f"Generateing page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        from_contents = f.read()
    with open(template_path) as f:
        template_contents = f.read()
    html_node = markdown_to_html_node(from_contents)
    html_string = html_node.to_html()
    title = extract_title(from_contents)
    html_file = template_contents.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w') as f:
        f.write(html_file)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    list_of_files = os.listdir(dir_path_content)
    for item in list_of_files:
        from_path = os.path.join(dir_path_content, item)
        to_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(from_path):
            if from_path.endswith(".md"):
                to_path = to_path.replace(".md", ".html")
                generate_page(from_path, template_path, to_path)
        else:
            generate_pages_recursive(from_path, template_path, to_path)
        