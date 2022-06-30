import os
import datetime as dt


def generate_stats(catalog_name: str):
    """
    Function finds files in particular catalogs that have been modified in last year.
    :param catalog_name: Name of the catalog in which the files will be checked.
    :return: List with the files and their modification date.
    """
    if type(catalog_name) is not str:
        raise ValueError("Catalog name type must be string.")
    elif not os.path.exists(catalog_name):
        raise ValueError("Catalog doesn't exist.")
    else:
        now = dt.datetime.now()
        ago = now - dt.timedelta(days=365)
        modified_files = []

        for root, dirs, files in os.walk(catalog_name):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                st = os.stat(file_path)
                modification_time = dt.datetime.fromtimestamp(st.st_mtime)
                if modification_time > ago:
                    modified_files.append('%s modified %s' % (file_path, modification_time))
        save_to_txt(modified_files)

    return modified_files


def save_to_txt(list_to_save):
    """
    Function saves given list to a txt file.
    :param list_to_save: List that we want to save as txt file.
    """
    with open('last_year_modified_files.txt', 'w') as f:
        for item in list_to_save:
            f.write("%s\n" % item)


print(generate_stats("C:/Users/Artur/Desktop/tutoring"))
