"""
LEÇON 2 — Conditions et boucles
Application : évolution d'un capital, tableau d'amortissement d'un prêt
"""

# ---------------------------------------------------------------
# 1. Les conditions : if / elif / else
#    ATTENTION : l'indentation (4 espaces) fait partie du langage !
# ---------------------------------------------------------------
age = 67

if age < 18:
    print("Mineur : pas de contrat possible")
elif age <= 65:
    print("Âge accepté au tarif standard")
else:
    print("Âge accepté avec surprime")

# Opérateurs de comparaison : ==  !=  <  <=  >  >=
# Opérateurs logiques       : and  or  not
fumeur = True
if age > 60 and fumeur:
    print("Questionnaire médical renforcé")

# ---------------------------------------------------------------
# 2. La boucle for : répéter pour chaque élément
#    range(1, 6) produit 1, 2, 3, 4, 5  (la borne de fin est EXCLUE)
# ---------------------------------------------------------------
capital = 1000
taux = 0.05

print("\nAnnée | Capital")
for annee in range(1, 6):
    capital = capital * (1 + taux)     # on écrase l'ancienne valeur
    print(f"{annee:5d} | {capital:10.2f}")

# ---------------------------------------------------------------
# 3. La boucle while : répéter TANT QUE la condition est vraie
#    Ici : combien d'années pour atteindre 2000 ?
# ---------------------------------------------------------------
capital = 1000
annees = 0
while capital < 2000:
    capital *= 1 + taux    # raccourci pour capital = capital * (1 + taux)
    annees += 1
print(f"\nCapital doublé après {annees} ans ({capital:.2f})")

# ---------------------------------------------------------------
# 4. Tableau d'amortissement d'un prêt à annuités constantes
#    Annuité : a = K * i / (1 - (1 + i) ** -n)
# ---------------------------------------------------------------
K = 20000     # montant emprunté
i = 0.04      # taux annuel
n = 5         # nombre d'annuités

annuite = K * i / (1 - (1 + i) ** -n)
restant = K

print(f"\nAnnuité constante : {annuite:.2f}")
print(f"{'Année':>5} {'Début':>10} {'Intérêts':>10} {'Amort.':>10} {'Fin':>10}")
for annee in range(1, n + 1):
    interets = restant * i
    amortissement = annuite - interets
    fin = restant - amortissement
    print(f"{annee:>5} {restant:>10.2f} {interets:>10.2f} {amortissement:>10.2f} {fin:>10.2f}")
    restant = fin

# ===============================================================
# EXERCICES (corrigés dans solutions/02_solutions.py)
# ===============================================================
# 1) Écris une condition qui affiche la classe de bonus-malus :
#    coefficient < 1 -> "bonus", == 1 -> "neutre", > 1 -> "malus".
# 2) Avec une boucle for, calcule la somme des valeurs actuelles
#    de 10 versements de 100 en fin d'année au taux de 3 %.
#    (valeur actuelle du versement k : 100 / 1.03 ** k)
# 3) Refais le tableau d'amortissement avec un amortissement
#    CONSTANT (K / n chaque année) au lieu d'une annuité constante.
