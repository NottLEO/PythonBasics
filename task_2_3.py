anzahl = 1
wert1 = 0
wert2 = 0
wert3 = 0
max_wert = 0
wert1 = float(input("Wert " + str(anzahl) + ": "))
anzahl += 1

wert2 = float(input("Wert " + str(anzahl) + ": "))
anzahl += 1
wert3 = float(input("Wert " + str(anzahl) + ": "))
anzahl += 1
if wert1 > wert2 and > wert3:
    max_wert = wert1
else wert3 > wert2:
        max_wert = wert3

print("Der grösste Wert ist:", max_wert)