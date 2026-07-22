from textnode import TextNode, TextType
from copy_folder import scan_folder, clear_destination
from generate_page import generate_page, generate_page_recursively
from pathlib import Path

print("hello world")

def main():
    asdf =  TextNode("Hello", TextType.TEXT, "http://example.com")
    print(asdf)
    scan_folder(Path("static"), Path("public"))
#    generate_page(Path("content/index.md"), Path("template.html"), Path("public/index.html"))
    source = Path("content")
    source_root = Path("content")
    target_root = Path("public")
    generate_page_recursively(source, Path("template.html"), target_root, source_root)
            
main()