import shutil
import os
filename = input("Wprowadz nazwe pliku graficznego do skopiowania: ")
if os.path.isfile(filename):
    if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):
        shutil.copy(filename, "lab1zad1.png")
    else:
        print("Plik nie jest plikiem graficznynm")
else:
    print("Ten plik nie istnieje")
