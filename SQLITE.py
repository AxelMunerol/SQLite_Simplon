import sqlite3
import csv

# Connexion à la base de données
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# (Optionnel) Suppression de la table Clients si elle existe
cursor.execute('DROP TABLE IF EXISTS Clients')
cursor.execute('DROP TABLE IF EXISTS Commandes')

# Création de la table Clients si elle n'existe pas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        prenom TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        date_inscription DATE
    )
''')

# Insertion de plusieurs lignes dans la table Clients
cursor.execute('''
    INSERT INTO Clients (nom, prenom, email, date_inscription)
    VALUES 
        ('Ricard', 'Bob', 'Bob.ricard@gmail.com', '2022-01-21'),
        ('Jeanne', 'Darc', 'Jeanne.darc@lycos.com', '2022-01-22')
''')

# Création de la table Commandes si elle n'existe pas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Commandes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER,
        produit TEXT NOT NULL,
        date_commande DATE NOT NULL,
        FOREIGN KEY (client_id) REFERENCES Clients(id)
    )
''')

# Insertion de plusieurs lignes dans la table Commandes
cursor.execute('''
    INSERT INTO Commandes (client_id, produit, date_commande)
    VALUES 
        (1, 'Alcool', '2023-01-01'),
        (1, 'Robe', '2023-01-22'),
        (2, 'Buchet', '2024-02-12')
''')
print('Tous les clients :')
cursor.execute('''
    SELECT * from Clients
''')
clients = cursor.fetchall()

# Affichage des résultats
for client in clients:
    print(client)
print('--------------------')
print('Toutes les commandes de l id client 1 ')


cursor.execute('''
    SELECT * from Commandes WHERE client_id = 1
''')
clients = cursor.fetchall()

# Affichage des résultats
for client in clients:
    print(client)

print('--------------------')

print('MAJ d un mail ')
cursor.execute('''
    UPDATE Clients
    SET email = 'RicardLover@caramail.com'
    where id = 1 
''')
cursor.execute('''
    select email from clients where id = 1
''')
clients = cursor.fetchall()

# Affichage des résultats
for client in clients:
    print(client)

print('--------------------')
print('Suppression dune commande')


cursor.execute('''
    delete from Commandes WHERE id = 2
''')

cursor.execute('''
    select * from Commandes WHERE client_id = 1
''')
clients = cursor.fetchall()

# Affichage des résultats
for client in clients:
    print(client)

print('--------------------')


# Sauvegarde des changements


conn.commit()


# Récupération des données de la table Clients
cursor.execute('SELECT * FROM Clients')
clients = cursor.fetchall()

# Écriture des données dans le fichier CSV
with open('Clients.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)

    # Écriture des lignes de données
    writer.writerows(clients)

print('Données exportées avec succès dans Clients.csv')


# Récupération des données de la table Clients
cursor.execute('SELECT * FROM Commandes')
commandes = cursor.fetchall()

# Écriture des données dans le fichier CSV
with open('Commandes.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)

    # Écriture des lignes de données
    writer.writerows(commandes)

print('Données exportées avec succès dans Ccommandes.csv')
# Fermeture de la connexion
conn.close()


