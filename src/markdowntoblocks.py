def markdown_to_blocks(markdown):
    md_blocks = []
    split_md = markdown.strip().split("\n")
    
    md_item = ""
    for item in split_md:
        if item != "":
            if md_item != "":
                md_item += "\n"+item
            else:
                md_item += item
        else:
            if md_item != "":
                md_blocks.append(md_item)
                md_item = ""
    if md_item != "":
        md_blocks.append(md_item)
    return md_blocks