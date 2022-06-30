import os
from PIL import Image


def generate_miniature_jpg(file_name_in: str, size: list, file_name_out: str):
    """
    Functions generate s a thumbnail of the image in jpg format.
    :param file_name_in: Input file name.
    :param size: List that contains the dimensions of the image.
    :param file_name_out: Output file name.
    """
    if type(file_name_in) is not str or type(file_name_out) is not str:
        raise ValueError("file name type must be string.")
    elif type(size) is not list or len(size) != 2:
        raise ValueError("size type must be two element list.")
    elif not os.path.exists(file_name_in):
        raise ValueError("Image doesn't exist.")
    else:
        image = Image.open(file_name_in)
        image_resize = image.resize((size[0], size[1]))
        image_resize.save(file_name_out)


generate_miniature_jpg(r"C:\Users\Artur\Desktop\Matematyka stosowana\Programowanie\lista7\images\unicorn.png", [80,80], r"C:\Users\Artur\Desktop\Matematyka stosowana\Programowanie\lista7\images\miniunicorn.png")
