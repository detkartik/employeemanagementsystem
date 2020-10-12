CREATE TABLE Employees (
id INTEGER NOT NULL PRIMARY KEY,
managerId INTEGER REFERENCES employees(id), 
name VARCHAR(30) NOT NULL
);

INSERT INTO Employees(id, managerId, name) VALUES(1, NULL, 'RG');
INSERT INTO Employees(id, managerId, name) VALUES(2, 1, 'PD');
INSERT INTO Employees(id, managerId, name) VALUES(3, 2, 'Kartik');
INSERT INTO Employees(id, managerId, name) VALUES(4, 2, 'Imman');