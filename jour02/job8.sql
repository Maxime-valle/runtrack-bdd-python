CREATE DATABASE IF NOT EXISTS zoo;
USE zoo;


CREATE TABLE IF NOT EXISTS animal (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    race VARCHAR(255),
    id_cage INT,
    date_naissance DATE,
    pays_origine VARCHAR(255)
);


CREATE TABLE IF NOT EXISTS cage (
    id INT AUTO_INCREMENT PRIMARY KEY,
    superficie DECIMAL(10, 2),
    capacite_max INT
);


INSERT INTO cage (superficie, capacite_max) VALUES (50.0, 10), (30.0, 5);

INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) 
VALUES 
    ('peroquet', 'Africain', 1, '2020-01-01', 'Afrique'),
    ('Ours', 'Grizzly', 2, '2019-05-15', 'Amérique du sud');
