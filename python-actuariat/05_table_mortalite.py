"""
LEÇON 5 — Projet : une table de mortalité
On combine tout : listes, boucles, fonctions, dictionnaires.

Notations :
  l_x : nombre de survivants à l'âge x
  d_x = l_x - l_{x+1}  : décès entre x et x+1
  q_x = d_x / l_x      : probabilité de décéder dans l'année
  p_x = 1 - q_x        : probabilité de survivre un an
  _tp_x = l_{x+t} / l_x : probabilité de survivre t années
"""
import math

# ---------------------------------------------------------------
# 1. Construire une table « jouet » avec la loi de Gompertz-Makeham
#    mu_x = A + B * c**x   (force de mortalité)
#    p_x  = exp(-(A + B * c**x * (c - 1) / ln c))
#    (Dans la vraie vie, tu importerais une table réglementaire.)
# ---------------------------------------------------------------
A, B, c = 0.0005, 0.00003, 1.10
AGE_MAX = 110


def proba_survie_1an(x):
    return math.exp(-(A + B * c ** x * (c - 1) / math.log(c)))


lx = {0: 100000.0}
for x in range(0, AGE_MAX):
    lx[x + 1] = lx[x] * proba_survie_1an(x)
lx[AGE_MAX + 1] = 0.0     # personne ne survit au-delà


# ---------------------------------------------------------------
# 2. Fonctions de base
# ---------------------------------------------------------------
def qx(x):
    return (lx[x] - lx[x + 1]) / lx[x]


def tpx(t, x):
    """Probabilité qu'une personne d'âge x survive t années."""
    if x + t > AGE_MAX + 1:
        return 0.0
    return lx[x + t] / lx[x]


def esperance_vie(x):
    """Espérance de vie résiduelle abrégée e_x = somme des _tp_x (t >= 1)."""
    return sum(tpx(t, x) for t in range(1, AGE_MAX - x + 2))


print(" Âge       l_x       q_x     e_x")
for x in [0, 20, 40, 60, 80, 100]:
    print(f"{x:4d} {lx[x]:10.0f} {qx(x):9.5f} {esperance_vie(x):7.2f}")


# ---------------------------------------------------------------
# 3. Rente viagère due :  ä_x = somme_{t>=0} v**t * _tp_x
#    Valeur actuelle de 1 payé chaque début d'année tant que l'assuré vit.
# ---------------------------------------------------------------
def rente_viagere_due(x, i):
    v = 1 / (1 + i)
    return sum(v ** t * tpx(t, x) for t in range(0, AGE_MAX - x + 1))


# ---------------------------------------------------------------
# 4. Assurance décès temporaire n ans (capital 1 payé en fin d'année du décès)
#    A^1_{x:n} = somme_{t=0}^{n-1} v**(t+1) * _tp_x * q_{x+t}
# ---------------------------------------------------------------
def assurance_deces_temporaire(x, n, i):
    v = 1 / (1 + i)
    return sum(v ** (t + 1) * tpx(t, x) * qx(x + t) for t in range(n))


def rente_temporaire_due(x, n, i):
    v = 1 / (1 + i)
    return sum(v ** t * tpx(t, x) for t in range(n))


i = 0.02
x = 40
print(f"\nÀ {x} ans, taux technique {i:.0%} :")
print(f"  Rente viagère due ä_x           = {rente_viagere_due(x, i):.4f}")

capital, n = 100000, 20
vap_prestation = capital * assurance_deces_temporaire(x, n, i)
vap_primes = rente_temporaire_due(x, n, i)
prime_annuelle = vap_prestation / vap_primes   # principe d'équivalence

print(f"  Temporaire décès {n} ans, capital {capital:,} :")
print(f"    prime unique   = {vap_prestation:,.2f}")
print(f"    prime annuelle = {prime_annuelle:,.2f}")

# ===============================================================
# EXERCICES (corrigés dans solutions/05_solutions.py)
# ===============================================================
# 1) Écris  capital_differe(x, n, i) = v**n * _np_x  (nE_x) : valeur
#    actuelle de 1 versé à l'âge x+n si l'assuré est vivant.
# 2) Vérifie numériquement la relation  A_x = 1 - d * ä_x  pour
#    l'assurance vie entière A_x (somme jusqu'à AGE_MAX).
# 3) Trace l'évolution de la prime annuelle de la temporaire 20 ans
#    pour des âges de souscription de 25 à 55 ans (un print par âge).
