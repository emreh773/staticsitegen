from enum import Enum
from textwrap import dedent
import re

from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import text_to_textnodes

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    CODE = "code"
    QUOTE = "quote"

def block_to_block_type(block: str) -> BlockType:
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    elif re.match(r"^- ", block):
        block_lines = block.splitlines()
        if all(re.match(r"^- ", line) for line in block_lines):
            return BlockType.UNORDERED_LIST
    elif re.match(r"^1\. ", block):
        block_lines = block.splitlines()
        i = 1
        flag = True
        for line in block_lines:
            if not re.match(rf"^{i}\. ", line):
                flag = False
                break
            i += 1
        if flag:
            return BlockType.ORDERED_LIST
    elif re.match(r"^```\n", block):
        if block.endswith("\n```"):
            return BlockType.CODE
    elif re.match(r"^> ", block):
        block_lines = block.splitlines()
        if all(re.match(r"^> ", line) for line in block_lines):
            return BlockType.QUOTE
    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown: str) -> list[str]:
    delimiter = "\n\n"
    blocks = markdown.split(delimiter)
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def markdown_to_html_node(markdown: str) -> ParentNode:
    markdown = dedent(markdown)
    blocks = markdown_to_blocks(markdown)
    child_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            block = heading_to_html_node(block)
        elif block_type == BlockType.UNORDERED_LIST:
            block = unordered_list_to_html_node(block)
        elif block_type == BlockType.ORDERED_LIST:
            block = ordered_list_to_html_node(block)
        elif block_type == BlockType.CODE:
            block = code_block_to_html_node(block)
        elif block_type == BlockType.QUOTE:
            block = quote_to_html_node(block)
        elif block_type == BlockType.PARAGRAPH:
            block = paragraph_to_html_node(block)
        child_nodes.append(block)
    return ParentNode(tag="div", children=child_nodes)

def heading_to_html_node(heading: str) -> ParentNode:
    hash_count = len(heading) - len(heading.lstrip("#"))
    heading = heading.lstrip("#").strip()
    text_nodes = text_to_textnodes(heading)
    children = []
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return ParentNode(tag=f"h{hash_count}", children=children)

def unordered_list_to_html_node(unordered_list: str) -> ParentNode:
    list_items = unordered_list.splitlines()
    children = []
    for item in list_items:
        item = item[2:].strip()
        text_nodes = text_to_textnodes(item)
        item_children = []
        for node in text_nodes:
            item_children.append(text_node_to_html_node(node))
        children.append(ParentNode(tag="li", children=item_children))
    return ParentNode(tag="ul", children=children)

def ordered_list_to_html_node(ordered_list: str) -> ParentNode:
    list_items = ordered_list.splitlines()
    children = []
    for item in list_items:
        item = item[(item.find(".") + 1):].strip()
        text_nodes = text_to_textnodes(item)
        item_children = []
        for node in text_nodes:
            item_children.append(text_node_to_html_node(node))
        children.append(ParentNode(tag="li", children=item_children))
    return ParentNode(tag="ol", children=children)

def code_block_to_html_node(code_block: str) -> ParentNode:
    code_block = code_block[3:-3].lstrip("\n")
    text_node = TextNode(code_block, TextType.CODE)
    html_node = text_node_to_html_node(text_node)
    children = [html_node]
    return ParentNode(tag="pre", children=children)

def quote_to_html_node(quote: str) -> ParentNode:
    quote_lines = quote.splitlines()
    quote = " ".join(line[1:].strip() for line in quote_lines)
    text_nodes = text_to_textnodes(quote)
    children = []
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return ParentNode(tag="blockquote", children=children)

def paragraph_to_html_node(paragraph: str) -> ParentNode:
    paragraph = paragraph.replace("\n", " ")
    text_nodes = text_to_textnodes(paragraph)
    children = []
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return ParentNode(tag="p", children=children)