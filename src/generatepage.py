import os

from extracttitle import extract_title
from markdowntohtmlnode import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    markdown = ""
    with open(from_path, 'r') as f:
        markdown += f.read()
    f.close()

    title = extract_title(markdown)
    html = markdown_to_html_node(markdown).to_html()

    template_data = ""
    with open(template_path, 'r') as t:
        template_data += t.read()
    t.close()
    
    n_html = template_data.replace('{{ Title }}', title)
    n_html = n_html.replace('{{ Content }}', html)

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    
    with open(dest_path, 'w') as d:
        d.write(n_html)
    
