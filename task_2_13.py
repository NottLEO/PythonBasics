import random
import time

def wuerfeln():
    return random.randint(1, 6)

def spielzug_spieler(name):
    rundenpunkte = 0
    while True:
        wurf = wuerfeln()
        print(f"{name} würfelt eine {wurf}.")
        if wurf == 1:
            print("Oh nein! Eine 1! Alle in dieser Runde erspielten Punkte sind verloren.\n")
            rundenpunkte = 0
            break
        else:
            rundenpunkte += wurf
            print(f"Aktuelle Rundepunkte: {rundenpunkte}")
            entscheidung = input("Willst du weiterwürfeln (w) oder sichern (s)? ").lower()
            if entscheidung == "s":
                print(f"{name} sichert {rundenpunkte} Punkte.\n")
                break
    return rundenpunkte

def spielzug_computer(gesicherte_punkte, ziel):
    rundenpunkte = 0
    print("Computer ist am Zug...")
    time.sleep(1)
    while True:
        wurf = wuerfeln()
        print(f"Computer würfelt eine {wurf}.")
        time.sleep(0.8)
        if wurf == 1:
            print("Computer hat eine 1 gewürfelt! Runde verloren.\n")
            rundenpunkte = 0
            break
        else:
            rundenpunkte += wurf
            # einfache Strategie: Computer sichert, wenn er mind. 20 Punkte in der Runde hat oder nahe dem Ziel ist
            if rundenpunkte >= 20 or gesicherte_punkte + rundenpunkte >= ziel:
                print(f"Computer sichert {rundenpunkte} Punkte.\n")
                break
    return rundenpunkte

def spiel():
    print("🎲 Willkommen beim Würfelspiel gegen den Computer! 🎲")
    name = input("Bitte gib deinen Namen ein: ")
    ziel = int(input("Bitte gib die Zielpunktzahl ein (z.B. 100): "))
    print()

    # zufällig entscheiden, wer beginnt
    aktueller_spieler = random.choice(["spieler", "computer"])
    print(f"Zufall entscheidet: {name if aktueller_spieler == 'spieler' else 'Computer'} beginnt!\n")

    punkte_spieler = 0
    punkte_computer = 0

    # Hauptspiel-Schleife
    while punkte_spieler < ziel and punkte_computer < ziel:
        if aktueller_spieler == "spieler":
            print(f"--- {name} ist am Zug ---")
            punkte_spieler += spielzug_spieler(name)
            print(f"{name}: {punkte_spieler} Punkte | Computer: {punkte_computer}\n")
            aktueller_spieler = "computer"
        else:
            print("--- Computer ist am Zug ---")
            punkte_computer += spielzug_computer(punkte_computer, ziel)
            print(f"{name}: {punkte_spieler} Punkte | Computer: {punkte_computer}\n")
            aktueller_spieler = "spieler"

    # Gewinner ausgeben
    if punkte_spieler >= ziel:
        print(f"🎉 Herzlichen Glückwunsch, {name}! Du hast mit {punkte_spieler} Punkten gewonnen! 🎉")
    else:
        print(f"💻 Der Computer hat mit {punkte_computer} Punkten gewonnen. Versuch es nochmal!")

# Start
if __name__ == "__main__":
    spiel()
