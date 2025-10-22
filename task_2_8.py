import os

def quersumme(zahl: int) -> int:
    """Berechnet die Quersumme einer ganzen Zahl."""
    return sum(int(z) for z in str(abs(zahl)))

def teilbarkeitspruefung():
    while True:
        # Zahl einlesen
        eingabe = input("Bitte eine ganze Zahl eingeben: ")
        try:
            zahl = int(eingabe)
        except ValueError:
            print("Ungültige Eingabe! Bitte eine ganze Zahl eingeben.\n")
            continue

        # Quersumme berechnen
        qs = quersumme(zahl)
        print(f"\nDie Quersumme von {zahl} ist {qs}.")

        # Teilbarkeitsregeln prüfen
        if qs % 9 == 0:
            print(f"→ {zahl} ist durch 9 und somit auch durch 3 teilbar.")
        elif qs % 3 == 0:
            print(f"→ {zahl} ist durch 3, aber nicht durch 9 teilbar.")
        else:
            print(f"→ {zahl} ist weder durch 3 noch durch 9 teilbar.")

        # Wiederholen?
        antwort = input("\nMöchtest du eine weitere Zahl prüfen? (j/n): ").strip().lower()
        if antwort == "j":
            # Bildschirm löschen
            os.system("cls" if os.name == "nt" else "clear")
        else:
            print("\nProgramm beendet. Auf Wiedersehen!")
            break

# Startpunkt des Programms
if __name__ == "__main__":
    teilbarkeitspruefung()
