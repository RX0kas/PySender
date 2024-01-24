# coding: utf-8
from os import system as execute
from os import path,makedirs
from PySender import LOGGER


LOGGER.log("Starting the parameter creation script...")
from parameter import first_start
first_start()

###################################
LOGGER.log("Initiation of the installation of the lib")
LOGGER.log("Updating pip...")
execute("python -m pip install --upgrade pip")

LOGGER.log("Installation of pyClamd")
execute("pip install pyClamd")
execute("pip install -U pyClamd")
LOGGER.log("Installation Done")

LOGGER.log("Installation of tkinter")
execute("pip install tk") 
execute("pip install -U tk")
LOGGER.log("Installation Done")

LOGGER.log("All Installation Done")
###################################
LOGGER.log("Starting the folder creation script...")
if not path.exists("LOG"):
        LOGGER.log("The folder 'LOG' was create")
LOGGER.log("Creation Done")
###################################

LOGGER.log("Starting for the first time...")
execute("python PySender.py True")
