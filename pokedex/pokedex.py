import pygame
import json

# Charger les données depuis le fichier JSON
with open('pokedex.json') as fichier_json:
    donnees = json.load(fichier_json)

# Accéder aux données
print (donnees)
nom_pokemon = donnees [0]['nom']
print (nom_pokemon)
type_pokemon = donnees[0]['type']
stats_pokemon = donnees[0]['statistiques']

# Accéder à des statistiques spécifiques
vie_pokemon = stats_pokemon['vie']
attaque_pokemon = stats_pokemon['attaque']
defense_pokemon = stats_pokemon['defense']


# Afficher les données
print(f"Nom: {nom_pokemon}")
print(f"Type: {type_pokemon}")
print(f"Vie: {vie_pokemon}")
print(f"Attaque: {attaque_pokemon}")
print(f"Défense: {defense_pokemon}")


# Accéder aux données
nom_pokemon = donnees[1]['nom']
type_pokemon = donnees[1]['type']
stats_pokemon = donnees[1]['statistiques']

# Accéder à des statistiques spécifiques
vie_pokemon = stats_pokemon['vie']
attaque_pokemon = stats_pokemon['attaque']
defense_pokemon = stats_pokemon['defense']


# Afficher les données
print(f"Nom: {nom_pokemon}")
print(f"Type: {type_pokemon}")
print(f"Vie: {vie_pokemon}")
print(f"Attaque: {attaque_pokemon}")
print(f"Défense: {defense_pokemon}")


# Accéder aux données
nom_pokemon = donnees[2]['nom']
type_pokemon = donnees[2]['type']
stats_pokemon = donnees[2]['statistiques']

# Accéder à des statistiques spécifiques
vie_pokemon = stats_pokemon['vie']
attaque_pokemon = stats_pokemon['attaque']
defense_pokemon = stats_pokemon['defense']


# Afficher les données
print(f"Nom: {nom_pokemon}")
print(f"Type: {type_pokemon}")
print(f"Vie: {vie_pokemon}")
print(f"Attaque: {attaque_pokemon}")
print(f"Défense: {defense_pokemon}")


# Accéder aux données
nom_pokemon = donnees[3]['nom']
type_pokemon = donnees[3]['type']
stats_pokemon = donnees[3]['statistiques']

# Accéder à des statistiques spécifiques
vie_pokemon = stats_pokemon['vie']
attaque_pokemon = stats_pokemon['attaque']
defense_pokemon = stats_pokemon['defense']


# Afficher les données
print(f"Nom: {nom_pokemon}")
print(f"Type: {type_pokemon}")
print(f"Vie: {vie_pokemon}")
print(f"Attaque: {attaque_pokemon}")
print(f"Défense: {defense_pokemon}")


