def main():
    print("Zinseszins-Rechner mit Umrechnung in Erden aus purem Gold")
    startjahr = int(input("Startjahr: "))
    zieljahr = int(input("Zieljahr: "))
    betrag = float(input("Betrag (z. B. in CHF): "))
    zinssatz = float(input("Jährlicher Zinssatz in % (z. B. 5 für 5 %): "))
    
    if zieljahr <= startjahr:
        print("Fehler: Das Zieljahr muss grösser sein als das Startjahr.")
        return
    
    jahre = zieljahr - startjahr
    wachstumsfaktor = (1 + zinssatz/100) ** jahre
    endbetrag = betrag * wachstumsfaktor
    

    masse_erde_kg = 5.9722e24   
    preis_gold_pro_kg_chf = 96433.0  
    
    wert_erde_aus_gold = masse_erde_kg * preis_gold_pro_kg_chf
    
    anzahl_erden = endbetrag / wert_erde_aus_gold
    
  
    print(f"\nErgebnis nach {jahre} Jahren:")
    print(f"Endbetrag: {endbetrag:,.2f} CHF")
    print(f"Wert einer „Erde aus purem Gold“: ca. {wert_erde_aus_gold:.2e} CHF")
    print(f"Das entspricht ca. {anzahl_erden:.2e} Erden aus purem Gold.")
    
if __name__ == "__main__":
    main()
