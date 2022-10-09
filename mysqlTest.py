import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(user="jhonnyd",password="Gniffi1234.",
                                  host="webdev.script-source.net",
                                  database="bmirechner")
except mysql.connect.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something  is wrong with your user name odr password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print("Error")
else:
    print("Connection OK")
    cursor = cnx.cursor()
    cursor.execute('''SELECT * FROM bmirechner.user_data''')
    rows = cursor.fetchall()
    for row in rows:
        id = row[0]
        firstname = row[1]
        lastname = row[2]
        age = row[3]
        height = row[4]
        weight = row[5]
        print(str(id) + ": " +
              firstname + " " +
              lastname + " " +
              str(age) + " " +
              str(height) + " " +
              str(weight) + " ")
    cnx.close()