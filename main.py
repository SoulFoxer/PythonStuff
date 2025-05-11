from markdown_table import create_md_header, add_md_row

header = create_md_header(["Name", "Age", "Country","Test"])
row1 = add_md_row(["Alice", "30", "Germany","UK"])
row2 = add_md_row(["Bob", "25", "USA","Italy"])

table = '\n'.join([header, row1, row2])
print(table)
