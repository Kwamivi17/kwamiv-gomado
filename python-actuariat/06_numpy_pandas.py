"""
LEÇON 6 — NumPy et pandas : les outils de l'actuaire
Application : simulation Monte-Carlo d'une charge de sinistres

Prérequis :  pip install numpy pandas
  - NumPy  : calcul sur des tableaux de nombres, très rapide
  - pandas : tableaux de données (comme Excel), lecture de CSV, etc.
"""
import numpy as np
import pandas as pd

# ---------------------------------------------------------------
# 1. NumPy : on calcule sur un tableau ENTIER, sans boucle
# ---------------------------------------------------------------
t = np.arange(1, 11)              # [1, 2, ..., 10]
v = 1 / 1.03 ** t                 # facteurs d'actualisation, d'un coup
print("a_10 à 3 % =", v.sum().round(4))

# ---------------------------------------------------------------
# 2. Simulation : modèle Poisson composé
#    N ~ Poisson(lambda)  nombre de sinistres dans l'année
#    X ~ LogNormale       montant de chaque sinistre
#    S = X_1 + ... + X_N  charge annuelle
# ---------------------------------------------------------------
rng = np.random.default_rng(seed=2026)   # seed fixée -> résultats reproductibles
n_sim = 100_000
lam = 50
mu, sigma = 7.0, 1.2      # paramètres de la lognormale

N = rng.poisson(lam, size=n_sim)
S = np.array([rng.lognormal(mu, sigma, size=n).sum() for n in N])

esperance_theorique = lam * np.exp(mu + sigma ** 2 / 2)
print(f"\nE[S] simulée   : {S.mean():,.0f}")
print(f"E[S] théorique : {esperance_theorique:,.0f}")

# Mesures de risque
var_995 = np.quantile(S, 0.995)            # Value-at-Risk 99,5 % (Solvabilité II)
tvar_995 = S[S >= var_995].mean()           # Tail-VaR
print(f"VaR 99,5 %     : {var_995:,.0f}")
print(f"TVaR 99,5 %    : {tvar_995:,.0f}")

# ---------------------------------------------------------------
# 3. pandas : un DataFrame = un tableau avec des colonnes nommées
# ---------------------------------------------------------------
df = pd.DataFrame({"nb_sinistres": N, "charge": S})
print("\nAperçu :")
print(df.head())
print("\nStatistiques descriptives :")
print(df.describe().round(0))

# Nouvelle colonne, filtre, regroupement
df["grosse_annee"] = df["charge"] > var_995
print(f"\nProportion d'années extrêmes : {df['grosse_annee'].mean():.3%}")

par_nb = df.groupby(pd.cut(df["nb_sinistres"], bins=[0, 40, 50, 60, 200]),
                    observed=True)["charge"].mean()
print("\nCharge moyenne selon le nombre de sinistres :")
print(par_nb.round(0))

# Pour lire un fichier :  df = pd.read_csv("sinistres.csv")
# Pour écrire           :  df.to_csv("resultats.csv", index=False)

# Graphique (nécessite matplotlib) : décommente pour afficher l'histogramme
# import matplotlib.pyplot as plt
# df["charge"].hist(bins=100); plt.axvline(var_995, color="red"); plt.show()

# ===============================================================
# EXERCICES (corrigés dans solutions/06_solutions.py)
# ===============================================================
# 1) Ajoute une réassurance en excédent de sinistre : pour chaque
#    sinistre, l'assureur garde min(X, 20 000). Recalcule E[S] et la VaR.
# 2) Vérifie que la variance simulée de S est proche de
#    lambda * E[X**2] = lambda * exp(2*mu + 2*sigma**2).
# 3) Mets la table de mortalité de la leçon 5 dans un DataFrame
#    avec les colonnes  age, lx, qx  et affiche les 10 premières lignes.
