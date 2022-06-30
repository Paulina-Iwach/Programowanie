import os
import sys


def changeLineEnding(file: str):
    """
    Function converts line breaks in txt files from Unix to Windows
    and conversely, from Windows to Unix.
    :param file:Text file in which we want to change line breaks.
    """
    WINDOWS_ENDING = b'\r\n'
    UNIX_ENDING = b'\n'

    if not os.path.exists(file):
        raise ValueError("File doesn't exist.")

    elif not '.txt' in file:
        raise ValueError("File must have the .txt extension.")

    with open(file, 'rb') as open_file:
        content = open_file.read()

    if not WINDOWS_ENDING in content:
        content = content.replace(UNIX_ENDING, WINDOWS_ENDING)
        with open(file, 'wb') as open_file:
            open_file.write(content)
    else:
        content = content.replace(WINDOWS_ENDING, UNIX_ENDING)
        with open(file, 'wb') as open_file:
            open_file.write(content)
    print("End line character has been changed.")


# changeLineEnding("C:/Users/Artur/Desktop/wf.txt")
changeLineEnding(sys.argv[1])
