import sqlite3
con = sqlite3.connect('employee.db')
print("Database Connected")

cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS Employees(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, address TEXT)')

con.commit()
con.close()