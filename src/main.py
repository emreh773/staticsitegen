from textnode import TextNode, TextType
from copy_folder import scan_folder
from generate_page import generate_page
from pathlib import Path

print("hello world")

def main():
    asdf =  TextNode("Hello", TextType.TEXT, "http://example.com")
    print(asdf)
    scan_folder(Path("static"), Path("public"))
    generate_page(Path("content/index.md"), Path("template.html"), Path("public/index.html"))

main()