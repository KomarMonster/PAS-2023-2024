import shutil
import os
filename = input("Wprowadz nazwe pliku do skopiowania: ")
if os.path.isfile(filename):
    shutil.copy(filename, "lab1zad1.txt")
else:
    print("Ten plik nie istnieje")
