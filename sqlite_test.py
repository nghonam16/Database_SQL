import sqlite3


# Create a new SQLite database (or connect to an existing one)
with sqlite3.connect("employees.db") as conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")
    print(cur.fetchall())