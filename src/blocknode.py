from enum import Enum

class BlockType(Enum):
    PARA = "paragraph"
    HEAD = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED = "unordered list"
    ORDERED = "ordered list"

def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEAD
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    block_lines = block.split("\n")
    if block.startswith(">"):
        is_quote = True
        for line in block_lines:
            if not line.startswith(">"):
                is_quote = False
                break
        if is_quote:
            return BlockType.QUOTE
    if block.startswith("- "):
        is_unordered_list = True
        for line in block_lines:
            if not line.startswith("- "):
                is_unordered_list = False
                break
        if is_unordered_list:
            return BlockType.UNORDERED
    if block.startswith("1. "):
        is_ordered_list = True
        i = 1
        for line in block_lines:
            if not line.startswith(f"{i}. "):
                is_ordered_list = False
                break
            i += 1
        if is_ordered_list:
            return BlockType.ORDERED
    return BlockType.PARA
        
def markdown_to_blocks(markdown):
    block = markdown.split("\n\n")
    split_blocks = []
    for item in block:
        stripped = item.strip()
        if stripped != "":
            split_blocks.append(stripped)
    return split_blocks