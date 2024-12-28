import pyodbc

drivers = pyodbc.drivers()
print("Available ODBC Drivers:")
for driver in drivers:
    print(driver)

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=your_server;'
    'DATABASE=your_database;'
    'UID=your_username;'
    'PWD=your_password'
)

