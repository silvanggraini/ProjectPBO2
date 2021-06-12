import sqlite3, os

connection = None

try:
    connection = sqlite3.connect(os.path.abspath('data.sqlite3'))

except Exception as err:
    print(err)
    