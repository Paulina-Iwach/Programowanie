import os
import shutil
import sys


def unpack(folder: str):
    """
    Function unpacks files from the selected directory to directory above.
    :param folder: Directory from which we want to unpack the files.
    """
    if not os.path.exists(folder):
        raise ValueError("Catalog doesn't exist.")
    else:
        list_of_files = []

        for root, directories, files in os.walk(folder):
            for filename in files:
                filepath = os.path.join(root, filename)
                list_of_files.append(filepath)

        for i in list_of_files:
            shutil.copy2(i, os.path.split(os.path.abspath(folder))[0] + "/" + os.path.split(i)[1])

    print("Folder was successfully unpacked.")


# unpack("C:/Users/Artur/Desktop/Matematyka stosowana/Programowanie/lista_3/archiwum2")
unpack(sys.argv[1])
