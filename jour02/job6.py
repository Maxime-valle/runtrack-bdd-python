import mysql.connector


cnx = mysql.connector.connect(
    host='localhost',  
    user='root ',  
    password='lolomax',  
    database='laplateforme'  
)


cursor = cnx.cursor()


cursor.execute("SELECT SUM(capacite) AS total_capacite FROM salle")


result = cursor.fetchone()
print(f"La capacité totale des salles est de {result[0]}")


cnx.close()