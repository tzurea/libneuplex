import sqlite3
import json
from datetime import date

con = sqlite3.connect("/home/azine/dist/scripts/enentrance/peadailycap/qn.db")
cur = con.cursor()

cur.execute("SELECT * from dtable")
questions = cur.fetchall()

for value in questions:
    if value[0] == str(date.today()):
        print(value)
        lst = value[1]
        
count = 1
for index,talue in enumerate(json.loads(lst)):
    print(talue)
    string = "SELECT * FROM qn WHERE id=" + str(talue) +";"
    print(string)
    cur.execute(string)
    output = cur.fetchall()
    print(count)
    print(output[0][4])
    print()
    print(output[0][5])
    print()
    print(output[0][6])
    print()
    print(output[0][7])
    print()
    print(output[0][8])
    print()
    val = input(">")
    count = count + 1
