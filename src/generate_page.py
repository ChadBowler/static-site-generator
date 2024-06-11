import os
import re
from pathlib import Path
from split_blocks import markdown_to_html

md_pattern = re.compile(r"[a-zA-Z0-9]+\.md")
file_pattern = re.compile(r"[a-zA-Z0-9]+\.[a-z]{,4}")

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.split(" ", 1)[1]
    raise Exception("Page must have a header")
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path}, to {dest_path} using {template_path}")
    with open(from_path, 'r', encoding="utf-8") as f:
        md_contents = f.read()

    with open(template_path, 'r', encoding="utf-8") as f:
        temp_contents = f.read()
    title = extract_title(md_contents)
    html_content = markdown_to_html(md_contents).to_html()
    temp_contents = temp_contents.replace(r"{{ Title }}", title)
    temp_contents = temp_contents.replace(r"{{ Content }}", html_content)

    with open(dest_path, 'w', encoding="utf-8") as f:
        f.write(temp_contents)
 
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    content_dir_files = os.listdir(dir_path_content)
    files = []
    directories = []
    for file in content_dir_files:
        if re.match(file_pattern, file):
            files.append(file)
        else:
            directories.append(file)
    for file in files:
        if re.match(file_pattern, file):
            if re.match(md_pattern, file):
                new_dir_name = dir_path_content.split("/")[-1]
                os.mkdir(os.path.join(dest_dir_path, new_dir_name))
                if new_dir_name != "content":
                    new_dir = os.path.join(dest_dir_path, new_dir_name)
                else:
                    new_dir = dest_dir_path
                generate_page(os.path.join(dir_path_content, file), template_path, os.path.join(new_dir, "index.html"))
    for folder in directories:
        return generate_pages_recursive(os.path.join(dir_path_content, folder), template_path, dest_dir_path)