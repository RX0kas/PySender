import os

print("MIT License")
print("Copyright (c) 2024 ninjagoku4560")

if not os.path.exists("Data"):
    print("First launch detected starting init script")
    os.system("python init.py")
    os.system("md Data")
    