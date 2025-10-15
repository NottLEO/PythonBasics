monat = int(input("Geben Sie einen Monat ein (1-12): "))


match  monat:    
    case 12 | 1| 2:
        print("Winter")
    case 3 | 4 | 5:
        print("Frühling")    
    case 6 | 7 | 8:
        print("Sommer")
    case 9 | 10 | 11:
        print("Herbst")
