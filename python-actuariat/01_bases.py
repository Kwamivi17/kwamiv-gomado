"""
LEÇON 1 — Les bases : variables, types et calculs
Application : intérêts simples et composés

Lance ce fichier avec :  python 01_bases.py
Tout ce qui suit un # est un COMMENTAIRE : Python l'ignore.
"""

# ---------------------------------------------------------------
# 1. Afficher quelque chose
# ---------------------------------------------------------------
print("Bonjour, futur actuaire !")

# ---------------------------------------------------------------
# 2. Les variables : on donne un NOM à une valeur
# ---------------------------------------------------------------
capital = 10000        # un entier (int)
taux = 0.03            # un nombre décimal (float) : 3 % s'écrit 0.03
duree = 5              # en années
nom_client = "Awa"     # une chaîne de caractères (str), entre guillemets

# type() indique le type d'une valeur
print(type(capital), type(taux), type(nom_client))

# ---------------------------------------------------------------
# 3. Les opérations
#    +  -  *  /     addition, soustraction, multiplication, division
#    **             puissance  (2 ** 3 = 8)
#    //  %          division entière et reste
# ---------------------------------------------------------------
print(7 / 2)    # 3.5
print(7 // 2)   # 3
print(7 % 2)    # 1
print(1.03 ** 2)

# ---------------------------------------------------------------
# 4. Intérêts simples :   C_n = C_0 * (1 + n * i)
# ---------------------------------------------------------------
valeur_simple = capital * (1 + duree * taux)

# ---------------------------------------------------------------
# 5. Intérêts composés :  C_n = C_0 * (1 + i) ** n
# ---------------------------------------------------------------
valeur_composee = capital * (1 + taux) ** duree

# ---------------------------------------------------------------
# 6. Afficher proprement avec une f-string
#    f"... {variable} ..."  insère la valeur dans le texte
#    {x:.2f} = 2 décimales,  {x:,.2f} = séparateur de milliers
# ---------------------------------------------------------------
print(f"Client : {nom_client}")
print(f"Intérêts simples  après {duree} ans : {valeur_simple:,.2f}")
print(f"Intérêts composés après {duree} ans : {valeur_composee:,.2f}")
print(f"Écart : {valeur_composee - valeur_simple:.2f}")

# ---------------------------------------------------------------
# 7. Taux équivalents : un taux annuel i correspond à un taux
#    mensuel i_m tel que (1 + i_m) ** 12 = 1 + i
# ---------------------------------------------------------------
taux_mensuel = (1 + taux) ** (1 / 12) - 1
print(f"Taux mensuel équivalent à {taux:.2%} annuel : {taux_mensuel:.4%}")

# ===============================================================
# EXERCICES (corrigés dans solutions/01_solutions.py)
# ===============================================================
# 1) Quelle somme faut-il placer aujourd'hui à 4 % composés pour
#    obtenir 15 000 dans 8 ans ?   (indice : C_0 = C_n / (1+i)**n)
# 2) Calcule le taux d'escompte d = i / (1 + i) pour i = 5 %.
# 3) Combien d'années faut-il pour doubler un capital à 6 % ?
#    (indice : n = ln(2) / ln(1+i) ; tape  import math  puis math.log(...))
