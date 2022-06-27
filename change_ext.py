import os
import editlib as edl

old_exts = input("Enter formats, divided by space (example: 'md adoc txt'): ").split()
new_ext = input("Enter wanted extension: ")

file_list = edl.get_file_list(old_exts)

for file in file_list:
    os.rename(file, file.split(".")[0] + "." + new_ext)

input("Done. Press any key to close")
