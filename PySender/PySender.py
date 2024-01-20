import os
from tkinter import ttk,Tk
from logger import Logger
import sys



LOGGER = Logger(True)


if not os.path.exists("parameter.txt"):
    LOGGER.warning("First launch detected starting init script")
    
    # Temporary
    with open("parameter.txt","w") as file:
        file.write("")
    # Temporary

    os.system("python init.py")
    os.system("md Data")


def start():
    LOGGER.log("MIT License")
    LOGGER.log("Copyright (c) 2024 ninjagoku4560")
    root = Tk()
    root.title("PySender v0.0.1")

    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="PySender").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()



if __name__ == "__main__":
    start()
 