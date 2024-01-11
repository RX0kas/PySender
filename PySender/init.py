from os import system as execute

print("\033[34mInitiation of the installation of the lib")
print("Updating pip...\033[0m")
execute("python -m pip install --upgrade pip")
print("\033[34mInstallation of pyClamd \033[0m")
execute("pip install pyClamd")
print("\033[92mInstallation Done\033[0m")

print("\033[92mAll Installation Done")
print("\033[34mStarting for the first time...\033[0m")
execute("python PySender.py")
