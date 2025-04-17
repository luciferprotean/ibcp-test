import sqlite3
import tkinter as tk
connection = sqlite3.connect('test.db')
cursor = connection.cursor()
firstnamevar = "Nikhil"
query1="""SELECT * FROM player WHERE player_firstname=?"""
cursor.execute(query1, (firstnamevar,))
mySQList = cursor.fetchall()
print(mySQList)
window = tk.Tk()
label = tk.Label(
    text=mySQList,
    fg="white",
    bg="black",
    width=50,
    height=30
)
label.pack()
window.mainloop()

