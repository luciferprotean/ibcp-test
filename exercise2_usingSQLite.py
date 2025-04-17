import sqlite3
connection = sqlite3.connect('test.db')
cursor = connection.cursor()
firstnamevar = "Nikhil"
query1="""SELECT * FROM player WHERE player_firstname=?"""
cursor.execute(query1, (firstnamevar,))
mySQList = cursor.fetchall()
print(mySQList)

