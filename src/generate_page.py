import os
from split_blocks import markdown_to_html

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
 