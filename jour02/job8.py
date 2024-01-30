import mysql.connector

class ZooManagement:
    def __init__(self, host, user, password):
        self.cnx = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.cursor = self.cnx.cursor()

    def create_database(self, database):
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
        self.cnx.database = database

    def create_table_animal(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS animal (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nom VARCHAR(255),
                race VARCHAR(255),
                id_cage INT,
                date_naissance DATE,
                pays_origine VARCHAR(255)
            )
        """)

    def create_table_cage(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS cage (
                id INT AUTO_INCREMENT PRIMARY KEY,
                superficie DECIMAL(10, 2),
                capacite_max INT
            )
        """)

    def insert_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        self.cursor.execute("""
            INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine)
            VALUES (%s, %s, %s, %s, %s)
        """, (nom, race, id_cage, date_naissance, pays_origine))
        self.cnx.commit()

    def insert_cage(self, superficie, capacite_max):
        self.cursor.execute("""
            INSERT INTO cage (superficie, capacite_max)
            VALUES (%s, %s)
        """, (superficie, capacite_max))
        self.cnx.commit()

    def select_all_animals(self):
        self.cursor.execute("SELECT * FROM animal")
        return self.cursor.fetchall()

    def select_all_cages(self):
        self.cursor.execute("SELECT * FROM cage")
        return self.cursor.fetchall()

    def close(self):
        self.cnx.close()

host = 'localhost'
user = 'root'
password = 'lolomax'

# Création de l'instance ZooManagement
zoo_manager = ZooManagement(host, user, password)


zoo_manager.create_database('zoo')


zoo_manager.create_table_animal()
zoo_manager.create_table_cage()


zoo_manager.insert_cage(50.0, 10)
zoo_manager.insert_cage(30.0, 5)

zoo_manager.insert_animal('Lion', 'Africain nord ', 1, '2020-01-01', 'Afrique')
zoo_manager.insert_animal('Ours', 'Grizzly', 2, '2019-05-15', 'Amérique du sud')
zoo_manager.insert_animal('peroquet', 'australien', 1, '2020-01-01', 'mongolie')
zoo_manager.insert_animal('lapin ', 'croatie', 1, '2020-01-08', 'france')
zoo_manager.insert_animal('crocodile', 'Nepal', 1, '2023-10-03', 'pays-bas')
zoo_manager.insert_animal('singe', 'thaillande', 1, '2026-01-06', 'france')
zoo_manager.insert_animal('peruche', 'australien', 1, '2027-05-01', 'italie')




print("Animaux dans le zoo:")
animals = zoo_manager.select_all_animals()
for animal in animals:
    print(animal)


print("\nCages dans le zoo:")
cages = zoo_manager.select_all_cages()
for cage in cages:
    print(cage)


zoo_manager.close()
