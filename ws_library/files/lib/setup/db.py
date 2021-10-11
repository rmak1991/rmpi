import mysql.connector
cnx = mysql.connector.connect(user='root@localhost',
                             password='root',
                             host='localhost',
                             database='library')
cursor =cnx.cursor()
def executeScriptsFromFile(filename):
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')
    for command in sqlCommands:
        try:
            if command.strip() != '':
                cursor.execute(command)
        except Exception as e:
            print ("Command skipped: ", e)
executeScriptsFromFile('sqlfile')
cnx.commit()