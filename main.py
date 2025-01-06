from data_import import faecherliste, schuelernamensliste, jahr_halbjahr_klasse

dateipfad = "/Users/georgsteiner1987/Desktop/notenanalyse/noten_10a.xlsx"

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "dbrks761",
    database = "datensammlung"
)
mycursor = mydb.cursor()
mycursor.execute("select * from noten_test")

myresult = mycursor.fetchall()
for x in myresult:
  print(x)


#print(jahr_halbjahr_klasse(dateipfad))
#print(schuelernamensliste(dateipfad))
#print(faecherliste(dateipfad))
