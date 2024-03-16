#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sqlite3
import time

# Connect to the database (or create it if not exists)
conn = sqlite3.connect('mydatabase.db')

# Create a table called "Ages"
conn.execute('''CREATE TABLE IF NOT EXISTS Ages (
                      name VARCHAR(128),
                      age INTEGER
                )''')

# Delete any existing rows
conn.execute("DELETE FROM Ages")

# Insert rows into the table
conn.execute("INSERT INTO Ages (name, age) VALUES ('Mara', 28)")
conn.execute("INSERT INTO Ages (name, age) VALUES ('Otto', 33)")
conn.execute("INSERT INTO Ages (name, age) VALUES ('Fyn', 31)")
conn.execute("INSERT INTO Ages (name, age) VALUES ('Neshawn', 17)")

# Commit the changes
conn.commit()

# Select hex encoded values
try:
    cursor = conn.execute("SELECT hex(name || age) AS X FROM Ages ORDER BY X")
    rows = cursor.fetchall()
    for row in rows:
        print(row[0])
except sqlite3.OperationalError as e:
    print("Error:", e)
    print("Retrying after 1 second...")
    time.sleep(1)
    # Attempt query again
    cursor = conn.execute("SELECT hex(name || age) AS X FROM Ages ORDER BY X")
    rows = cursor.fetchall()
    for row in rows:
        print(row[0])

# Close the connection
conn.close()


# In[ ]:




