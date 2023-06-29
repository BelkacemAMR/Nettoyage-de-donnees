# Exemple Simple en python de la phase de netoyage de données dans le cadre d'une analyse de données:

import pandas as pd
import numpy as np

# Chargement des données à partir d'un fichier CSV
data = pd.read_csv('donnees_brutes.csv')

# Suppression des valeurs manquantes
data = data.dropna()

# Élimination des doublons
data = data.drop_duplicates()

# Détection des valeurs aberrantes (ici, considérons les valeurs aberrantes comme étant les points de données situés à plus de 3 écarts-types de la moyenne)
mean = np.mean(data['valeur'])
std = np.std(data['valeur'])
threshold = 3 * std
data = data[np.abs(data['valeur'] - mean) < threshold]

# Normalisation des données (par exemple, mise à l'échelle des valeurs entre 0 et 1)
data['valeur_normalisee'] = (data['valeur'] - data['valeur'].min()) / (data['valeur'].max() - data['valeur'].min())

# Affichage des données nettoyées
print(data)
