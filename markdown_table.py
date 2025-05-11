def create_md_header(columns):
    header = '| ' + ' | '.join(columns) + ' |'
    separator = '| ' + ' | '.join(['---'] * len(columns)) + ' |'
    return header + '\n' + separator

def add_md_row(values):
    return '| ' + ' | '.join(values) + ' |'
