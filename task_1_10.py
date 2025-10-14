Distanz = input("Geben Sie die Distanz die sie fahren wollen in km ein: ")
Geschwindigkeit = input("Geben Sie die durchschnittliche Geschwindigkeit in km/h ein: ")
Zeit = (int(Distanz) / int(Geschwindigkeit)* 60)

Benzinverbrauch = 8 / 100
Benzin = (int(Distanz) * Benzinverbrauch) 



print(f"Der Benzinverbrauch beträgt {str(Benzin)} Liter")
print(f"Die Fahrt dauert {str(Zeit)} Minuten")