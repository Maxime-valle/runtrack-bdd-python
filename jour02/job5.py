import mysql.connector


cnx = mysql.connector.connect(
    host='localhost',  
    user='root', 
    password='lolomax',  
    database='laplateforme'  
)

cursor = cnx.cursor()

cursor.execute("SELECT SUM(superficie) AS total_superficie FROM etage")


result = cursor.fetchone()
print(f"La superficie de La Plateforme est de {result[0]} m2")

cnx.close()