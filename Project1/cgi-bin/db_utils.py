import mysql.connector

supplyDB = mysql.connector.connect(
  host="localhost",
  user="proj",
  passwd="proj",
  database="SupplyDB",
  auth_plugin="mysql_native_password"
)

cursor = supplyDB.cursor()
