def wochentag(t, m, j):
    if m <= 2:
        m += 12
        j -= 1
   
    c = j // 100
    j = j % 100
   
    h = ( (26 * m - 2) // 10 + t + j + j // 4 + c // 4 - 2 * c ) % 7
   
    if h < 0:
        h += 7
   
    return h
 
tage = ["Sonntag", "Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag"]
 
t_in, m_in, j_in = map(int, input("Tag, Monat, Jahr (z.B. 25 10 2021): ").split())
 
h_wert = wochentag(t_in, m_in, j_in)
 
print(f"Der {t_in:02d}.{m_in:02d}.{j_in} ist ein {tage[h_wert]}.")