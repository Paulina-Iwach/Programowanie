from tkinter import *
from tkinter import ttk
import sys
import requests
import json
import pickle


def downloadApi():
    """
    Function downloads api with exchange rates from the NBP website and save this data in txt file.
    :return:list with information about about currencies.
    """
    try:
        api_request = requests.get("http://api.nbp.pl/api/exchangerates/tables/c/")
        api = json.loads(api_request.content)
        a_file = open("exchange_rate.txt", "wb")
        pickle.dump(api, a_file)
        a_file.close()
    except:
        a_file = open("exchange_rate.txt", "rb")
        api = pickle.load(a_file)

    return api


def createDictionary(api):
    """
    Function creates dictionary where keys are currency abbreviations and values are exchange rates.
    :param api: list with information about about currencies.
    :return:list with currency abbreviations and exchange rates.
    """
    rates = {}
    for i in range(len(api[0]["rates"])):
        rates[api[0]["rates"][i]["code"]] = api[0]["rates"][i]["bid"]

    return rates


api = downloadApi()
rates = createDictionary(api)


def calculate():
    """
    Function checks if the entered data are positive numbers and then converts currencies.
    """
    try:
        if float(amount.get()) < 0:
            lResult.config(text="Number must be positive")
        else:
            rate1 = rates[list1.get()]
            rate2 = rates[list2.get()]
            lResult.config(text=f"{round(float(amount.get()) * rate1 / rate2, 2)} {list2.get()} ")
    except ValueError:
        lResult.config(text="Enter a number!")


def endProgram():
    """
    Function terminates the program.
    """
    sys.exit()


width = 500
height = 350
root = Tk()
root.title("Bureau de change")
root.geometry(f"{width}x{height}")
root.iconbitmap("icon.ico")

FONT = "Arial"
FONTSIZE = 14
BG_COLOUR = "misty rose"

# Top frame, begin
mainFrame = Frame(root, bg=BG_COLOUR)
mainFrame.pack(fill="both", expand="True")

lWelcome = Label(mainFrame, text="Currency converter", font=(FONT, FONTSIZE), bg=BG_COLOUR)
lWelcome.pack(side=TOP, padx=10, pady=10)

# Chosing currency
frameCenter = Frame(mainFrame, bg=BG_COLOUR)
frameCenter.pack(fill="both", expand="True")

frameLeft = Frame(frameCenter, bg=BG_COLOUR)
frameLeft.pack(fill="both", expand="True", side=LEFT)

l1 = Label(frameLeft, text="Convert from:", font=(FONT, FONTSIZE), bg=BG_COLOUR)
l1.pack()

list1 = ttk.Combobox(frameLeft, width=27, state="readonly")
list1.pack()

list1["values"] = [api[0]["rates"][i]["code"] for i in range(len(api[0]["rates"]))]
list1.current(0)

frameRight = Frame(frameCenter, bg=BG_COLOUR)
frameRight.pack(fill="both", expand="True", side=RIGHT)
l2 = Label(frameRight, text="Convert to:", font=(FONT, FONTSIZE), bg=BG_COLOUR)
l2.pack()

list2 = ttk.Combobox(frameRight, width=27, state="readonly")
list2.pack()
list2["values"] = [api[0]["rates"][i]["code"] for i in range(len(api[0]["rates"]))]
list2.current(0)

# Result
frameEnd = Frame(mainFrame, bg=BG_COLOUR)
frameEnd.pack(fill="both", expand="True", side=BOTTOM)
l3 = Label(frameEnd, text="Enter the amount:", font=(FONT, FONTSIZE), bg=BG_COLOUR)
l3.pack()

amount = Entry(frameEnd, font=(FONT, FONTSIZE), relief=GROOVE, borderwidth=5)
amount.pack()

bCalculate = Button(frameEnd, text="Convert", font=(FONT, FONTSIZE), command=calculate, bg="light cyan")
bCalculate.pack(padx=5, pady=5)

l4 = Label(frameEnd, text="Amount after conversion:", font=(FONT, FONTSIZE), bg=BG_COLOUR)
l4.pack()

lResult = Label(frameEnd, font=(FONT, FONTSIZE), borderwidth=5, width=20, height=1, relief=GROOVE)
lResult.pack()

bEnd = Button(frameEnd, text="Quit", font=(FONT, FONTSIZE), command=endProgram, bg="light cyan")
bEnd.pack(padx=5, pady=5)

root.mainloop()
