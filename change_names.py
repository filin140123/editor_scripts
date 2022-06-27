import os

user_file = input("Enter file name with extension: ")

for dirname, dirs, files in os.walk("."):
    for filename in files:
        if filename.lower() == user_file.lower():
            old = dirname + "\\" + filename
            new = dirname + "\\" + dirname.rsplit("\\", 1)[1] + "." + filename.split(".")[1]
            os.rename(old, new)

input("Done. Press any key to close")
