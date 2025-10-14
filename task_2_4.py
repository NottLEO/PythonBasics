Gender = str(input("Bitte Geschlecht angeben (m/w): "))
Gewicht = int(input("Bitte Gewicht in kg angeben: "))

if Gender == "m":
    if Gewicht < 0 and Gewicht > 55:
        print ("Du bist in der Fliegengewichtsklasse") 
    if Gewicht > 56 and Gewicht < 66:
        print ("Du bist in der Leichtgewichtsklasse")
    if Gewicht > 67 and Gewicht < 84:
        print ("Du bist in der Mittelgewichtsklasse")
    if Gewicht > 85:
        print ("Du bist in der Schwergewichtsklasse")
        
if Gender == "w":
    if Gewicht < 0 and Gewicht > 48:
        print ("Du bist in der Fliegengewichtsklasse") 
    if Gewicht > 49 and Gewicht < 55:
        print ("Du bist in der Leichtgewichtsklasse")
    if Gewicht > 56 and Gewicht < 63:
        print ("Du bist in der Mittergewichtsklasse")
    if Gewicht > 64:
        print ("Du bist in der schwergewichtsklasse")