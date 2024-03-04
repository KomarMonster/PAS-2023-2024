import re

address = input("Podaj adres IP: ")
pattern = re.compile("^((25[0-5]|(2[0-4]|1\\d|[1-9]|)\\d)\\.?\\b){4}$")

if re.match(pattern, address):
    print("Adres poprawny")
else:
    print("Adres niepoprawny")
