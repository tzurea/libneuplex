import sqlite3
import json
from datetime import date

con = sqlite3.connect("/home/azine/dist/scripts/enentrance/peadailycap/qn.db")
cur = con.cursor()

cur.execute("SELECT * from dtable")
questions = cur.fetchall()

for value in questions:
    if value[0] == str(date.today()):
        last = value[1]

print(str(date.today()))      
print()

count = 1
for index,talue in enumerate(json.loads(last)):
    string = "SELECT * FROM qn WHERE id=" + str(talue) +";"
    cur.execute(string)
    output = cur.fetchall()
    print(str(count) + "." + output[0][4])
    print()
    print(output[0][5])
    print()
    print(output[0][6])
    print()
    print(output[0][7])
    print()
    print(output[0][8])
    print()
    count = count + 1
