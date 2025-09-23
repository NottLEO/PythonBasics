stunden = int(input("Stunden eingeben: "))
minuten = int(input("Minuten eingeben: "))
sekunden = int(input("Sekunden eingeben: "))

# Umrechnung in Stunden (Dezimalsystem)
dezimalstunden = stunden + minuten / 60 + sekunden / 3600

print("Das entspricht:", dezimalstunden, "Stunden")