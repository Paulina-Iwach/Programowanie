from tkinter import *
from numpy import *
import sys
import matplotlib.pyplot as plt
import math


def endProgram():
    """
    Function terminates the program.
    """
    sys.exit()


def get_data():
    """
    Function gets the ranges of x-axis and y-axis from the user.
    """
    if "," in e_x.get() and "," in e_y.get():
        try:
            axis_range = []
            axis_range.append(float(e_x.get().split(",")[0]))
            axis_range.append(float(e_x.get().split(",")[1]))
            axis_range.append(float(e_y.get().split(",")[0]))
            axis_range.append(float(e_y.get().split(",")[1]))
            l_error.config(text="")
            return axis_range
        except ValueError:
            l_error.config(text="Axis ranges must be numbers!")
    else:
        l_error.config(text="Separate numbers by semicolon!")


def get_formula():
    """
    Function gets the formulas of mathematical functions from the user.
    :return: List with function formulas.
    """
    formula = e_formula.get().replace("^", "**")
    formula = formula.replace(" ", "")
    formula = formula.split(";")
    formula = [i + "+x*0" for i in formula]
    return formula


def draw_function():
    """
    Function draws graphs from the data provided by the user.
    """
    axis_range = get_data()
    formula = get_formula()

    x = arange(axis_range[0], axis_range[1], 0.1)

    axes = plt.gca()
    try:
        for i in formula:
            plt.plot(x, eval(i[2:]))

    except:
        l_error.config(text="Invalid function formula!")
        return 0

    axes.spines['right'].set_color('none')
    axes.spines['top'].set_color('none')
    axes.xaxis.set_ticks_position('bottom')
    axes.spines['bottom'].set_position(('data', 0))  #
    axes.yaxis.set_ticks_position('left')
    axes.spines['left'].set_position(('data', 0))  #
    axes.set_ylim(axis_range[2], axis_range[3])
    axes.grid(True)

    formula = [i.replace("**", "^") for i in formula]
    formula = [i[:-4] for i in formula]
    if int(var.get()): plt.legend(['$' + i + '$' for i in formula])
    plt.title(e_title.get())
    plt.savefig('wykres.png')

    img = PhotoImage(file="wykres.png")
    l_graph.config(image=img)
    l_graph.image = img
    plt.clf()


width = 1100
height = 620
root = Tk()
root.title("figure generator")
root.geometry(f"{width}x{height}")
root.iconbitmap("icon.ico")

img = PhotoImage(file="function.png")

FONT = "Arial"
FONTSIZE = 16
BG_COLOUR = "misty rose"

# Top frame, begin
mainFrame = Frame(root, bg=BG_COLOUR)
mainFrame.pack(fill="both", expand="True")

lWelcome = Label(mainFrame, text="FIGURE GENERATOR", font=(FONT, FONTSIZE), bg=BG_COLOUR)
lWelcome.pack(side=TOP, padx=10, pady=10)

# center
frameCenter = Frame(mainFrame, bg="pink")
frameCenter.pack(fill="both", expand="True")

frameLeft = Frame(frameCenter, bg=BG_COLOUR)
frameLeft.pack(fill="both", expand="True", side=LEFT)

l_formula = Label(frameLeft, text="Enter functions:", font=(FONT, FONTSIZE), bg=BG_COLOUR)
l_formula.pack()

e_formula = Entry(frameLeft, font=(FONT, FONTSIZE), width=30, relief=GROOVE)
e_formula.insert(END, "y=x+2")
e_formula.pack()

l_title = Label(frameLeft, text="Title:", font=(FONT, FONTSIZE), bg=BG_COLOUR)
l_title.pack()

e_title = Entry(frameLeft, font=(FONT, FONTSIZE), width=30, relief=GROOVE)
e_title.pack()

l_empty = Label(frameLeft, font=(FONT, FONTSIZE), bg=BG_COLOUR)
l_empty.pack()

l_x = Label(frameLeft, text="x range:", font=(FONT, FONTSIZE), bg=BG_COLOUR, )
l_x.pack()

e_x = Entry(frameLeft, font=(FONT, FONTSIZE), relief=GROOVE, justify="center")
e_x.insert(END, "-5,10")
e_x.pack()

l_y = Label(frameLeft, text="y range:", font=(FONT, FONTSIZE), bg=BG_COLOUR)
l_y.pack()

e_y = Entry(frameLeft, font=(FONT, FONTSIZE), relief=GROOVE, justify="center")
e_y.insert(END, "-5,10")
e_y.pack()

l_empty2 = Label(frameLeft, font=(FONT, FONTSIZE), bg=BG_COLOUR)
l_empty2.pack()

var = IntVar()
check_legend = Checkbutton(frameLeft, text="Legend", font=(FONT, FONTSIZE), variable=var, bg=BG_COLOUR, )
check_legend.pack()
check_legend.select()

l_empty3 = Label(frameLeft, bg=BG_COLOUR, font=(FONT, FONTSIZE))
l_empty3.pack()

b_draw = Button(frameLeft, text="Draw", font=(FONT, FONTSIZE), bg="light cyan", width=8, command=draw_function)
b_draw.pack()

frameRight = Frame(frameCenter, bg=BG_COLOUR)
frameRight.pack(fill="both", expand="True", side=RIGHT)

l_graph = Label(frameRight, image=img, height=480, width=640, bg=BG_COLOUR, relief=GROOVE, borderwidth=2)
l_graph.pack(expand=YES)

bEnd = Button(frameLeft, text="Quit", font=(FONT, FONTSIZE), command=endProgram, bg="light cyan", width=8,
              borderwidth=2)
bEnd.pack(padx=5, pady=20, )

l_error = Label(frameLeft, font=(FONT, FONTSIZE), bg=BG_COLOUR)
l_error.pack(pady=20)

root.mainloop()
