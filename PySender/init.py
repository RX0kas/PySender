from calendar import FRIDAY
from os import system as execute

print("\033[34mInitiation of the installation of the lib")
print("Updating pip...\033[0m")
execute("python -m pip install --upgrade pip")

print("\033[34mInstallation of pyClamd \033[0m")
execute("pip install pyClamd")
execute("pip install -U pyClamd")
print("\033[92mInstallation Done\033[0m")

print("\033[34mInstallation of tkinter \033[0m")
execute("pip install tk") 
execute("pip install -U tk")
print("\033[92mInstallation Done\033[0m")

print("\033[92mAll Installation Done")
print("\033[34mStarting the parameter creation script...")
from parameter import first_start
first_start()

print("Starting for the first time...\033[0m")
execute("python PySender.py")
