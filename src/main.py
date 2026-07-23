from textnode import TextNode, TextType
from copy_folder import scan_folder, clear_destination
from generate_page import generate_page, generate_page_recursively
from pathlib import Path
import sys

print("hello world")

def main():
    asdf =  TextNode("Hello", TextType.TEXT, "http://example.com")
    print(asdf)
    scan_folder(Path("static"), Path("public"))
    basepath = sys.argv[1]
    source = Path("content")
    source_root = Path("content")
    target_root = Path("public")
    generate_page_recursively(source, Path("template.html"), target_root, source_root)
            
main()