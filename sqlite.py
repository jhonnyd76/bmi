import sqlite3
import os.path

if not os.path.exists("bmi.db"):
    connection = sqlite3.connect("bmi.db")
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE bmirechner(name TEXT, bmi REAL)''')
else:
    connection = sqlite3.connect("bmi.db")
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO bmirechner VALUES (?,?)''',('Gion',22.34))
    cursor.execute('''INSERT INTO bmirechner VALUES (?,?)''',('Gion',25.54))
    cursor.execute('''SELECT name,bmi FROM bmirechner''')
    rows = cursor.fetchall()
    print(rows)
connection.close()
