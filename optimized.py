import csv
import time

def lire_donnees_csv(fichier_csv):
    actions = []
    with open(fichier_csv, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for index, row in enumerate(reader, start=1):  # `enumerate` pour obtenir le numéro de ligne
                cout = float(row["cout"])  # Conversion en float avant d'ignorer les valeurs négatives
                if cout <= 0:
                    # Ignorer les lignes avec des coûts négatifs ou nuls
                    print(f"Ligne {index} ignorée : coût négatif ou nul ({cout}).")
                    continue
                actions.append({
                    "nom": row["nom"],
                    "cout": int(float(row["cout"]) * 100),
                    "benefice": int(float(row["cout"]) * float(row["benefice"]) / 100 * 100)
                })
    return actions

def trouver_meilleur_investissement_optimise(actions, budget_max):
    n = len(actions)
    # Initialiser une matrice de zéro pour stocker les bénéfices maximums
    dp = [[0 for _ in range(budget_max + 1)] for _ in range(n + 1)]

    # Remplir la matrice dp
    for i in range(1, n + 1):
        cout = actions[i - 1]["cout"]
        benefice = actions[i - 1]["benefice"]  # Le bénéfice est déjà calculé en valeur absolue
        for w in range(1, budget_max + 1):
            if cout <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cout] + benefice)
            else:
                dp[i][w] = dp[i - 1][w]

    # Extraire les éléments choisis
    y = budget_max
    meilleure_combinaison = []
    for i in range(n, 0, -1):
        if dp[i][y] != dp[i - 1][y]:
            meilleure_combinaison.append(actions[i - 1])
            y -= actions[i - 1]["cout"]

    # Calculer le meilleur bénéfice
    meilleur_benefice = dp[n][budget_max]

    return meilleure_combinaison, meilleur_benefice

# Lire les données depuis le fichier CSV
fichier_csv = 'actions.csv'
actions = lire_donnees_csv(fichier_csv)

# Définir le budget maximum
budget_max = 50000

start = time.time()
# Trouver la meilleure combinaison d'actions
meilleure_combinaison, meilleur_benefice = trouver_meilleur_investissement_optimise(actions, budget_max)
end = time.time()
print(end - start)

# Affichage des résultats (conversion centimes -> euros)
budget_utilise = sum(action["cout"] for action in meilleure_combinaison) / 100  # Convertir en euros
print("Meilleure combinaison d'actions:")
for action in meilleure_combinaison:
    # Convertir les valeurs en euros pour l'affichage
    cout_en_euros = action["cout"] / 100
    benefice_en_euros = action["benefice"] / 100
    print(f"{action['nom']} - Coût: {cout_en_euros:.2f}€, Bénéfice: {benefice_en_euros:.2f}€")

# Afficher le budget et bénéfice total en euros
print(f"\nBudget utilisé: {budget_utilise:.2f}€")
print(f"Bénéfice total: {meilleur_benefice / 100:.2f}€")  # Convertir en euros
