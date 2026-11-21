"""Corrigés — Leçon 6"""
import math

import numpy as np
import pandas as pd

rng = np.random.default_rng(seed=2026)
n_sim, lam, mu, sigma = 100_000, 50, 7.0, 1.2
priorite = 20_000

N = rng.poisson(lam, size=n_sim)
sinistres = [rng.lognormal(mu, sigma, size=n) for n in N]

S_brut = np.array([x.sum() for x in sinistres])
S_net = np.array([np.minimum(x, priorite).sum() for x in sinistres])

# 1) Réassurance XS
print("1)           brut        net")
print(f"   E[S]  {S_brut.mean():10,.0f} {S_net.mean():10,.0f}")
print(f"   VaR   {np.quantile(S_brut, 0.995):10,.0f} {np.quantile(S_net, 0.995):10,.0f}")

# 2) Variance
var_theorique = lam * math.exp(2 * mu + 2 * sigma ** 2)
print(f"2) Var simulée {S_brut.var():.3e}   théorique {var_theorique:.3e}")

# 3) Table de mortalité dans pandas
A, B, c = 0.0005, 0.00003, 1.10
ages = np.arange(0, 111)
px = np.exp(-(A + B * c ** ages * (c - 1) / np.log(c)))
lx = 100000 * np.concatenate([[1.0], np.cumprod(px)[:-1]])
table = pd.DataFrame({"age": ages, "lx": lx, "qx": 1 - px})
print("3)")
print(table.head(10).round(5).to_string(index=False))
