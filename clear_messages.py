import os
from colorama import Fore

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

while(True):
    print(Fore.RED + "Delete ALL messages? (y or n)")
    inp = input("")
    if inp == "y":
        os.remove("app/database.db")
        raise SystemExit
    elif inp == "n":
        raise SystemExit
    clear()
    