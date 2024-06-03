import re

def extract_markdown_images(text):
    reg_pattern = r"!\[(.*?)\]\((.*?)\)"
    images = re.findall(reg_pattern, text)
    return images

def extract_markdown_links(text):
    reg_pattern = r"\[(.*?)\]\((.*?)\)"
    images = re.findall(reg_pattern, text)
    return images
