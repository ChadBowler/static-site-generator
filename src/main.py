from textnode import TextNode

def main():
    text = "This is a text node"
    text_type = "bold"
    url = "https://www.google.com"
    new_node = TextNode(text, text_type, url)
    print(new_node)


if __name__ == "__main__":
    main()