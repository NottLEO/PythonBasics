# Wenn man eine 3 und eine 5 geschrieben hat, dann ist der durchschnitt 4.0
anzahl = 0
note1 = 0.0
note2 = 0.0
note1 = float(input("Note 1:"))
anzahl += 1
note2 = float(input("Note 2:"))
anzahl += 1
schnitt = (note1 + note2) / anzahl
if schnitt >= 4:
    print("*****")
    durchschnitt = int(schnitt * 2)
    durchschnitt = (durchschnitt + 1) // 2
    if durchschnitt == 4:
        print("Typ 2")
    else:
        if durchschnitt == 5:
            print("Typ 3")
        else:
            print("Typ 4")
else:
    print("-----")
    if note1 >= 4 or note2 >= 4:
        print("Typ 1")
    else:
        print("Typ 0")