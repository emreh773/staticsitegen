from pathlib import Path

from markdown_blocks import markdown_to_html_node, extract_title
from htmlnode import HTMLNode

def generate_page(from_path: Path, template_path: Path, dest_path: Path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r", encoding="utf-8") as file:
        content = file.read()
    with open(template_path, "r", encoding="utf-8") as template_file:
        template_content = template_file.read()
    html_content = markdown_to_html_node(content).to_html()
    title = extract_title(content)

    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html_content)

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    dest_path.write_text(template_content)