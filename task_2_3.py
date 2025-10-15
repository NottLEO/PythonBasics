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

if wert1 > wert2 and wert2 > wert3:
    max_wert = wert1
elif wert3 > wert2:
        max_wert = wert3

print("Der grösste Wert ist:", max_wert)

#in zeile 16 weiss der computer nicht mit was er vergleichen soll, da ich kein vergleichsoperator benutzt habe.
#in zeile 18 fehlt ein else if (elif) damit der computer weiss was er vergleichen soll.