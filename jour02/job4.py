import mysql.connector


cnx = mysql.connector.connect(
    host='localhost',  
    user='root', 
    password='lolomax',  
    database='laplateforme' 
)


cursor = cnx.cursor()


cursor.execute("SELECT nom, capacite FROM salle")


results = cursor.fetchall()
print(results)


cnx.close()
    