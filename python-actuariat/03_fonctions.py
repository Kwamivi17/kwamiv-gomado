"""
LEÇON 3 — Les fonctions
Application : boîte à outils de mathématiques financières

Une fonction = un bloc de code réutilisable, avec des entrées
(paramètres) et une sortie (return). C'est comme une formule.
"""


# ---------------------------------------------------------------
# 1. Définir une fonction avec def
# ---------------------------------------------------------------
def facteur_actualisation(i):
    """Renvoie v = 1 / (1 + i)."""      # la « docstring » documente la fonction
    return 1 / (1 + i)


def valeur_actuelle(montant, i, n):
    """Valeur actuelle d'un montant payé dans n années."""
    return montant * facteur_actualisation(i) ** n


print(facteur_actualisation(0.05))
print(f"{valeur_actuelle(1000, 0.05, 10):.2f}")


# ---------------------------------------------------------------
# 2. Annuités certaines
#    a_n  (paiements en FIN de période)   = (1 - v**n) / i
#    ä_n  (paiements en DÉBUT de période) = (1 - v**n) / d,  d = i/(1+i)
# ---------------------------------------------------------------
def annuite_immediate(i, n):
    """a_n : valeur actuelle de n paiements de 1 en fin d'année."""
    v = facteur_actualisation(i)
    return (1 - v ** n) / i


def annuite_due(i, n):
    """ä_n : valeur actuelle de n paiements de 1 en début d'année."""
    v = facteur_actualisation(i)
    d = i / (1 + i)
    return (1 - v ** n) / d


print(f"a_10 à 5 % = {annuite_immediate(0.05, 10):.4f}")
print(f"ä_10 à 5 % = {annuite_due(0.05, 10):.4f}")


# ---------------------------------------------------------------
# 3. Paramètres par défaut et appel par nom
# ---------------------------------------------------------------
def valeur_acquise(capital, n, i=0.03):
    """Valeur acquise ; si on ne précise pas i, on prend 3 %."""
    return capital * (1 + i) ** n


print(valeur_acquise(1000, 10))            # utilise i = 3 %
print(valeur_acquise(1000, 10, i=0.06))    # appel par nom : plus lisible


# ---------------------------------------------------------------
# 4. Vérifier son code : comparer à un calcul « à la main »
#    a_n doit être égal à la somme des v**k pour k = 1..n
# ---------------------------------------------------------------
i, n = 0.04, 7
somme = 0
for k in range(1, n + 1):
    somme += facteur_actualisation(i) ** k
print(f"Formule : {annuite_immediate(i, n):.6f}   Somme : {somme:.6f}")

# ===============================================================
# EXERCICES (corrigés dans solutions/03_solutions.py)
# ===============================================================
# 1) Écris une fonction  mensualite(K, taux_annuel, annees)  qui renvoie
#    la mensualité d'un prêt (convertis d'abord le taux en taux mensuel
#    équivalent, puis applique  K * i / (1 - (1+i)**-n)).
# 2) Écris  annuite_perpetuelle(i)  = 1 / i  et vérifie que
#    annuite_immediate(i, 1000) en est très proche.
# 3) Écris  annuite_differee(i, n, m) : n paiements commençant après
#    m années de différé  ( = v**m * a_n ).
