def block_to_block_type(markdown):
    header = markdown.split(" ")[0]
    if (header.count("#") > 1 or header.count("#") < 6)and len(header) == header.count("#"):
        return "heading"
    if header[0:3] == '```' and markdown[len(markdown)-3:] == '```' :
        return "code"
    if header.count(">") == 1 and len(header) == 1:
        return "quote"
    if (header.count("*") == 1 or header.count("-") == 1) and len(header) == 1:
        return "unordered_list"
    if header[0].isnumeric() and len(header) == 2 and header[1] == '.':
        split_lines = markdown.split("\n")
        line_num = 1
        for line in split_lines:
            if int(line[0]) != line_num:
                return "paragraph"
            line_num += 1
        return "ordered_list"
    return "paragraph"