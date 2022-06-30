import matplotlib.pyplot as plt
import numpy as np
import random
import os
import glob
from PIL import Image
from pathlib import Path

x_steps = [30]
y_steps = [30]
fig = plt.figure(figsize=(6, 6), dpi=100)


def createGif():
    """
    Function creates gif from photos.
    """
    # filepaths
    fp_in = "frames/*.png"
    fp_out = "agent.gif"

    files = list(filter(os.path.isfile, glob.glob(fp_in)))
    files.sort(key=lambda x: os.path.getmtime(x))

    # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
    img, *imgs = [Image.open(f) for f in files]
    img.save(fp=fp_out, format='GIF', append_images=imgs,
             save_all=True, duration=100, loop=1)


def deleteFrames():
    """
    Function deletes all pictures created earlier by calling the gif-creating function.
    This is needed to create a new gif with the same name.
    """
    count = 0
    Path("frames").mkdir(parents=True, exist_ok=True)
    while not os.path.isfile("frames/[0-9].png"):
        try:
            os.remove("frames/" + str(count) + ".png")
            count += 1
        except FileNotFoundError:
            if count != 0:
                print("Files deleted!")
            break


def randomWalk(count):
    """
    Function moves agent by the vector drawn from the MOVES list and adds new agent position to the list.
    :param count: numbering the photos needed to create a gif.
    """
    MOVES = [(5, 0), (0, 5), (0, -5), (-5, 0)]
    go = random.choice(MOVES)
    position = [x_steps[-1] + go[0], y_steps[-1] + go[1]]
    x_steps.append(position[0])
    y_steps.append(position[1])
    createBoard(x_steps, y_steps, count)


def createBoard(x_coordinates, y_coordinates, count):
    """
    Function creates a grid on which the agent moves.
    :param x_coordinates: list with the agent's movements along the x axis.
    :param y_coordinates: list with the agent's movements along the y axis.
    :param count: numbering the photos needed to create a gif.
    """
    ax = fig.add_subplot(1, 1, 1)

    minor_ticks = np.arange(0, 61, 5)

    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(minor_ticks, minor=True)
    ax.set_ylim([0, 60])
    ax.set_xlim([0, 60])

    # And a corresponding grid
    ax.grid(which='both')
    plt.plot(x_coordinates[-1], y_coordinates[-1], 'ro')  # rysuje aktualne położenie agenta
    plt.plot(x_coordinates, y_coordinates, 'hotpink')  # łączy x i y linią

    fig.savefig('frames/' + str(count) + '.png')
    plt.clf()

    count += 1


def start():
    """
    Auxiliary function.
    It moves agent until it touches the wall. Then it creates a gif.
    """
    deleteFrames()
    count = 0
    while x_steps[-1] != 60 and y_steps[-1] != 60 and x_steps[-1] != 0 and y_steps[-1] != 0:
        randomWalk(count)
        count += 1
    createGif()
    print("Gif created.")


start()
