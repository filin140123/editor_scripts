from os import listdir
from os.path import isfile, join


def get_file_list(exts: list, path=".") -> list:
    """
    :param exts: one or multiple file extensions to search for.
    :param path: path to directory to look for, current directory by default.
    :return: list of files with specified extensions.
    """
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    file_list = []
    for ext in exts:
        for file in onlyfiles:
            if file.endswith(ext):
                file_list.append(file)
    return file_list


def get_strings_from_files_by_word(file_names: list, word: str) -> list:
    """
    :param file_names: list of file names to search in.
    :param word: special word to search for.
    :return: list of strings with specified word.
    """
    string_list = []
    for name in file_names:
        with open(name, "r", encoding="utf-8") as file:
            b = file.readline()
            while b:
                if word in b:
                    string_list.append(b)
                b = file.readline()
    return string_list


if __name__ == "__main__":
    get_file_list()
    get_strings_from_files_by_word()
