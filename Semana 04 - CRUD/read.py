import mysql.connector
import datetime

connection = mysql.connector.connect (
  host = "localhost",
  user = "root",
  password = "",
  database = "te04crude"
)

dbConnection = connection.cursor()

stmt = "SELECT * FROM users"

dbConnection.execute(stmt)
results = dbConnection.fetchall()


dbConnection.close()
connection.close()

for result in results:
  print(result)
