"""
LEÇON 4 — Listes et dictionnaires
Application : flux de trésorerie, VAN et TRI
"""

# ---------------------------------------------------------------
# 1. Les listes : une suite ordonnée de valeurs, entre [ ]
#    Les indices commencent à 0 !
# ---------------------------------------------------------------
flux = [-1000, 300, 400, 500]   # investissement puis recettes annuelles

print(flux[0])        # -1000  (premier élément)
print(flux[-1])       # 500    (dernier élément)
print(len(flux))      # 4      (longueur)
print(flux[1:3])      # [300, 400]  (« tranche » : de l'indice 1 inclus à 3 exclu)

flux.append(200)      # ajouter à la fin
print(flux)
print(sum(flux), max(flux), min(flux))

# ---------------------------------------------------------------
# 2. Parcourir une liste avec enumerate (donne l'indice ET la valeur)
# ---------------------------------------------------------------
for t, montant in enumerate(flux):
    print(f"t = {t} : {montant}")


# ---------------------------------------------------------------
# 3. Valeur actuelle nette (VAN) :  somme des CF_t / (1 + i) ** t
# ---------------------------------------------------------------
def van(flux, i):
    total = 0
    for t, cf in enumerate(flux):
        total += cf / (1 + i) ** t
    return total


print(f"\nVAN à 5 % : {van(flux, 0.05):.2f}")

# Version compacte avec une « compréhension de liste »
valeurs_actuelles = [cf / 1.05 ** t for t, cf in enumerate(flux)]
print([round(x, 2) for x in valeurs_actuelles])


# ---------------------------------------------------------------
# 4. TRI : le taux qui annule la VAN. On le cherche par DICHOTOMIE :
#    on coupe l'intervalle en deux jusqu'à trouver la racine.
# ---------------------------------------------------------------
def tri(flux, bas=-0.99, haut=1.0, tolerance=1e-8):
    while haut - bas > tolerance:
        milieu = (bas + haut) / 2
        if van(flux, milieu) > 0:   # VAN décroissante en i pour ce type de flux
            bas = milieu
        else:
            haut = milieu
    return (bas + haut) / 2


taux_tri = tri(flux)
print(f"TRI : {taux_tri:.4%}   (VAN au TRI : {van(flux, taux_tri):.6f})")

# ---------------------------------------------------------------
# 5. Les dictionnaires : des paires  clé -> valeur, entre { }
# ---------------------------------------------------------------
contrat = {
    "numero": "AV-2026-001",
    "assure": "Kofi",
    "age": 40,
    "capital": 50000,
}
print(contrat["assure"])
contrat["prime"] = 320.5           # ajouter une clé
for cle, valeur in contrat.items():
    print(f"{cle:>8} : {valeur}")

# Une liste de dictionnaires = un petit portefeuille (comme un tableau Excel)
portefeuille = [
    {"assure": "Kofi", "age": 40, "capital": 50000},
    {"assure": "Awa", "age": 35, "capital": 80000},
    {"assure": "Yao", "age": 52, "capital": 30000},
]
capital_total = sum(c["capital"] for c in portefeuille)
print(f"\nCapital total assuré : {capital_total}")

# ===============================================================
# EXERCICES (corrigés dans solutions/04_solutions.py)
# ===============================================================
# 1) Calcule l'âge moyen du portefeuille.
# 2) Construis la liste des assurés de plus de 38 ans.
# 3) Compare deux projets avec la VAN à 6 % et le TRI :
#    A = [-5000, 1500, 1500, 1500, 1500]   B = [-5000, 0, 0, 0, 7000]
