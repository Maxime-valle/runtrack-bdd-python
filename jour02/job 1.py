import mysql.connector

cnx = mysql.connector.connect(
    
    host='localhost', 
    user='root',  
    password='lolomax',  
    database='laplateforme'  
)

cursor = cnx.cursor()


cursor.execute("SELECT * FROM etudiant")  

results = cursor.fetchall()
for row in results:
    print(row)


cnx.close()