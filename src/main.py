from copy_static import clear_public
from generate_page import generate_page

from_path = "./content/index.md"
template_path = "./template.html"
dest_path = "./public/index.html"

def main():
    clear_public()
    generate_page(from_path, template_path, dest_path)

if __name__ == "__main__":
    main()
