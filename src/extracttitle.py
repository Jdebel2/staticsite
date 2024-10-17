

def extract_title(markdown):
    md_split = markdown.split('\n')[0].split(" ", 1)
    if md_split[0] != '#':
        raise Exception("Missing h1 markdown header")
    return md_split[1].strip()