#!/usr/local/bin/python3
from health.bmicalculator import BmiCalculator, User

user = User()
bmicalculator = BmiCalculator()
while True:
    try:
        bmi = bmicalculator.calculate(user.height)
        if not bmi:
            break
    except ValueError:
        continue
    print("BMI: ", bmi)
    print("Der berechnete BMI von " + user.name + " ist " + str(bmi))
    bmicalculator.analyse(bmi)
    bmicalculator.adding(user.name,bmi)

bmicalculator.output()