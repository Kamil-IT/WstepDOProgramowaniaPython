import os
import re


def list_pdf_files(include_word, dir_path):
    path_list = []
    for root, dirs, files in os.walk(dir_path, topdown=True):
        # Root - ścieżka względna
        # dirs - katalogi w danym podfolderze
        # files - pliki w danym lokacji
        for name in files:
            if name[-4:] == ".pdf" and re.search(include_word, name):
                path_list.append(os.path.abspath(root + "\\" + name))
    return path_list


for path in list_pdf_files("praca", "."):
    print(path)
