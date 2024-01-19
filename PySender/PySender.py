import os

import tkinter as tk
from logger import logger

LOGGER = logger(True)

LOGGER.log("MIT License")
LOGGER.log("Copyright (c) 2024 ninjagoku4560")

if not os.path.exists("Data"):
    LOGGER.log("First launch detected starting init script")
    os.system("python init.py")
    os.system("md Data")

class app(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
 
