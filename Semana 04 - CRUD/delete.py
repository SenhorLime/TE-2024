import mysql.connector
import datetime

connection = mysql.connector.connect (
  host = "localhost",
  user = "root",
  password = "",
  database = "te04crude"
)

dbConnection = connection.cursor()

stmt = "DELETE FROM users WHERE id = %s"
data = (6,)

dbConnection.execute(stmt, data)
connection.commit()

recordsaffected = dbConnection.rowcount

dbConnection.close()
connection.close()

print(recordsaffected, " registros alterados")