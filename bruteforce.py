from itertools import combinations
import time

# Définir les données sur les actions
actions = [
    {"nom": "Action-1", "cout": 20, "benefice": 5},
    {"nom": "Action-2", "cout": 30, "benefice": 10},
    {"nom": "Action-3", "cout": 50, "benefice": 15},
    {"nom": "Action-4", "cout": 70, "benefice": 20},
    {"nom": "Action-5", "cout": 60, "benefice": 17},
    {"nom": "Action-6", "cout": 80, "benefice": 25},
    {"nom": "Action-7", "cout": 22, "benefice": 7},
    {"nom": "Action-8", "cout": 26, "benefice": 11},
    {"nom": "Action-9", "cout": 48, "benefice": 13},
    {"nom": "Action-10", "cout": 34, "benefice": 27},
    {"nom": "Action-11", "cout": 42, "benefice": 17},
    {"nom": "Action-12", "cout": 110, "benefice": 9},
    {"nom": "Action-13", "cout": 38, "benefice": 23},
    {"nom": "Action-14", "cout": 14, "benefice": 1},
    {"nom": "Action-15", "cout": 18, "benefice": 3},
    {"nom": "Action-16", "cout": 8, "benefice": 8},
    {"nom": "Action-17", "cout": 4, "benefice": 12},
    {"nom": "Action-18", "cout": 10, "benefice": 14},
    {"nom": "Action-19", "cout": 24, "benefice": 21},
    {"nom": "Action-20", "cout": 114, "benefice": 18},
]

budget_max = 500

def calculer_benefice_total(choix):
    """Calculer le bénéfice total d'une combinaison d'actions."""
    return sum(action["cout"] * (action["benefice"] / 100) for action in choix)

def trouver_meilleur_investissement(actions, budget_max):
    """Trouver la meilleure combinaison d'actions pour maximiser le bénéfice total."""
    meilleur_benefice = 0
    meilleure_combinaison = []

    # Essayer toutes les combinaisons possibles d'actions
    for i in range(1, len(actions) + 1):
        for combinaison in combinations(actions, i):
            cout_total = sum(action["cout"] for action in combinaison)
            if cout_total <= budget_max:
                benefice_total = calculer_benefice_total(combinaison)
                if benefice_total > meilleur_benefice:
                    meilleur_benefice = benefice_total
                    meilleure_combinaison = combinaison

    return meilleure_combinaison, meilleur_benefice

start = time.time()
# Trouver la meilleure combinaison d'actions
meilleure_combinaison, meilleur_benefice = trouver_meilleur_investissement(actions, budget_max)
end = time.time()
print(end - start)

# Calculer le coût total de la meilleure combinaison
budget_utilise = sum(action["cout"] for action in meilleure_combinaison)

# Afficher le résultat
print("Meilleure combinaison d'actions:")
for action in meilleure_combinaison:
    print(f"{action['nom']} - Coût: {action['cout']}€, Bénéfice: {action['benefice']}%")

# Afficher le budget utilisé
print(f"\nBudget utilisé: {budget_utilise:.2f}€")

# Afficher le bénéfice total
print(f"Bénéfice total: {meilleur_benefice:.2f}€")