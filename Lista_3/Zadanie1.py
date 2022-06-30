import os
import shutil
import sys


def createArchive(files: list):
    """
    Function packs selected txt files into a given folder.
    If folder does not exist, it is created.
    :param files: List of files to pack. Last element in te list is path to directory.
    """

    if len(files) < 2:
        raise ValueError("Minimum two arguments are required.")
    else:
        for i in range(len(files) - 1):
            if os.path.splitext(files[i])[1] != ".txt":
                raise ValueError("Incorrect file extension: " + str(files[i]))
            elif not os.path.exists(files[i]):
                raise ValueError("File " + str(files[i]) + " doesn't exist.")

        if not os.path.exists(files[-1]):
            os.makedirs(files[-1])

        for i in files[:-1]:
            shutil.copy2(i, files[-1] + "/" + os.path.split(i)[1])
    print("The archive has been created.")

createArchive(sys.argv[1:])
# createArchive("a.txt", "b.txt", "c.txt", "archive")
