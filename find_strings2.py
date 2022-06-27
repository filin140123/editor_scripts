import os
import editlib as edl

exts = input("Enter formats, divided by space (example: 'md adoc txt'): ").split()
word = input("Enter word to find: ")

file_list = []

for dirname, dirs, files in os.walk("."):
    for filename in files:
        if filename.endswith(tuple(exts)):
            file_list.append(dirname + "\\" + filename)

string_list = edl.get_strings_from_files_by_word(file_list, word)

if input("Remove string part before seeking word? (y/n): ") in ["y", "Y", "yes"]:
    string_list = sorted(set([word + i.split(word, 1)[1] for i in string_list]))

with open(f"results by word {word}.txt", "a", encoding="utf-8") as r:
    for i in string_list:
        r.write(i + "\n")

input("Done. Press any key to close")
