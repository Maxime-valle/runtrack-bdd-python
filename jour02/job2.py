import mysql.connector


cnx = mysql.connector.connect(
    host='localhost',  
    user='root', 
    password='lolomax',  
    database='laplatefome' 
)


cursor = cnx.cursor()

cursor.execute(
"CREATE TABLE salle (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), id_etage INT, capacite INT)"
)

cnx.commit()
cursor.close()
cnx.close()
