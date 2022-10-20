import os.path
import sqlite3


class User:
    def __init__(self, name, firstName, height):
        self.name = name
        self.firstName = firstName
        self.height = height


class BmiCalculator:
    '''BMI Rechner'''

    def __init__(self):
        '''init des Rechners'''
        self.dataspace = {}
        if not os.path.exists("bmi.db"):
            connection = sqlite3.connect("bmi.db")
            cursor = connection.cursor()
            cursor.execute('''CREATE TABLE bmirechner(name TEXT, firstName TEXT, bmi REAL)''')
        else:
            connection = sqlite3.connect("bmi.db")
            cursor = connection.cursor()
            cursor.execute('''SELECT name, firstName, bmi FROM bmirechner''')
            rows = cursor.fetchall()
            for row in rows:
                name = row[0]
                bmi = row[2]
                if name in self.dataspace:
                    bmis = self.dataspace[name]
                else:
                    bmis = []
                bmis.append(bmi)
                self.dataspace.update({name: bmis})

    def calculate(self, hg, wg):
        '''Berechnungsfunktion'''
        return round(float(wg) / (float(hg) ** 2), 2)

    def analyse(self, b):
        '''Analyse der Berechnung'''
        if b >= 25:
            return"Overweight"
        elif b < 18.5:
            return "Underweight"
        else:
            return "Normalweight"

    def adding(self, n, f, b):
        '''hinzufühgen der Daten in ein Datenspeicher'''
        if n in self.dataspace:
            bmis = self.dataspace[n]
        else:
            bmis = []
        bmis.append(b)
        self.dataspace.update({n: bmis})
        connection = sqlite3.connect("bmi.db")
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO bmirechner VALUES (?,?,?)''', (n, f, b))
        connection.commit()
        connection.close()
