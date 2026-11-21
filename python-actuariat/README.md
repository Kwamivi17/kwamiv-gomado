# Apprendre Python pour l'actuariat — parcours débutant

Ce dossier contient un parcours progressif : chaque leçon est un fichier Python
commenté que tu peux **lire, exécuter puis modifier**. Tous les exemples viennent
de l'actuariat (intérêts, annuités, tables de mortalité, sinistres).

## 0. Installer Python

1. Télécharge Python 3 sur <https://www.python.org/downloads/> (coche « Add Python to PATH » sous Windows).
2. Installe un éditeur : **VS Code** (+ extension « Python ») ou **Thonny** (très simple pour débuter).
3. Pour la leçon 6, installe les bibliothèques scientifiques :
   ```bash
   pip install numpy pandas matplotlib
   ```

> Sans rien installer, tu peux aussi tout tester sur <https://colab.research.google.com>.

## 1. Exécuter une leçon

Dans un terminal, depuis ce dossier :

```bash
python 01_bases.py
```

## 2. Le parcours

| Leçon | Notions Python | Application actuarielle |
|------|----------------|-------------------------|
| `01_bases.py` | variables, types, opérations, `print`, f-strings | intérêts simples et composés |
| `02_conditions_boucles.py` | `if/elif/else`, `for`, `while`, `range` | capitalisation année par année, tableau d'amortissement |
| `03_fonctions.py` | `def`, paramètres, `return`, valeurs par défaut | facteur d'actualisation, annuités certaines |
| `04_listes_dictionnaires.py` | listes, dictionnaires, boucles sur collections | VAN, TRI par dichotomie |
| `05_table_mortalite.py` | tout combiné | `l_x`, `q_x`, `p_x`, espérance de vie, rente viagère, assurance décès |
| `06_numpy_pandas.py` | NumPy, pandas, simulation aléatoire | Monte-Carlo d'un modèle de sinistres Poisson composé |

Chaque fichier se termine par des **exercices**. Les corrigés sont dans
`solutions/` — essaie vraiment avant de regarder !

## 3. Méthode conseillée

- **30 à 45 minutes par jour** valent mieux que 5 heures le dimanche.
- Ne fais pas que lire : **change les valeurs**, casse le code, lis le message d'erreur.
- Un message d'erreur se lit **de bas en haut** : la dernière ligne dit ce qui ne va pas.
- Après ce parcours : refais tes exercices de mathématiques financières / actuariat en Python.

## 4. Ressources pour la suite

- Tutoriel officiel (en français) : <https://docs.python.org/fr/3/tutorial/>
- pandas — « 10 minutes to pandas » : <https://pandas.pydata.org/docs/user_guide/10min.html>
- Bibliothèques actuarielles : `chainladder` (provisionnement IARD), `lifelib` (modèles vie).
