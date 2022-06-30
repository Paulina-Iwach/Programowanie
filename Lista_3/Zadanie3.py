import os
import shutil
import datetime as dt
import sys
from time import strftime, localtime


def find_files(extension, directory):
    """
    Function finds files with given extensions that were modified
    in the last 3 days in particular directory.
    :param extension:Extension of files we want to find.
    :param directory: Name/path to the directory where we want to look for files.
    :return: List of files modified in the last 3 days.
    """
    now = dt.datetime.now()
    ago = now - dt.timedelta(days=3)
    list_of_files = []

    if extension[0] != ".":
        raise ValueError("It's not file extension.")
    elif not os.path.exists(directory):
        raise ValueError("Catalog doesn't exist!")
    else:
        for root, directories, files in os.walk(directory):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                st = os.stat(file_path)
                modification_time = dt.datetime.fromtimestamp(st.st_mtime)

                if ago < modification_time and os.path.splitext(file_path)[1] == extension:
                    list_of_files.append(file_path)
        return list_of_files


def create_backup_copy(extension, directory):
    """
    Function creates backup copy of files with particular extension which are in given  directory.
    :param extension: Extension of files we want to copy.
    :param directory:Path to directory from we want to copy files.
    """
    files = find_files(extension, directory)
    date = strftime("%Y-%m-%d %H-%M-%S", localtime())
    final_path = "Backup/copy-" + date

    if not os.path.exists("Backup"):
        os.makedirs("Backup")
    elif not os.path.exists(final_path):
        os.makedirs(final_path)

    for i in files:
        shutil.copy2(i, final_path + "/" + os.path.split(i)[1])

    print("Backup was successfully created.")


# create_backup_copy(".txt", "C:/Users/Artur/Desktop/Matematyka stosowana/Programowanie")

create_backup_copy(sys.argv[1], sys.argv[2])
