from copy_static import clear_public
from generate_page import generate_pages_recursive

dir_path_content = "./content"
template_path = "./template.html"
dest_dir_path = "./public"

def main():
    clear_public()
    generate_pages_recursive(dir_path_content, template_path, dest_dir_path)

if __name__ == "__main__":
    main()
