import os.path
import sqlite3

class User:
    def __init__(self):
        self.name = input("Name: ")
        self.height = input("Körpergrösse: ")

class BmiCalculator:
    '''BMI Rechner'''
    def __init__(self):
        '''init des Rechners'''
        self.dataspace = {}
        if not os.path.exists("bmi.db"):
            connection = sqlite3.connect("bmi.db")
            cursor = connection.cursor()
            cursor.execute('''CREATE TABLE bmirechner(name TEXT, bmi REAL)''')
        else:
            connection = sqlite3.connect("bmi.db")
            cursor = connection.cursor()
            cursor.execute('''SELECT name, bmi FROM bmirechner''')
            rows = cursor.fetchall()
            for row in rows:
                name = row[0]
                bmi = row[1]
                if name in self.dataspace:
                    bmis = self.dataspace[name]
                else:
                    bmis = []
                bmis.append(bmi)
                self.dataspace.update({name:bmis})
        for i in self.dataspace.items():
            print(i)

    def calculate(self, hg):
        '''Berechnungsfunktion'''
        weight = input("Gewicht in kg: ")
        if not weight:
            return
        return round(float(weight) / (float(hg) ** 2),2)

    def analyse(self, b):
        '''Analyse der Berechnung'''
        if b >= 25:
            print(str(b) + " = Overweight")
        elif b < 18.5:
            print(str(b) +" = Underweight")
        else:
            print(str(b) + " = Normalweight")

    def adding(self, n, b):
        '''hinzufühgen der Daten in ein Datenspeicher'''
        if n in self.dataspace:
            bmis=self.dataspace[n]
        else:
            bmis =[]
        bmis.append(b)
        self.dataspace.update({n:bmis})
        connection = sqlite3.connect("bmi.db")
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO bmirechner VALUES (?,?)''',(n,b))
        connection.commit()
        connection.close()


    def output(self):
        '''Ausgabe der Berechnung'''
        for i in self.dataspace.items():
            print(i)


