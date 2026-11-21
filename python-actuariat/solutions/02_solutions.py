"""Corrigés — Leçon 2"""

# 1) Bonus-malus
coefficient = 0.85
if coefficient < 1:
    print("1) bonus")
elif coefficient == 1:
    print("1) neutre")
else:
    print("1) malus")

# 2) Somme des valeurs actuelles
total = 0
for k in range(1, 11):
    total += 100 / 1.03 ** k
print(f"2) Valeur actuelle : {total:.2f}")

# 3) Amortissement constant
K, i, n = 20000, 0.04, 5
amortissement = K / n
restant = K
print(f"3) {'Année':>5} {'Intérêts':>10} {'Annuité':>10} {'Fin':>10}")
for annee in range(1, n + 1):
    interets = restant * i
    annuite = amortissement + interets
    restant -= amortissement
    print(f"   {annee:>5} {interets:>10.2f} {annuite:>10.2f} {restant:>10.2f}")
