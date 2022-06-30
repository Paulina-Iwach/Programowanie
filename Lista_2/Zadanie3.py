import os
import zipfile
from time import localtime, strftime


def generate_zip_copy(catalog_name: str):
    """
    Function creates backups, saving selected catalogs to zip archives.
    :param catalog_name: Name of the catalog to back up.
    """
    if type(catalog_name) is not str:
        raise ValueError("Catalog name type must be string.")
    elif not os.path.exists(catalog_name):
        raise ValueError("Catalog doesn't exist.")
    else:
        file_list = []
        name = strftime("%Y-%m-%d %H-%M-%S", localtime()) + ".zip"

        for root, directories, files in os.walk(catalog_name):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_list.append(filepath)

        zf = zipfile.ZipFile(name, mode='w')
        for file in file_list:
            zf.write(file, os.path.relpath(os.path.join(root, file), os.path.join(catalog_name, '..')))

        zf.close()


generate_zip_copy("C:/Users/Artur/Desktop/tutoring")
