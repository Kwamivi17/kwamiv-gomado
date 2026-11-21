"""Corrigés — Leçon 1"""
import math

# 1) Valeur actuelle
C_n, i, n = 15000, 0.04, 8
C_0 = C_n / (1 + i) ** n
print(f"1) Somme à placer : {C_0:,.2f}")

# 2) Taux d'escompte
i = 0.05
d = i / (1 + i)
print(f"2) d = {d:.4%}")

# 3) Temps de doublement
i = 0.06
n = math.log(2) / math.log(1 + i)
print(f"3) Doublement en {n:.2f} ans (règle de 72 : {72 / 6:.0f} ans)")
