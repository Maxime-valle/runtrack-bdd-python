import mysql.connector

class Employe:
    def __init__(self, host, user, password):
        self.cnx = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.cursor = self.cnx.cursor()

    def create_database(self, database):
        self.cursor.execute(f"DROP DATABASE IF EXISTS {database}")
        self.cursor.execute(f"CREATE DATABASE {database}")
        self.cnx.database = database

    def create_table(self, table, fields):
        fields_str = ', '.join(fields)
        self.cursor.execute(f"CREATE TABLE {table} ({fields_str})")

    def insert_data(self, table, data):
        for row in data:
            values = ', '.join([f"'{v}'" if isinstance(v, str) else str(v) for v in row])
            self.cursor.execute(f"INSERT INTO {table} VALUES ({values})")
        self.cnx.commit()

    def select_data(self, table, condition=None):
        self.cursor.execute(f"SELECT * FROM {table}" + (f" WHERE {condition}" if condition else ""))
        return self.cursor.fetchall()

    def update_data(self, table, set_values, condition=None):
        set_str = ', '.join([f"{key} = '{value}'" if isinstance(value, str) else f"{key} = {value}" for key, value in set_values.items()])
        self.cursor.execute(f"UPDATE {table} SET {set_str}" + (f" WHERE {condition}" if condition else ""))
        self.cnx.commit()

    def delete_data(self, table, condition=None):
        self.cursor.execute(f"DELETE FROM {table}" + (f" WHERE {condition}" if condition else ""))
        self.cnx.commit()

    def close(self):
        self.cnx.close()


employe = Employe('localhost', 'root', 'lolomax')

employe.create_database('laplateforme')
employe.create_table('employe', ['id INT AUTO_INCREMENT PRIMARY KEY', 'nom VARCHAR(255)', 'prenom VARCHAR(255)', 'salaire DECIMAL(10, 2)', 'id_service INT'])
employe.create_table('service', ['id INT AUTO_INCREMENT PRIMARY KEY', 'nom VARCHAR(255)'])


employe.insert_data('employe', [(1, 'francis', 'kevin', 3500.00, 1), (2, 'willy', 'max', 2500.00, 2)])
employe.insert_data('service', [(1, 'Service 1'), (2, 'Service 2')])


results = employe.select_data('employe', 'salaire > 3000')
for row in results:
    print(row)


employe.update_data('employe', {'salaire': 4000.00}, 'id = 1')


employe.delete_data('employe', 'id = 2')


results = employe.select_data('employe')
for row in results:
    service = employe.select_data('service', f'id = {row[4]}')[0]
    print(f"Employé: {row[1]} {row[2]}, Service: {service[1]}")

employe.close()

