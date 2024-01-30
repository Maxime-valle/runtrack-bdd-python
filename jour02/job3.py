import mysql.connector


cnx = mysql.connector.connect(
    host='localhost',  
    user='root', 
    password='lolomax',  
    database='laplateforme' 
)
 
cursor = cnx.cursor()

cursor.execute(
"INSERT INTO salle (nom, id_etage, capacite)VALUES('Lounge', 1, 100),('Studio Son', 1, 5),('Broadcasting', 2, 50),('Bocal Peda', 2, 4),('Coworking', 2, 80),('Studio Video', 2, 5);"
)

cursor.execute(
"INSERT INTO salle (nom, id_etage, capacite)VALUES('Lounge', 1, 100),('Studio Son', 1, 5),('Broadcasting', 2, 50),('Bocal Peda', 2, 4),('Coworking', 2, 80),('Studio Video', 2, 5);"
)
cnx.commit()
cursor.close()
cnx.close()

 
 
 