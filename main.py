from data_import import faecherliste, schuelernamensliste, jahr_halbjahr_klasse

dateipfad = "/Users/georgsteiner1987/notenanalyse/notenanalyse/noten_10a.xlsx"

print(jahr_halbjahr_klasse(dateipfad))
print(schuelernamensliste(dateipfad))
print(faecherliste(dateipfad))