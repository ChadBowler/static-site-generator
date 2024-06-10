import re

def markdown_to_blocks(markdown):
    blocks = re.split(r"[\n]{2}", markdown)
    stripped_blocks = []
    for block in blocks:
        if block == "":
            continue
        stripped_blocks.append(block.strip())
    return stripped_blocks
