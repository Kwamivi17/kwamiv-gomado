"""Corrigés — Leçon 4"""

portefeuille = [
    {"assure": "Kofi", "age": 40, "capital": 50000},
    {"assure": "Awa", "age": 35, "capital": 80000},
    {"assure": "Yao", "age": 52, "capital": 30000},
]

# 1) Âge moyen
age_moyen = sum(c["age"] for c in portefeuille) / len(portefeuille)
print(f"1) Âge moyen : {age_moyen:.1f}")

# 2) Filtre
plus_de_38 = [c["assure"] for c in portefeuille if c["age"] > 38]
print(f"2) {plus_de_38}")


# 3) Comparaison de projets
def van(flux, i):
    return sum(cf / (1 + i) ** t for t, cf in enumerate(flux))


def tri(flux, bas=-0.99, haut=1.0, tolerance=1e-8):
    while haut - bas > tolerance:
        milieu = (bas + haut) / 2
        if van(flux, milieu) > 0:
            bas = milieu
        else:
            haut = milieu
    return (bas + haut) / 2


projets = {
    "A": [-5000, 1500, 1500, 1500, 1500],
    "B": [-5000, 0, 0, 0, 7000],
}
for nom, flux in projets.items():
    print(f"3) Projet {nom} : VAN 6 % = {van(flux, 0.06):8.2f}   TRI = {tri(flux):.2%}")
print("   -> Ici B l'emporte sur les deux critères ; essaie un taux de 12 % : la VAN de B passe sous celle de A.")
