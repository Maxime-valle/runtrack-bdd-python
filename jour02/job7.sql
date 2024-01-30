CREATE DATABASE MaBaseDeDonnees;  
USE MaBaseDeDonnees;

CREATE TABLE employe (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    prenom VARCHAR(255),
    salaire DECIMAL(10, 2),
    id_service INT
);

INSERT INTO employe (nom, prenom, salaire, id_service)
    -> VALUES ('francis', 'kevin', 3500.00, 1), ('willy', 'max', 2500.00, 2);

    SELECT * FROM employe WHERE salaire > 3000;

    CREATE TABLE service (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255)
);

INSERT INTO service (nom)
VALUES ('Service 1'), ('Service 2');

SELECT e.nom, e.prenom, s.nom 
FROM employe e 
INNER JOIN service s ON e.id_service = s.id;
