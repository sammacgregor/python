import pyodbc 
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=SAM-DESKTOP;"
                      "Database=sandbox;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()
cursor.execute('SELECT * FROM Table')

for row in cursor:
    print('row = %r' % (row,))