"""Corrigés — Leçon 5 (on réutilise les fonctions de la leçon)"""
import importlib.util
import pathlib

# Charger le fichier de la leçon 5 comme un module (son nom commence par un chiffre)
chemin = pathlib.Path(__file__).parent.parent / "05_table_mortalite.py"
spec = importlib.util.spec_from_file_location("lecon5", chemin)
l5 = importlib.util.module_from_spec(spec)
print("--- sortie de la leçon 5 ---")
spec.loader.exec_module(l5)
print("--- corrigés ---")


# 1) Capital différé nE_x
def capital_differe(x, n, i):
    return (1 / (1 + i)) ** n * l5.tpx(n, x)


print(f"1) 20E_40 à 2 % = {capital_differe(40, 20, 0.02):.4f}")


# 2) Relation A_x = 1 - d * ä_x
def assurance_vie_entiere(x, i):
    return l5.assurance_deces_temporaire(x, l5.AGE_MAX - x + 1, i)


x, i = 40, 0.02
d = i / (1 + i)
print(f"2) A_x = {assurance_vie_entiere(x, i):.6f}   1 - d*ä_x = {1 - d * l5.rente_viagere_due(x, i):.6f}")

# 3) Prime selon l'âge
print("3) Âge | prime annuelle (capital 100 000, 20 ans)")
for age in range(25, 56, 5):
    prime = (100000 * l5.assurance_deces_temporaire(age, 20, i)
             / l5.rente_temporaire_due(age, 20, i))
    print(f"   {age:4d} | {prime:10.2f}")
