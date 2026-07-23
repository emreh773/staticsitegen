from pathlib import Path
import sys

from textnode import TextNode, TextType
from copy_folder import scan_folder, clear_destination
from generate_page import generate_page, generate_page_recursively

print("hello world")

def main():
    asdf =  TextNode("Hello", TextType.TEXT, "http://example.com")
    print(asdf)
    scan_folder(Path("static"), Path("docs"))
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    source = Path("content")
    source_root = Path("content")
    target_root = Path("docs")
    generate_page_recursively(source, Path("template.html"), target_root, source_root, basepath)
            
main()