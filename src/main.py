from textnode import *
from copytodirectory import copy_to_directory
from generatepagesrecursive import generate_pages_recursive

def main():
    copy_to_directory('static/', 'public/')
    generate_pages_recursive('content/', 'template.html', 'public/')

if __name__ == '__main__':
    main() 
