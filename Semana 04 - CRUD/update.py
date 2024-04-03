import mysql.connector
import datetime

connection = mysql.connector.connect (
  host = "localhost",
  user = "root",
  password = "",
  database = "te04crude"
)

dbConnection = connection.cursor()

stmt = "UPDATE users SET name = %s, email = %s WHERE id = %s"
data = (
  'Primeiro Usuario',
  'primeriousuariomudado@teste.com.br',
  5
)

dbConnection.execute(stmt, data)
connection.commit()

recordaffected = dbConnection.rowcount

dbConnection.close()
connection.close()

print(recordaffected, "registros alterados")