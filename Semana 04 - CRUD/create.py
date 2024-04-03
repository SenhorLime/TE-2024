import mysql.connector
import datetime

connection = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "",
    database = "te04crude"
)

dbConnection = connection.cursor()

stmt = "INSERT INTO users (name, email, created) VALUES (%s, %s, %s)"
data = (
    'Primeiro Usuario',
    'primeriousuario@teste.com.br',
    datetime.datetime.today()
)

dbConnection.execute(stmt, data)
connection.commit()

userid = dbConnection.lastrowid

dbConnection.close()
connection.close()

print("Foi cadastrado o novo usuario de ID: ", userid)