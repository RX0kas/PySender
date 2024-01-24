import os
from tkinter import ttk,Tk,filedialog
from logger import Logger
import sys
import Send



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
    
    #########
    ip = 0 # a remplir
    port = 0 # a remplir
    Path = "" # a remplir
    ttk.Button(root,text="Send",command=Send.sendFile(IPServeur=ip,PortServeur=port,FilePath=Path)) # Bouton pour envoyer

    root.mainloop()



if __name__ == "__main__":
    start()
 