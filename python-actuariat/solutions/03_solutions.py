"""Corrigés — Leçon 3"""


def annuite_immediate(i, n):
    v = 1 / (1 + i)
    return (1 - v ** n) / i


# 1) Mensualité
def mensualite(K, taux_annuel, annees):
    i = (1 + taux_annuel) ** (1 / 12) - 1
    n = annees * 12
    return K * i / (1 - (1 + i) ** -n)


print(f"1) Prêt de 150 000 sur 20 ans à 3,5 % : {mensualite(150000, 0.035, 20):.2f} / mois")


# 2) Perpétuité
def annuite_perpetuelle(i):
    return 1 / i


print(f"2) perpétuité {annuite_perpetuelle(0.05):.6f} vs a_1000 {annuite_immediate(0.05, 1000):.6f}")


# 3) Annuité différée
def annuite_differee(i, n, m):
    v = 1 / (1 + i)
    return v ** m * annuite_immediate(i, n)


print(f"3) 10 paiements différés de 5 ans à 4 % : {annuite_differee(0.04, 10, 5):.4f}")
