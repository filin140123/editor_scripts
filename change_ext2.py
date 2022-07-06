import os

exts = tuple(input("Enter formats, divided by space (example: 'md adoc txt'): ").split())
new_ext = input("Enter wanted extension: ")

for dirname, dirs, files in os.walk("."):
    for filename in files:
        if filename.endswith(exts):
            old = dirname + "\\" + filename
            new = dirname + "\\" + filename.split(".")[0] + "." + new_ext
            os.rename(old, new)

input("Done. Press any key to close")
